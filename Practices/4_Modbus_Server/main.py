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
SLAVE1_IP = "192.168.2.10"
SLAVE2_IP = "192.168.2.20"
SLAVE3_IP = "192.168.2.30"
SLAVE4_IP = "192.168.2.40"
SLAVE5_IP = "192.168.2.50"
SLAVE6_IP = "192.168.2.60"
SLAVE7_IP = "192.168.2.70"
SLAVE8_IP = "192.168.2.80"
SLAVE9_IP = "192.168.2.90"
SLAVE10_IP = "192.168.2.100"
SLAVE11_IP = "192.168.2.110"


HRS_IP = "192.168.2.190"
H2D1_IP = "192.168.2.220"
H2D2_IP = "192.168.2.223"

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

H2D1_STORE = ModbusSlaveContext(
    di=ModbusSequentialDataBlock(0, [0]*NUM_REGISTERS),
    co=ModbusSequentialDataBlock(0, [0]*NUM_REGISTERS),
    hr=ModbusSequentialDataBlock(0, [0]*NUM_REGISTERS),
    ir=ModbusSequentialDataBlock(0, [0]*NUM_REGISTERS),
)

H2D2_STORE = ModbusSlaveContext(
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

SLAVE2_STORE = ModbusSlaveContext(
    di=ModbusSequentialDataBlock(0, [0]*NUM_REGISTERS),
    co=ModbusSequentialDataBlock(0, [0]*NUM_REGISTERS),
    hr=ModbusSequentialDataBlock(0, [0]*NUM_REGISTERS),
    ir=ModbusSequentialDataBlock(0, [0]*NUM_REGISTERS),
)

SLAVE3_STORE = ModbusSlaveContext(
    di=ModbusSequentialDataBlock(0, [0]*NUM_REGISTERS),
    co=ModbusSequentialDataBlock(0, [0]*NUM_REGISTERS),
    hr=ModbusSequentialDataBlock(0, [0]*NUM_REGISTERS),
    ir=ModbusSequentialDataBlock(0, [0]*NUM_REGISTERS),
)

SLAVE4_STORE = ModbusSlaveContext(
    di=ModbusSequentialDataBlock(0, [0]*NUM_REGISTERS),
    co=ModbusSequentialDataBlock(0, [0]*NUM_REGISTERS),
    hr=ModbusSequentialDataBlock(0, [0]*NUM_REGISTERS),
    ir=ModbusSequentialDataBlock(0, [0]*NUM_REGISTERS),
)

SLAVE5_STORE = ModbusSlaveContext(
    di=ModbusSequentialDataBlock(0, [0]*NUM_REGISTERS),
    co=ModbusSequentialDataBlock(0, [0]*NUM_REGISTERS),
    hr=ModbusSequentialDataBlock(0, [0]*NUM_REGISTERS),
    ir=ModbusSequentialDataBlock(0, [0]*NUM_REGISTERS),
)

SLAVE6_STORE = ModbusSlaveContext(
    di=ModbusSequentialDataBlock(0, [0]*NUM_REGISTERS),
    co=ModbusSequentialDataBlock(0, [0]*NUM_REGISTERS),
    hr=ModbusSequentialDataBlock(0, [0]*NUM_REGISTERS),
    ir=ModbusSequentialDataBlock(0, [0]*NUM_REGISTERS),
)

SLAVE7_STORE = ModbusSlaveContext(
    di=ModbusSequentialDataBlock(0, [0]*NUM_REGISTERS),
    co=ModbusSequentialDataBlock(0, [0]*NUM_REGISTERS),
    hr=ModbusSequentialDataBlock(0, [0]*NUM_REGISTERS),
    ir=ModbusSequentialDataBlock(0, [0]*NUM_REGISTERS),
)

SLAVE8_STORE = ModbusSlaveContext(
    di=ModbusSequentialDataBlock(0, [0]*NUM_REGISTERS),
    co=ModbusSequentialDataBlock(0, [0]*NUM_REGISTERS),
    hr=ModbusSequentialDataBlock(0, [0]*NUM_REGISTERS),
    ir=ModbusSequentialDataBlock(0, [0]*NUM_REGISTERS),
)

SLAVE9_STORE = ModbusSlaveContext(
    di=ModbusSequentialDataBlock(0, [0]*NUM_REGISTERS),
    co=ModbusSequentialDataBlock(0, [0]*NUM_REGISTERS),
    hr=ModbusSequentialDataBlock(0, [0]*NUM_REGISTERS),
    ir=ModbusSequentialDataBlock(0, [0]*NUM_REGISTERS),
)

SLAVE10_STORE = ModbusSlaveContext(
    di=ModbusSequentialDataBlock(0, [0]*NUM_REGISTERS),
    co=ModbusSequentialDataBlock(0, [0]*NUM_REGISTERS),
    hr=ModbusSequentialDataBlock(0, [0]*NUM_REGISTERS),
    ir=ModbusSequentialDataBlock(0, [0]*NUM_REGISTERS),
)

SLAVE11_STORE = ModbusSlaveContext(
    di=ModbusSequentialDataBlock(0, [0]*NUM_REGISTERS),
    co=ModbusSequentialDataBlock(0, [0]*NUM_REGISTERS),
    hr=ModbusSequentialDataBlock(0, [0]*NUM_REGISTERS),
    ir=ModbusSequentialDataBlock(0, [0]*NUM_REGISTERS),
)


SRC_MASTER_DEVICE = ModbusServerContext(slaves=SRC_MASTER_STORE, single=True)

EXP_MASTER_DEVICE = ModbusServerContext(slaves=EXP_MASTER_STORE, single=True)

HRS_DEVICE = ModbusServerContext(slaves=HRS_STORE, single=True)

H2D1_DEVICE = ModbusServerContext(slaves=H2D1_STORE, single=True)

H2D2_DEVICE = ModbusServerContext(slaves=H2D2_STORE, single=True)

SLAVE1_DEVICE = ModbusServerContext(slaves=SLAVE1_STORE, single=True)

SLAVE2_DEVICE = ModbusServerContext(slaves=SLAVE2_STORE, single=True)

SLAVE3_DEVICE = ModbusServerContext(slaves=SLAVE3_STORE, single=True)

SLAVE4_DEVICE = ModbusServerContext(slaves=SLAVE4_STORE, single=True)

SLAVE5_DEVICE = ModbusServerContext(slaves=SLAVE5_STORE, single=True)

SLAVE6_DEVICE = ModbusServerContext(slaves=SLAVE6_STORE, single=True)

SLAVE7_DEVICE = ModbusServerContext(slaves=SLAVE7_STORE, single=True)

SLAVE8_DEVICE = ModbusServerContext(slaves=SLAVE8_STORE, single=True)

SLAVE9_DEVICE = ModbusServerContext(slaves=SLAVE9_STORE, single=True)

SLAVE10_DEVICE = ModbusServerContext(slaves=SLAVE10_STORE, single=True)

SLAVE11_DEVICE = ModbusServerContext(slaves=SLAVE11_STORE, single=True)


def start_src_master_device():
    print(f"Starting src master server on port {PORT} with {NUM_REGISTERS} registers")
    StartUdpServer(SRC_MASTER_DEVICE, address=(SRC_MASTER_IP, PORT))

def start_exp_master_device():
    print(f"Starting src master server on port {PORT} with {NUM_REGISTERS} registers")
    StartUdpServer(EXP_MASTER_DEVICE, address=(EXP_MASTER_IP, PORT))

def start_hrs_device():
    print(f"Starting hrs server on port {PORT} with {NUM_REGISTERS} registers")
    StartUdpServer(HRS_DEVICE, address=(HRS_IP, PORT))

def start_h2d1_device():
    print(f"Starting h2d1 server on port {PORT} with {NUM_REGISTERS} registers")
    StartUdpServer(H2D1_DEVICE, address=(H2D1_IP, PORT))

def start_h2d2_device():
    print(f"Starting h2d2 server on port {PORT} with {NUM_REGISTERS} registers")
    StartUdpServer(H2D2_DEVICE, address=(H2D2_IP, PORT))

def start_slave1_device():
    print(f"Starting slave 1 server on port {PORT} with {NUM_REGISTERS} registers")
    StartUdpServer(SLAVE1_DEVICE, address=(SLAVE1_IP, PORT))

def start_slave2_device():
    print(f"Starting slave 2 server on port {PORT} with {NUM_REGISTERS} registers")
    StartUdpServer(SLAVE2_DEVICE, address=(SLAVE2_IP, PORT))

def start_slave3_device():
    print(f"Starting slave 3 server on port {PORT} with {NUM_REGISTERS} registers")
    StartUdpServer(SLAVE3_DEVICE, address=(SLAVE3_IP, PORT))

def start_slave4_device():
    print(f"Starting slave 4 server on port {PORT} with {NUM_REGISTERS} registers")
    StartUdpServer(SLAVE4_DEVICE, address=(SLAVE4_IP, PORT))

def start_slave5_device():
    print(f"Starting slave 5 server on port {PORT} with {NUM_REGISTERS} registers")
    StartUdpServer(SLAVE5_DEVICE, address=(SLAVE5_IP, PORT))

def start_slave6_device():
    print(f"Starting slave 6 server on port {PORT} with {NUM_REGISTERS} registers")
    StartUdpServer(SLAVE6_DEVICE, address=(SLAVE6_IP, PORT))

def start_slave7_device():
    print(f"Starting slave 2 server on port {PORT} with {NUM_REGISTERS} registers")
    StartUdpServer(SLAVE7_DEVICE, address=(SLAVE7_IP, PORT))

def start_slave8_device():
    print(f"Starting slave 8 server on port {PORT} with {NUM_REGISTERS} registers")
    StartUdpServer(SLAVE8_DEVICE, address=(SLAVE8_IP, PORT))

def start_slave9_device():
    print(f"Starting slave 2 server on port {PORT} with {NUM_REGISTERS} registers")
    StartUdpServer(SLAVE9_DEVICE, address=(SLAVE9_IP, PORT))

def start_slave10_device():
    print(f"Starting slave 10 server on port {PORT} with {NUM_REGISTERS} registers")
    StartUdpServer(SLAVE10_DEVICE, address=(SLAVE10_IP, PORT))

def start_slave11_device():
    print(f"Starting slave 11 server on port {PORT} with {NUM_REGISTERS} registers")
    StartUdpServer(SLAVE11_DEVICE, address=(SLAVE11_IP, PORT))


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

def set_h2d1_device():
    print("Changing h2d 1 values")
    H2D1_DEVICE[1].setValues(4, 999, [1] * 1000)

def set_h2d2_device():
    print("Changing h2d 2 values")
    H2D2_DEVICE[1].setValues(4, 999, [1] * 1000)

def set_slave1_device():
    print("Changing slave 1 values")
    SLAVE1_DEVICE[1].setValues(4, 999, [1] * 1000)

def set_slave2_device():
    print("Changing slave 2 values")
    SLAVE2_DEVICE[1].setValues(4, 999, [1] * 1000)

def set_slave3_device():
    print("Changing slave 3 values")
    SLAVE3_DEVICE[1].setValues(4, 999, [1] * 1000)

def set_slave4_device():
    print("Changing slave 4 values")
    SLAVE4_DEVICE[1].setValues(4, 999, [1] * 1000)

def set_slave5_device():
    print("Changing slave 5 values")
    SLAVE5_DEVICE[1].setValues(4, 999, [1] * 1000)

def set_slave6_device():
    print("Changing slave 6 values")
    SLAVE6_DEVICE[1].setValues(4, 999, [1] * 1000)

def set_slave7_device():
    print("Changing slave 7 values")
    SLAVE7_DEVICE[1].setValues(4, 999, [1] * 1000)

def set_slave8_device():
    print("Changing slave 8 values")
    SLAVE8_DEVICE[1].setValues(4, 999, [1] * 1000)

def set_slave9_device():
    print("Changing slave 9 values")
    SLAVE9_DEVICE[1].setValues(4, 999, [1] * 1000)

def set_slave10_device():
    print("Changing slave 10 values")
    SLAVE10_DEVICE[1].setValues(4, 999, [1] * 1000)

def set_slave11_device():
    print("Changing slave 11 values")
    SLAVE11_DEVICE[1].setValues(4, 999, [1] * 1000)

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
    set_h2d1_device()
    set_h2d2_device()
    set_slave1_device()
    set_slave2_device()
    set_slave3_device()
    set_slave4_device()
    set_slave5_device()
    set_slave6_device()
    set_slave7_device()
    set_slave8_device()
    set_slave9_device()
    set_slave10_device()
    set_slave11_device()

    threading.Thread(target=start_src_master_device, daemon=True).start()
    threading.Thread(target=start_exp_master_device, daemon=True).start()
    threading.Thread(target=start_hrs_device, daemon=True).start()
    threading.Thread(target=start_h2d1_device, daemon=True).start()
    threading.Thread(target=start_h2d2_device, daemon=True).start()

    threading.Thread(target=start_slave1_device, daemon=True).start()
    threading.Thread(target=start_slave2_device, daemon=True).start()
    threading.Thread(target=start_slave3_device, daemon=True).start()
    threading.Thread(target=start_slave4_device, daemon=True).start()
    threading.Thread(target=start_slave5_device, daemon=True).start()
    threading.Thread(target=start_slave6_device, daemon=True).start()
    threading.Thread(target=start_slave7_device, daemon=True).start()
    threading.Thread(target=start_slave8_device, daemon=True).start()
    threading.Thread(target=start_slave9_device, daemon=True).start()
    threading.Thread(target=start_slave10_device, daemon=True).start()
    threading.Thread(target=start_slave11_device, daemon=True).start()

    threading.Thread(target=oscillate_hrs_sensors, daemon=True).start()

    print("🟢 Servers running... Press Ctrl+C to stop.")

    while(True):
        command = input("Enter your command")
        if command.lower() == "exit":
            print("Stopping servers...")
            os._exit(0)  # Forcefully terminates all threads and sockets






