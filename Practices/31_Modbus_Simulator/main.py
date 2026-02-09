from threading import Thread

from pymodbus.server.sync import StartUdpServer, StartTcpServer
from pymodbus.datastore import ModbusSlaveContext, ModbusServerContext
from pymodbus.datastore import ModbusSequentialDataBlock
import logging
import threading
import time
import multiprocessing
import os
import json
import qdarkstyle
from pathlib import Path
from enum import Enum

NUM_REGISTERS = 65000

ALARM_ON_VALUE = 9
ALARM_OFF_VALUE = 1

VALVE_OPEN_VALUE = 65
VALVE_CLOSE_VALUE = 1

SAFETY_DEVICE_ON_VALUE = 65
SAFETY_DEVICE_OFF_VALUE = 1

ANALOG_MIN_VALUE = 71
ANALOG_MAX_VALUE = 7001

ANY_MIN_VALUE = 1
ANY_MAX_VALUE = 32767

class DeviceType(Enum):
    master = 1
    slice = 2
    h2d = 3

class Simulator:
    def __init__(self, interval, port, exp_master, src_master, exp1, exp2, exp3, src1, src2, src3, src4, src5, src6, src7, src8, h2d_p, h2d_s):
        self.interval = interval
        self.port = port

        self.exp_master_ip = exp_master
        self.src_master_ip = src_master

        self.exp1_ip = exp1
        self.exp2_ip = exp2
        self.exp3_ip = exp3

        self.src1_ip = src1
        self.src2_ip = src2
        self.src3_ip = src3
        self.src4_ip = src4
        self.src5_ip = src5
        self.src6_ip = src6
        self.src7_ip = src7
        self.src8_ip = src8
        self.h2d_p_ip = h2d_p
        self.h2d_s_ip = h2d_s

        print("initialising modbus servers..")
        if self.exp_master_ip is not None:
            self.exp_master = Server(self.exp_master_ip ,port, DeviceType.master, self.interval)
        if self.src_master_ip is not None:
            self.src_master  = Server(self.src_master_ip, port, DeviceType.master, self.interval)

        if self.exp1_ip is not None:
            self.exp1 = Server(self.exp1_ip, port, DeviceType.slice, self.interval)
        if self.exp2_ip is not None:
            self.exp2 = Server(self.exp2_ip, port, DeviceType.slice, self.interval)
        if self.exp3_ip is not None:
            self.exp3 = Server(self.exp3_ip, port, DeviceType.slice, self.interval)

        if self.src1_ip is not None:
            self.src1 = Server(self.src1_ip, port, DeviceType.slice, self.interval)
        if self.src2_ip is not None:
            self.src2 = Server(self.src2_ip, port, DeviceType.slice, self.interval)
        if self.src3_ip is not None:
            self.src3 = Server(self.src3_ip, port, DeviceType.slice, self.interval)
        if self.src4_ip is not None:
            self.src4 = Server(self.src4_ip, port, DeviceType.slice, self.interval)
        if self.src5_ip is not None:
            self.src5 = Server(self.src5_ip, port, DeviceType.slice, self.interval)
        if self.src6_ip is not None:
            self.src6 = Server(self.src6_ip, port, DeviceType.slice, self.interval)
        if self.src7_ip is not None:
            self.src7 = Server(self.src7_ip, port, DeviceType.slice, self.interval)
        if self.src8_ip is not None:
            self.src8 = Server(self.src8_ip, port, DeviceType.slice, self.interval)
        if self.h2d_p_ip is not None:
            self.h2d_p = Server(self.h2d_p_ip, port, DeviceType.h2d, self.interval)
        if self.h2d_s_ip is not None:
            self.h2d_s = Server(self.h2d_s_ip, port, DeviceType.h2d, self.interval)

        self.initialise()

    def initialise(self):
        pass

class Server:
    def __init__(self, ip, port, device_type, interval):
        self.ip = ip
        self.port = port
        self.device_type = device_type
        self.interval = interval
        self.modbus_store = None
        self.modbus_device = None

        self.set_modbus_store()
        self.set_modbus_device()
        self.modbus_thread = threading.Thread(target=self.start_modbus_server, daemon=True)
        self.modbus_thread.start()

        if self.device_type == DeviceType.master:
            self.set_master_initial_values()
            self.simulate_thread = threading.Thread(target=self.simulate_master_modbus_values, daemon=True)
            self.simulate_thread.start()

        elif self.device_type == DeviceType.slice:
            self.set_slice_initial_values()
            self.simulate_thread = threading.Thread(target=self.simulate_slice_modbus_values, daemon=True)
            self.simulate_thread.start()

        elif self.device_type == DeviceType.h2d:
            self.set_h2d_initial_values()
            self.simulate_thread = threading.Thread(target=self.simulate_h2d_modbus_values, daemon=True)
            self.simulate_thread.start()

    def set_modbus_store(self):
        if self.modbus_store is None:
            self.modbus_store = ModbusSlaveContext(
                di=ModbusSequentialDataBlock(0, [0] * NUM_REGISTERS),
                co=ModbusSequentialDataBlock(0, [0] * NUM_REGISTERS),
                hr=ModbusSequentialDataBlock(0, [0] * NUM_REGISTERS),
                ir=ModbusSequentialDataBlock(0, [0] * NUM_REGISTERS),
            )

    def set_modbus_device(self):
        if self.modbus_device is None and self.modbus_store is not None:
            self.modbus_device = ModbusServerContext(slaves=self.modbus_store, single=True)

    def start_modbus_server(self):
        if self.modbus_device is not None and self.modbus_store is not None:
            print(f"Starting a server on port {self.port} with {self.ip} ip address")
            StartUdpServer(self.modbus_device, address=(self.ip, self.port))

    def set_master_initial_values(self):
        self.modbus_store.setValues(4, address=999, values=[1] * 1000)

    def set_slice_initial_values(self):
        self.modbus_store.setValues(4, address=999, values=[1] * 1000)

    def set_h2d_initial_values(self):
        self.modbus_store.setValues(4, address=999, values=[1] * 1000)

    def simulate_master_modbus_values(self):
        pass
        # flag = False
        # while True:
        #     if flag:
        #         flag = False
        #         self.modbus_store.setValues(4, address=999, values=[ANY_MAX_VALUE] * 1000)
        #
        #     else:
        #         flag = True
        #         self.modbus_store.setValues(4, address=999, values=[ANY_MIN_VALUE] * 1000)
        #
        #     time.sleep(self.interval)

    def simulate_slice_modbus_values(self):
        flag = False
        while True:
            if flag:
                flag = False
                self.modbus_store.setValues(4, address=999, values=[ANY_MAX_VALUE] * 1000)

            else:
                flag = True
                self.modbus_store.setValues(4, address=999, values=[ANY_MIN_VALUE] * 1000)

            time.sleep(self.interval)

    def simulate_h2d_modbus_values(self):
        flag = False
        while True:
            if flag:
                flag = False
                self.modbus_store.setValues(4, address=999, values=[ANY_MAX_VALUE] * 1000)

            else:
                flag = True
                self.modbus_store.setValues(4, address=999, values=[ANY_MIN_VALUE] * 1000)

            time.sleep(self.interval)

    def get_modbus_store(self):
        return self.modbus_store

    def get_modbus_device(self):
        return self.modbus_device


if __name__ == "__main__":
    CONFIG_PATH = Path("config.json")

    with CONFIG_PATH.open(encoding="utf-8") as f:
        CONFIG = json.load(f)

    INTERVAL = CONFIG["interval"]
    PORT = CONFIG["port"]
    EXP_MASTER = CONFIG["exp_master"]
    SRC_MASTER = CONFIG["src_master"]
    EXP1 = CONFIG["exp1"]
    EXP2 = CONFIG["exp2"]
    EXP3 = CONFIG["exp3"]
    SRC1 = CONFIG["src1"]
    SRC2 = CONFIG["src2"]
    SRC3 = CONFIG["src3"]
    SRC4 = CONFIG["src4"]
    SRC5 = CONFIG["src5"]
    SRC6 = CONFIG["src6"]
    SRC7 = CONFIG["src7"]
    SRC8 = CONFIG["src8"]

    H2D_P = CONFIG["h2d_p"]
    H2D_S = CONFIG["h2d_s"]

    print("Loaded configurations")
    print(INTERVAL, PORT, EXP_MASTER, SRC_MASTER, EXP1, EXP2, EXP3, SRC1, SRC2, SRC3, SRC4, SRC5, SRC6, SRC7, SRC8, H2D_P, H2D_S)
    simulator = Simulator(INTERVAL, PORT, EXP_MASTER, SRC_MASTER, EXP1, EXP2, EXP3, SRC1, SRC2, SRC3, SRC4, SRC5, SRC6, SRC7, SRC8, H2D_P, H2D_S)

    while(True):
        command = input("Enter your command")
        if command.lower() == "exit":
            print("Stopping servers...")
            os._exit(0)  # Forcefully terminates all threads and sockets