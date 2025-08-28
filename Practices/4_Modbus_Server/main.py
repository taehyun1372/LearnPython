from pymodbus.server.sync import StartUdpServer
from pymodbus.datastore import ModbusSlaveContext, ModbusServerContext
from pymodbus.datastore import ModbusSequentialDataBlock
import logging
import threading
import time
import multiprocessing
import os

PORT = 502
SRC_MASTER_IP = "192.168.2.2"
EXP_MASTER_IP = "192.168.2.3"
SLSAVE1_IP = "192.168.2.10"
HRS_IP = "192.168.2.190"

logging.basicConfig()
log = logging.getLogger()
log.setLevel(logging.INFO)

NUM_REGISTERS = 65000

SRC_MASTER_STORE = ModbusSlaveContext(
    di=ModbusSequentialDataBlock(0, [0]*NUM_REGISTERS),
    co=ModbusSequentialDataBlock(0, [0]*NUM_REGISTERS),
    hr=ModbusSequentialDataBlock(0, [0]*NUM_REGISTERS),
    ir=ModbusSequentialDataBlock(0, [0]*NUM_REGISTERS),
)

EXP_MASTER_STORE = ModbusSlaveContext(
    di=ModbusSequentialDataBlock(0, [0]*NUM_REGISTERS),
    co=ModbusSequentialDataBlock(0, [0]*NUM_REGISTERS),
    hr=ModbusSequentialDataBlock(0, [0]*NUM_REGISTERS),
    ir=ModbusSequentialDataBlock(0, [0]*NUM_REGISTERS),
)

HRS_STORE = ModbusSlaveContext(
    di=ModbusSequentialDataBlock(0, [0]*NUM_REGISTERS),
    co=ModbusSequentialDataBlock(0, [0]*NUM_REGISTERS),
    hr=ModbusSequentialDataBlock(0, [0]*NUM_REGISTERS),
    ir=ModbusSequentialDataBlock(0, [0]*NUM_REGISTERS),
)

SLAVE1_STORE = ModbusSlaveContext(
    di=ModbusSequentialDataBlock(0, [0]*NUM_REGISTERS),
    co=ModbusSequentialDataBlock(0, [0]*NUM_REGISTERS),
    hr=ModbusSequentialDataBlock(0, [0]*NUM_REGISTERS),
    ir=ModbusSequentialDataBlock(0, [0]*NUM_REGISTERS),
)



SRC_MASTER_DEVICE = ModbusServerContext(slaves=SRC_MASTER_STORE, single=True)

EXP_MASTER_DEVICE = ModbusServerContext(slaves=EXP_MASTER_STORE, single=True)

HRS_DEVICE = ModbusServerContext(slaves=HRS_STORE, single=True)

SLAVE1_DEVICE = ModbusServerContext(slaves=SLAVE1_STORE, single=True)


def start_src_master_device():
    print(f"Starting src master server on port {PORT} with {NUM_REGISTERS} registers")
    StartUdpServer(SRC_MASTER_DEVICE, address=(SRC_MASTER_IP, PORT))

def start_exp_master_device():
    print(f"Starting src master server on port {PORT} with {NUM_REGISTERS} registers")
    StartUdpServer(EXP_MASTER_DEVICE, address=(EXP_MASTER_IP, PORT))

def start_hrs_device():
    print(f"Starting hrs server on port {PORT} with {NUM_REGISTERS} registers")
    StartUdpServer(HRS_DEVICE, address=(HRS_IP, PORT))

def start_slave1_device():
    print(f"Starting slave 1 server on port {PORT} with {NUM_REGISTERS} registers")
    StartUdpServer(SLAVE1_DEVICE, address=(SLSAVE1_IP, PORT))


def set_src_master_device():
    print("Changing source master values")
    SRC_MASTER_DEVICE[1].setValues(4, 2999, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14])
    SRC_MASTER_DEVICE[1].setValues(3, 59999, [1234, 2345, 3456, 4567])

def set_exp_master_device():
    print("Changing exposure master values")
    EXP_MASTER_DEVICE[1].setValues(4, 2999, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14])
    EXP_MASTER_DEVICE[1].setValues(3, 59999, [1234, 2345, 3456, 4567])

def set_hrs_device():
    print("Changing HRS values")
    HRS_DEVICE[1].setValues(4, 1199, [1] * 200)
    HRS_DEVICE[1].setValues(4, 1799, [1] * 200)

def set_slave1_device():
    print("Changing slave 1 values")
    SLAVE1_DEVICE[1].setValues(4, 999, [1] * 1000)

def oscillate_hrs_sensors():
    _flag = False
    while(True):
        if _flag:
            _flag = False
            anal_value = 7000
            alarm_value = 4097
            valve_cmd_value = 65
            valve_value = 65
            param_221_1 = 17095
            param_221_2 = 65405
            safety_device = 65
        else:
            _flag = True
            anal_value = 700
            alarm_value = 1
            valve_cmd_value = 1
            valve_value = 9
            param_221_1 = 14979
            param_221_2 = 4719
            safety_device = 5

        # Setting Analog Values
        HRS_DEVICE[1].setValues(4, 1399, [anal_value]*100)
        # Setting Valve Command Values
        HRS_DEVICE[1].setValues(4, 1499, [valve_cmd_value]*100)
        # Setting Digital Values
        HRS_DEVICE[1].setValues(4, 1799, [alarm_value] * 200)
        HRS_DEVICE[1].setValues(4, 1299, [alarm_value] * 1)
        # Setting Status Values
        HRS_DEVICE[1].setValues(4, 1699, [alarm_value]*100)
        # Misc
        HRS_DEVICE[1].setValues(4, 1999, [anal_value] * 100)
        # Setting Valve Values
        HRS_DEVICE[1].setValues(4, 1199, [valve_value] * 100)
        HRS_DEVICE[1].setValues(4, 1300, [valve_value] * 10)
        # Setting Safety Device Values
        HRS_DEVICE[1].setValues(4, 1269, [safety_device] * 10)
        # Setting Parameter 221
        param_221 = [param_221_1, param_221_2]
        HRS_DEVICE[1].setValues(4, 1489, param_221)




        time.sleep(10)
        
def oscillate_master_sensors():
    _flag = False
    while(True):
        if _flag:
            _flag = False
            valve_value = 65
        else:
            _flag = True
            valve_value = 9

        # Setting Valve Values
        SRC_MASTER_DEVICE[1].setValues(4, 1400, [valve_value] * 100)
        SRC_MASTER_DEVICE[1].setValues(4, 1400, [valve_value] * 100)

        SRC_MASTER_DEVICE[1].setValues(4, 1411,  [valve_value])
        EXP_MASTER_DEVICE[1].setValues(4, 1411, [valve_value])

        EXP_MASTER_DEVICE[1].setValues(4, 1700, [valve_value] * 100)
        EXP_MASTER_DEVICE[1].setValues(4, 1700, [valve_value] * 100)

        time.sleep(10)



def set_bit(value, bit_value, position):
    if (bit_value) :
        value |= 1 << position
    else:
        value &= ~(1 << position)
    return value

if __name__ == "__main__":
    set_src_master_device()
    set_exp_master_device()
    set_hrs_device()
    set_slave1_device()

    threading.Thread(target=start_src_master_device, daemon=True).start()
    threading.Thread(target=start_exp_master_device, daemon=True).start()
    threading.Thread(target=start_hrs_device, daemon=True).start()
    threading.Thread(target=start_slave1_device, daemon=True).start()

    threading.Thread(target=oscillate_hrs_sensors, daemon=True).start()

    print("🟢 Servers running... Press Ctrl+C to stop.")

    while(True):
        command = input("Enter your command")
        if command.lower() == "exit":
            print("Stopping servers...")
            os._exit(0)  # Forcefully terminates all threads and sockets






