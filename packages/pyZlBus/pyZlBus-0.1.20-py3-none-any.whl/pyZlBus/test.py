# -*- coding: utf-8 -*-
#! -*-conding=: UTF-8 -*-
# 2023/5/6 15:53
import asyncio
import platform
from time import time, sleep
from bleak import BleakClient, BleakScanner
from bleak.backends.characteristic import BleakGATTCharacteristic
from threading import Thread

import pyZlBus.pyZlBus as zlb

# Serivce Characteristic UUID
CmdCtrl_WriteNotify_UUID = "AEC91001-6E7A-4BC2-9A4C-4CDA7A728F58"   # characteristic
UploadData_Notify_UUID   = "AEC91002-6E7A-4BC2-9A4C-4CDA7A728F58"   # characteristic
TxData_Notify_UUID       = "AEC91003-6E7A-4BC2-9A4C-4CDA7A728F58"   # characteristic

DEBUG = 0

class ZlBusSdk(Thread):
    def __init__(self, advNameStr: str = ''):
        Thread.__init__(self)  # 必须步骤
        if platform.system() == 'Windows':
            asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
        self.advNameStr  = advNameStr
        self.bFound      = False
        self.bQuit       = False
        self.blueAddr    = ""
        self.findAddr    = {}
        self.client      = None
        # step 1, 实例化解包单元,并设置内部解包FIFO大小
        self.pkt = zlb.ZlBusUnPack(fifoMaxSize = 20)

        # step 2, 手动设置上传数据流水号编码, 默认FLOW_ID_FORMAT_8
        self.pkt.setFlowIdFormat(zlb.e_FLOW_FORMAT.FLOW_ID_FORMAT_8.value)

        # step 3, 手动设置上传数据的数据格式，用于解包格式识别，错误的数据格式，无法解包成功，包数据直接丢弃
        # pkt.setDataFormat((zlb.e_UpLoadDataForMat.UPLOAD_DATA_TIME.value | zlb.e_UpLoadDataForMat.UPLOAD_DATA_QUATERNION.value|
        #                    zlb.e_UpLoadDataForMat.UPLOAD_DATA_GYRO.value | zlb.e_UpLoadDataForMat.UPLOAD_DATA_LIN_ACC.value))
        # or
        # 通过蓝牙获取, 见listenData函数中的如下调用 await client.write_gatt_char(CmdCtrl_WriteNotify_UUID, zlb.ul_getDataFormat(), response=True)

    def detection_callback(self, device, advertisement_data):
        if self.advNameStr != '':
            if device.name == self.advNameStr:
                self.blueAddr = device.address
                self.bFound = True
        elif device is not None and device.name is not None:
            if device.name.startswith("zl") or device.name.startswith("ZL"):
                if device.address in self.findAddr:
                    pass
                else:
                    self.findAddr[device.address] = device.name
                    print(device.name, " | ", device.address)

    def notification_handler(self, characteristic: BleakGATTCharacteristic, data: bytearray):
        if (DEBUG):
            print("low level rev data:",data) 

        try:
            # step 4 将流数据加入进，解包接口
            self.pkt.decodeDataStreamInput(bytes(data))
            
            # step 5 查询解包后,FIFO Block个数
            while self.pkt.count() > 0:
                # step 6 获取FIFO Block, 无效Block 或FIFO 中无数据时,返回None
                block =  self.pkt.getHeadBlockNote()
                if block != None:
                    if isinstance(block, zlb.ImuDataBlock):
                        print('IMU 数据 类型')
                        state, timeMs = block.getTimeStamp()
                        if state:
                            print("时间戳[ms]:", timeMs)
                        state, quat = block.getAhrsQuaternion()
                        if state:
                            print("四元数[w x y z]:", quat.w, quat.x, quat.y, quat.z)
                        state, euler = block.getAhrsEuler()
                        if state:
                            print("欧拉角[roll pitch yaw]:", euler.roll, euler.pitch, euler.yaw)
                        state, acc = block.getAcc()
                        if state:
                            print("加速度[x y z]:", acc.x, acc.y, acc.z)
                        state, gyro = block.getGyro()
                        if state:
                            print("陀螺仪[x y z]:", gyro.x, gyro.y, gyro.z)
                        state, mag = block.getMag()
                        if state:
                            print("磁力计[x y z]:", mag.x, mag.y, mag.z)
                        state, linAcc = block.getLinAcc()
                        if state:
                            print("线性加速度[x y z]:", linAcc.x, linAcc.y, linAcc.z)
                    elif isinstance(block, zlb.BatteryBlock):
                        print('电池 数据 类型')
                        state, mv = block.getAdcMv()
                        if state:
                            print("电池电压:", mv)
                        state, level = block.getLevel()
                        if state:
                            print("电池电量:", level)
                    elif isinstance(block, zlb.UploadDataFormatBlock):
                        format = block.getUploadDataFormat()
                        print("上报数据格式:", hex(format))
                    elif isinstance(block, zlb.FlowIdFormatBlock):
                        print('上传数据流水号格式')
                        self.pkt.setFlowIdFormat(block.getFlowIdFormat())
                    else:
                        print("其他数据类型", type(block))
        except Exception as e:
            print(f'数据解析异常 [Error] -> {e}')
            print(data.hex(' '))

    async def findBlue(self, timeout: float = 5.0):
        try:
            print(' 1、搜索Ble设备...')
            self.findAddr.clear()
            self.bFound = False
            self.client = None
            endTime = time() + timeout
            async with BleakScanner(detection_callback = self.detection_callback) as scanner:
                if platform.system() == 'Windows':
                    await scanner.start()
                while not self.bFound and time() < endTime:
                    await asyncio.sleep(0.1)

            if  self.advNameStr != '':
                if not self.bFound:
                    print('搜索Ble设备超时 [Error]')
                    print('未搜索到指定设备 [Error]')
                else:
                    print(f'搜索到指定设备 MacAddress: {self.blueAddr}')
        except asyncio.CancelledError as e:
            print(f'搜索Ble设备, 协程工作异常 [Error] -> {e}')
        except Exception as e:
            print(f'搜索Ble设备异常 [Error] -> {e}')

    async def listenData(self):
        try:
            print(' 2、连接BLE设备 + IO Test...')

            async with BleakClient(self.blueAddr) as self.client:
                print('    连接BLE设备成功.')
                await asyncio.sleep(0.2)
                await self.client.start_notify(UploadData_Notify_UUID, self.notification_handler)
                await asyncio.sleep(0.1)
                await self.client.start_notify(CmdCtrl_WriteNotify_UUID, self.notification_handler)
                await asyncio.sleep(0.1)
                await self.client.start_notify(TxData_Notify_UUID, self.notification_handler)
                await asyncio.sleep(0.5)
                await self.client.write_gatt_char(CmdCtrl_WriteNotify_UUID, zlb.ul_getDataFormat(), response=True)
                await asyncio.sleep(0.1)
                await self.client.write_gatt_char(CmdCtrl_WriteNotify_UUID, zlb.hl_configOutDataPort(zlb.e_DataOutPort.TK_RF_PORT.value|zlb.e_DataOutPort.TK_UART_PORT.value), response=True)
                await asyncio.sleep(0.1)
                while not self.bQuit:
                    await asyncio.sleep(0.1)

                if self.bQuit:
                    await self.client.disconnect()
                self.client = None
        except asyncio.CancelledError as e:
            print(f'连接BLE设备, 协程工作异常 [Error] -> {e}')
            self.client = None
        except Exception as e:
            print(f'连接BLE设备异常 [Error] -> {e}')
            self.client = None

    def getAddr(self):
        return self.blueAddr

    def setAddr(self, addr):
        self.blueAddr = addr

    def setAdvNameStr(self, name):
        self.advNameStr = name

    def find(self):
        try:
            asyncio.run(self.findBlue())
        except asyncio.CancelledError as e:
            print(f' #1、搜索Ble设备, 协程工作异常 [Error] -> {e}')
        except Exception as e:
            print(f' #1、搜索Ble设备异常 [Error] -> {e}')

    def run(self):
        try:
            asyncio.run(self.listenData())
        except asyncio.CancelledError as e:
            print(f' #2、连接BLE设备, 协程工作异常 [Error] -> {e}')
        except Exception as e:
            print(f' #2、连接BLE设备异常 [Error] -> {e}')

    def stop(self):
        self.bQuit = True

    def waitFound(self, timeout:float = 5.0):
        if self.blueAddr is None:
            return False
        endTime = time() + timeout
        while self.bFound == False:
            sleep(0.1)
            if time() > endTime:
                return False
        return True

    def waitConnect(self, timeout:float = 5.0):
        if self.blueAddr is None:
            return False
        endTime = time() + timeout
        while not(self.client is not None and self.client.is_connected):
            print("waitConnect...")
            sleep(0.1)
            if time() > endTime:
                return False
        return True

    def test(self):
        # 需要解析的数据流（上传数据）
        dataBuffer = [
            0xAA, 0x10, 0x30, 0x00, 0x03, 0x3F, 0x00, 0xB1, 0x81, 0x59, 0x76, 0x49, 0x16, 0x7C, 0x29, 0x3F, 0xF2, 0x28, 0xC0, 0x3B, 0x99, 0x9D, 0x96, 0x3D, 0x0E, 0xEE, 0x3E, 0xBF, 0x36, 0x6A, 0x9D, 0x3F, 0xA5, 0x1E, 0xE4, 0x3F, 0xC5, 0xBE, 0xC4, 0xBE, 0x80, 0x2B, 0x30, 0x3C, 0x80, 0x86, 0x67, 0x3A, 0x00, 0x6C, 0xC4, 0x3A, 0xD7,
            0xAA, 0x10, 0x30, 0x00, 0x03, 0x3F, 0x00, 0xB2, 0xBF, 0x5A, 0x76, 0x49, 0xCF, 0x7B, 0x29, 0x3F, 0x33, 0x8A, 0xBC, 0x3B, 0xD9, 0x38, 0x96, 0x3D, 0x99, 0xEF, 0x3E, 0xBF, 0xA7, 0xAC, 0x15, 0x3E, 0x00, 0xE2, 0x55, 0xC0, 0xBA, 0xA7, 0x20, 0x3F, 0x80, 0xD0, 0x4E, 0x3C, 0x40, 0x37, 0xC6, 0x3A, 0x00, 0x52, 0x27, 0x3B, 0x18,
            0xAA, 0x10, 0x30, 0x00, 0x03, 0x3F, 0x00, 0xB3, 0xFC, 0x5B, 0x76, 0x49, 0x2C, 0x7E, 0x29, 0x3F, 0x15, 0xD8, 0xB3, 0x3B, 0x21, 0xBB, 0x95, 0x3D, 0x2C, 0xEF, 0x3E, 0xBF, 0xE0, 0xF1, 0xD2, 0x3D, 0x00, 0xBC, 0x1A, 0xC0, 0xE0, 0x20, 0xAE, 0x3E, 0x80, 0xED, 0x3A, 0x3C, 0x10, 0x53, 0x83, 0x3B, 0x00, 0x52, 0xB1, 0xBA, 0xB8,
            0xAA, 0x10, 0x30, 0x00, 0x03, 0x3F, 0x00, 0xB4, 0x5F, 0x5D, 0x76, 0x49, 0xB3, 0x7D, 0x29, 0x3F, 0x10, 0xB4, 0xB0, 0x3B, 0x5D, 0x96, 0x95, 0x3D, 0x17, 0xF0, 0x3E, 0xBF, 0x96, 0x66, 0x8E, 0x3E, 0x33, 0x06, 0x03, 0xC0, 0x79, 0x1A, 0xD5, 0x3C, 0x58, 0x87, 0x07, 0x3C, 0x10, 0xAF, 0xB3, 0x3B, 0x00, 0xB4, 0xCE, 0xBB, 0xB6,
            0xAA, 0x10, 0x30, 0x00, 0x03, 0x3F, 0x00, 0xB5, 0x9C, 0x5E, 0x76, 0x49, 0x8E, 0x7F, 0x29, 0x3F, 0xC4, 0x09, 0xA7, 0x3B, 0xD7, 0x1D, 0x95, 0x3D, 0x0E, 0xF0, 0x3E, 0xBF, 0xB8, 0xE3, 0x85, 0x3E, 0xA3, 0xF4, 0x65, 0xC0, 0xC8, 0x7F, 0xCE, 0xBD, 0x20, 0x05, 0xA8, 0x3B, 0x40, 0x7F, 0x61, 0x3B, 0x00, 0xBA, 0xA4, 0xBA, 0xA1,
            0xAA, 0x10, 0x30, 0x00, 0x03, 0x3F, 0x00, 0xB6, 0xDB, 0x5F, 0x76, 0x49, 0x9B, 0x80, 0x29, 0x3F, 0xFD, 0x76, 0xA2, 0x3B, 0xE5, 0xDE, 0x94, 0x3D, 0xF3, 0xEF, 0x3E, 0xBF, 0x1D, 0x48, 0x8B, 0x3E, 0x26, 0xDC, 0x3C, 0xBE, 0x27, 0xE3, 0xC5, 0xBE, 0x0C, 0xEA, 0x9F, 0x3C, 0xE0, 0xDB, 0x60, 0x3B, 0x00, 0xC8, 0x8F, 0x39, 0x82,
            0xAA, 0x10, 0x30, 0x00, 0x03, 0x3F, 0x00, 0xB7, 0x19, 0x61, 0x76, 0x49, 0x69, 0x77, 0x29, 0x3F, 0x88, 0x4E, 0xB2, 0x3B, 0x5B, 0x98, 0x95, 0x3D, 0xA0, 0xF5, 0x3E, 0xBF, 0x16, 0x50, 0x85, 0x3F, 0x66, 0xFA, 0x86, 0x40, 0x80, 0x39, 0x68, 0xBE, 0xD8, 0x13, 0x65, 0x3C, 0xD0, 0x69, 0xA3, 0x3B, 0x80, 0x95, 0x1D, 0x3C, 0xA5,
            0xAA, 0x10, 0x30, 0x00, 0x03, 0x3F, 0x00, 0xB8, 0x57, 0x62, 0x76, 0x49, 0xCA, 0x6C, 0x29, 0x3F, 0x24, 0xDB, 0xCD, 0x3B, 0xD4, 0xC4, 0x96, 0x3D, 0xEC, 0xFA, 0x3E, 0xBF, 0xA1, 0x9C, 0x56, 0x3E, 0x37, 0x99, 0x16, 0xBE, 0x37, 0xBD, 0x65, 0x3B, 0xC0, 0x4A, 0x1A, 0x3B, 0x80, 0x43, 0x9D, 0x3B, 0x80, 0x2F, 0x44, 0xBC, 0xDA,
            0xAA, 0x10, 0x30, 0x00, 0x03, 0x3F, 0x00, 0xB9, 0x96, 0x63, 0x76, 0x49, 0x74, 0x70, 0x29, 0x3F, 0x44, 0x43, 0xC2, 0x3B, 0x21, 0x3F, 0x96, 0x3D, 0x83, 0xF9, 0x3E, 0xBF, 0x7D, 0x63, 0x1D, 0xBD, 0x05, 0xA7, 0xC3, 0xC0, 0xA4, 0x26, 0x5C, 0x3E, 0x70, 0xE3, 0xB7, 0x3B, 0x20, 0x5E, 0x89, 0x3B, 0x00, 0x63, 0x1F, 0xBB, 0xD9,
            0xAA, 0x10, 0x30, 0x00, 0x03, 0x3F, 0x00, 0xBA, 0xD4, 0x64, 0x76, 0x49, 0x41, 0x71, 0x29, 0x3F, 0x34, 0x43, 0xBA, 0x3B, 0x47, 0xDD, 0x95, 0x3D, 0x20, 0xFA, 0x3E, 0xBF, 0x2A, 0x87, 0x0C, 0x3F, 0xE9, 0x8B, 0xAA, 0xBF, 0x91, 0x3F, 0x68, 0xBE, 0xD8, 0x3F, 0x25, 0x3C, 0x40, 0xCA, 0x6E, 0x3B, 0x00, 0xE0, 0xF5, 0x38, 0xF2,
            0xAA, 0x10, 0x30, 0x00, 0x03, 0x3F, 0x00, 0xBB, 0x12, 0x66, 0x76, 0x49, 0x11, 0x6E, 0x29, 0x3F, 0x62, 0x07, 0xBF, 0x3B, 0xE7, 0xDF, 0x95, 0x3D, 0xDA, 0xFC, 0x3E, 0xBF, 0xDC, 0x83, 0x72, 0x3F, 0x74, 0xB0, 0x30, 0x3F, 0x7E, 0xA1, 0xB4, 0xBE, 0x80, 0xAD, 0xC4, 0x3B, 0x20, 0xDE, 0x7A, 0x3B, 0x00, 0x3A, 0xF6, 0xBA, 0xBB,
            0xAA, 0x14, 0x07, 0x00, 0x00, 0x3F, 0x00, 0x35, 0x64, 0x60, 0x10, 0xF2,
            0xAA, 0x10, 0x30, 0x00, 0x03, 0x3F, 0x00, 0xBC, 0x51, 0x67, 0x76, 0x49, 0x7B, 0x6E, 0x29, 0x3F, 0x93, 0xEF, 0xC1, 0x3B, 0x6D, 0xE8, 0x95, 0x3D, 0x55, 0xFC, 0x3E, 0xBF, 0x1C, 0x3A, 0x05, 0x3F, 0x00, 0xB7, 0xD0, 0x3D, 0x40, 0xE4, 0x8D, 0x3E, 0xF8, 0x09, 0x17, 0x3C, 0x00, 0xCC, 0x3E, 0x3B, 0x80, 0x90, 0xA6, 0x3B, 0x19,
            0xAA, 0x10, 0x30, 0x00]
        
        # 手动修改上传数据格式
        self.pkt.setDataFormat((zlb.e_UpLoadDataForMat.UPLOAD_DATA_TIME.value | zlb.e_UpLoadDataForMat.UPLOAD_DATA_QUATERNION.value|
                    zlb.e_UpLoadDataForMat.UPLOAD_DATA_GYRO.value | zlb.e_UpLoadDataForMat.UPLOAD_DATA_LIN_ACC.value))

        self.notification_handler(None, dataBuffer)

def bleDemo(advNameStr: str = ''):
    icDev = ZlBusSdk(advNameStr)
    
    if advNameStr == '':
        icDev.find()
        advNameStr = input("输入设备名 或 q 退出: ")
        if advNameStr == 'q' or advNameStr == 'Q' or advNameStr == 'quit':
            return
        else:
            icDev.setAdvNameStr(advNameStr)
    icDev.find()
    if icDev.bFound:
        icDev.start()
        state = icDev.waitConnect()
    else:
        print('未发现设备:', advNameStr)
        return

    if not state:
        print('设备未连接成功')
        return
    
    while True:
        user_input = input("输入'q'退出: ")
        if user_input == 'q' or user_input == 'Q' or user_input == 'quit':
            icDev.stop()
            print("退出程序。")
            break


def demo():
    icDev = ZlBusSdk()
    icDev.test()

__all__ = [bleDemo, demo]
