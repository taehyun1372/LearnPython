from pymodbus.server.sync import StartUdpServer, StartTcpServer
from pymodbus.datastore import ModbusSlaveContext, ModbusServerContext
from pymodbus.datastore import ModbusSequentialDataBlock
import logging
import threading
import time
import multiprocessing
import os
from const import *

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

EXP1_STORE = ModbusSlaveContext(
    di=ModbusSequentialDataBlock(0, [0]*NUM_REGISTERS),
    co=ModbusSequentialDataBlock(0, [0]*NUM_REGISTERS),
    hr=ModbusSequentialDataBlock(0, [0]*NUM_REGISTERS),
    ir=ModbusSequentialDataBlock(0, [0]*NUM_REGISTERS),
)

EXP2_STORE = ModbusSlaveContext(
    di=ModbusSequentialDataBlock(0, [0]*NUM_REGISTERS),
    co=ModbusSequentialDataBlock(0, [0]*NUM_REGISTERS),
    hr=ModbusSequentialDataBlock(0, [0]*NUM_REGISTERS),
    ir=ModbusSequentialDataBlock(0, [0]*NUM_REGISTERS),
)

EXP3_STORE = ModbusSlaveContext(
    di=ModbusSequentialDataBlock(0, [0]*NUM_REGISTERS),
    co=ModbusSequentialDataBlock(0, [0]*NUM_REGISTERS),
    hr=ModbusSequentialDataBlock(0, [0]*NUM_REGISTERS),
    ir=ModbusSequentialDataBlock(0, [0]*NUM_REGISTERS),
)

EXP4_STORE = ModbusSlaveContext(
    di=ModbusSequentialDataBlock(0, [0]*NUM_REGISTERS),
    co=ModbusSequentialDataBlock(0, [0]*NUM_REGISTERS),
    hr=ModbusSequentialDataBlock(0, [0]*NUM_REGISTERS),
    ir=ModbusSequentialDataBlock(0, [0]*NUM_REGISTERS),
)

SRC1_STORE = ModbusSlaveContext(
    di=ModbusSequentialDataBlock(0, [0]*NUM_REGISTERS),
    co=ModbusSequentialDataBlock(0, [0]*NUM_REGISTERS),
    hr=ModbusSequentialDataBlock(0, [0]*NUM_REGISTERS),
    ir=ModbusSequentialDataBlock(0, [0]*NUM_REGISTERS),
)

SRC2_STORE = ModbusSlaveContext(
    di=ModbusSequentialDataBlock(0, [0]*NUM_REGISTERS),
    co=ModbusSequentialDataBlock(0, [0]*NUM_REGISTERS),
    hr=ModbusSequentialDataBlock(0, [0]*NUM_REGISTERS),
    ir=ModbusSequentialDataBlock(0, [0]*NUM_REGISTERS),
)

SRC3_STORE = ModbusSlaveContext(
    di=ModbusSequentialDataBlock(0, [0]*NUM_REGISTERS),
    co=ModbusSequentialDataBlock(0, [0]*NUM_REGISTERS),
    hr=ModbusSequentialDataBlock(0, [0]*NUM_REGISTERS),
    ir=ModbusSequentialDataBlock(0, [0]*NUM_REGISTERS),
)

SRC4_STORE = ModbusSlaveContext(
    di=ModbusSequentialDataBlock(0, [0]*NUM_REGISTERS),
    co=ModbusSequentialDataBlock(0, [0]*NUM_REGISTERS),
    hr=ModbusSequentialDataBlock(0, [0]*NUM_REGISTERS),
    ir=ModbusSequentialDataBlock(0, [0]*NUM_REGISTERS),
)

SRC5_STORE = ModbusSlaveContext(
    di=ModbusSequentialDataBlock(0, [0]*NUM_REGISTERS),
    co=ModbusSequentialDataBlock(0, [0]*NUM_REGISTERS),
    hr=ModbusSequentialDataBlock(0, [0]*NUM_REGISTERS),
    ir=ModbusSequentialDataBlock(0, [0]*NUM_REGISTERS),
)

SRC6_STORE = ModbusSlaveContext(
    di=ModbusSequentialDataBlock(0, [0]*NUM_REGISTERS),
    co=ModbusSequentialDataBlock(0, [0]*NUM_REGISTERS),
    hr=ModbusSequentialDataBlock(0, [0]*NUM_REGISTERS),
    ir=ModbusSequentialDataBlock(0, [0]*NUM_REGISTERS),
)

SRC7_STORE = ModbusSlaveContext(
    di=ModbusSequentialDataBlock(0, [0]*NUM_REGISTERS),
    co=ModbusSequentialDataBlock(0, [0]*NUM_REGISTERS),
    hr=ModbusSequentialDataBlock(0, [0]*NUM_REGISTERS),
    ir=ModbusSequentialDataBlock(0, [0]*NUM_REGISTERS),
)

SRC8_STORE = ModbusSlaveContext(
    di=ModbusSequentialDataBlock(0, [0]*NUM_REGISTERS),
    co=ModbusSequentialDataBlock(0, [0]*NUM_REGISTERS),
    hr=ModbusSequentialDataBlock(0, [0]*NUM_REGISTERS),
    ir=ModbusSequentialDataBlock(0, [0]*NUM_REGISTERS),
)

SRC1_DP_STORE = ModbusSlaveContext(
    di=ModbusSequentialDataBlock(0, [0]*NUM_REGISTERS),
    co=ModbusSequentialDataBlock(0, [0]*NUM_REGISTERS),
    hr=ModbusSequentialDataBlock(0, [0]*NUM_REGISTERS),
    ir=ModbusSequentialDataBlock(0, [0]*NUM_REGISTERS),
)

SRC1_BP_STORE = ModbusSlaveContext(
    di=ModbusSequentialDataBlock(0, [0]*NUM_REGISTERS),
    co=ModbusSequentialDataBlock(0, [0]*NUM_REGISTERS),
    hr=ModbusSequentialDataBlock(0, [0]*NUM_REGISTERS),
    ir=ModbusSequentialDataBlock(0, [0]*NUM_REGISTERS),
)

EXP1_DP_STORE = ModbusSlaveContext(
    di=ModbusSequentialDataBlock(0, [0]*NUM_REGISTERS),
    co=ModbusSequentialDataBlock(0, [0]*NUM_REGISTERS),
    hr=ModbusSequentialDataBlock(0, [0]*NUM_REGISTERS),
    ir=ModbusSequentialDataBlock(0, [0]*NUM_REGISTERS),
)

EXP1_BP_STORE = ModbusSlaveContext(
    di=ModbusSequentialDataBlock(0, [0]*NUM_REGISTERS),
    co=ModbusSequentialDataBlock(0, [0]*NUM_REGISTERS),
    hr=ModbusSequentialDataBlock(0, [0]*NUM_REGISTERS),
    ir=ModbusSequentialDataBlock(0, [0]*NUM_REGISTERS),
)

RB1_DP_STORE = ModbusSlaveContext(
    di=ModbusSequentialDataBlock(0, [0]*NUM_REGISTERS),
    co=ModbusSequentialDataBlock(0, [0]*NUM_REGISTERS),
    hr=ModbusSequentialDataBlock(0, [0]*NUM_REGISTERS),
    ir=ModbusSequentialDataBlock(0, [0]*NUM_REGISTERS),
)

RB2_DP_STORE = ModbusSlaveContext(
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

EXP1_DEVICE = ModbusServerContext(slaves=EXP1_STORE, single=True)

EXP2_DEVICE = ModbusServerContext(slaves=EXP2_STORE, single=True)

EXP3_DEVICE = ModbusServerContext(slaves=EXP3_STORE, single=True)

EXP4_DEVICE = ModbusServerContext(slaves=EXP4_STORE, single=True)

SRC1_DEVICE = ModbusServerContext(slaves=SRC1_STORE, single=True)

SRC2_DEVICE = ModbusServerContext(slaves=SRC2_STORE, single=True)

SRC3_DEVICE = ModbusServerContext(slaves=SRC3_STORE, single=True)

SRC4_DEVICE = ModbusServerContext(slaves=SRC4_STORE, single=True)

SRC5_DEVICE = ModbusServerContext(slaves=SRC5_STORE, single=True)

SRC6_DEVICE = ModbusServerContext(slaves=SRC6_STORE, single=True)

SRC7_DEVICE = ModbusServerContext(slaves=SRC7_STORE, single=True)

SRC8_DEVICE = ModbusServerContext(slaves=SRC8_STORE, single=True)

SRC1_DP_DEVICE = ModbusServerContext(slaves=SRC1_DP_STORE, single=True)

SRC1_BP_DEVICE = ModbusServerContext(slaves=SRC1_BP_STORE, single=True)

EXP1_DP_DEVICE = ModbusServerContext(slaves=SRC1_DP_STORE, single=True)

EXP1_BP_DEVICE = ModbusServerContext(slaves=SRC1_BP_STORE, single=True)

RB1_DP_DEVICE = ModbusServerContext(slaves=RB1_DP_STORE, single=True)

RB2_DP_DEVICE = ModbusServerContext(slaves=RB2_DP_STORE, single=True)

def start_src_master_device():
    print(f"Starting src master server on port {PORT} with {NUM_REGISTERS} registers")
    StartUdpServer(SRC_MASTER_DEVICE, address=(SRC_MASTER_IP, PORT))

def start_exp_master_device():
    print(f"Starting exp master server on port {PORT} with {NUM_REGISTERS} registers")
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

def start_exp1_device():
    print(f"Starting exp 1 server on port {PORT} with {NUM_REGISTERS} registers")
    StartUdpServer(EXP1_DEVICE, address=(EXP1_IP, PORT))

def start_exp2_device():
    print(f"Starting exp 2 server on port {PORT} with {NUM_REGISTERS} registers")
    StartUdpServer(EXP2_DEVICE, address=(EXP2_IP, PORT))

def start_exp3_device():
    print(f"Starting exp 3 server on port {PORT} with {NUM_REGISTERS} registers")
    StartUdpServer(EXP3_DEVICE, address=(EXP3_IP, PORT))

def start_exp4_device():
    print(f"Starting exp 4 server on port {PORT} with {NUM_REGISTERS} registers")
    StartUdpServer(EXP4_DEVICE, address=(EXP4_IP, PORT))

def start_src1_device():
    print(f"Starting src 1 server on port {PORT} with {NUM_REGISTERS} registers")
    StartUdpServer(SRC1_DEVICE, address=(SRC1_IP, PORT))

def start_src2_device():
    print(f"Starting src 2 server on port {PORT} with {NUM_REGISTERS} registers")
    StartUdpServer(SRC2_DEVICE, address=(SRC2_IP, PORT))

def start_src3_device():
    print(f"Starting src 3 server on port {PORT} with {NUM_REGISTERS} registers")
    StartUdpServer(SRC3_DEVICE, address=(SRC3_IP, PORT))

def start_src4_device():
    print(f"Starting src 4 server on port {PORT} with {NUM_REGISTERS} registers")
    StartUdpServer(SRC4_DEVICE, address=(SRC4_IP, PORT))

def start_src5_device():
    print(f"Starting src 8 server on port {PORT} with {NUM_REGISTERS} registers")
    StartUdpServer(SRC5_DEVICE, address=(SRC5_IP, PORT))

def start_src6_device():
    print(f"Starting src 6 server on port {PORT} with {NUM_REGISTERS} registers")
    StartUdpServer(SRC6_DEVICE, address=(SRC6_IP, PORT))

def start_src7_device():
    print(f"Starting src 7 server on port {PORT} with {NUM_REGISTERS} registers")
    StartUdpServer(SRC7_DEVICE, address=(SRC7_IP, PORT))

def start_src8_device():
    print(f"Starting src 8 server on port {PORT} with {NUM_REGISTERS} registers")
    StartUdpServer(SRC8_DEVICE, address=(SRC8_IP, PORT))

def start_src1_dp_device():
    print(f"Starting src 1 dp server on port {PORT} with {NUM_REGISTERS} registers")
    StartTcpServer(SRC1_DP_DEVICE, address=(SRC1_DP, PORT))

def start_src1_bp_device():
    print(f"Starting src 1 bp server on port {PORT} with {NUM_REGISTERS} registers")
    StartTcpServer(SRC1_BP_DEVICE, address=(SRC1_BP, PORT))

def start_exp1_dp_device():
    print(f"Starting exp 1 dp server on port {PORT} with {NUM_REGISTERS} registers")
    StartTcpServer(EXP1_DP_DEVICE, address=(EXP1_DP, PORT))

def start_exp1_bp_device():
    print(f"Starting exp 1 bp server on port {PORT} with {NUM_REGISTERS} registers")
    StartTcpServer(EXP1_BP_DEVICE, address=(EXP1_BP, PORT))

def start_rb1_dp_device():
    print(f"Starting rb 1 dp server on port {PORT} with {NUM_REGISTERS} registers")
    StartTcpServer(RB1_DP_DEVICE, address=(RB1_DP, PORT))

def start_rb2_dp_device():
    print(f"Starting rb 2 dp server on port {PORT} with {NUM_REGISTERS} registers")
    StartTcpServer(RB2_DP_DEVICE, address=(RB2_DP, PORT))

def set_src_master_device():
    print("Changing source master values")
    SRC_MASTER_DEVICE[1].setValues(4, 1612, [4] * 1) # HRS Config Type Value: 1=HRS Dummy, 3=HRS#3, 4=HRS#4
    SRC_MASTER_DEVICE[1].setValues(4, 1713, [40] * 1)  # Test
    SRC_MASTER_DEVICE[1].setValues(4, 2999, [8650, 3, 0, 0, 0, 90, 80, 70, 60, 50, 40, 0])
    SRC_MASTER_DEVICE[1].setValues(4, 3071, [0, 0, 0, 392, 1560])
    SRC_MASTER_DEVICE[1].setValues(4, 3082, [110, 112, 278, 279, 133, 275, 276, 201, 201, 202, 201, 202, 201, 201, 87, 218, 156])

    SRC_MASTER_DEVICE[1].setValues(3, 59999, [1234, 2345, 3456, 4567])

def set_exp_master_device():
    print("Changing exposure master values")
    EXP_MASTER_DEVICE[1].setValues(4, 1713, [20] * 1)  # Test
    EXP_MASTER_DEVICE[1].setValues(4, 2999, [360, 2, 10, 20, 30, 0, 0, 0, 0, 0, 0, 150, 0, 0])
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

def set_exp1_device():
    print("Changing exp 1 values")
    EXP1_DEVICE[1].setValues(4, 999, [1] * 1000)
    EXP1_DEVICE[1].setValues(4, 1275, [0])
    EXP1_DEVICE[1].setValues(4, 2999,
                             [33207, 16385, 16385, 1707, 130, 0, 0, 0, 0, 2, 101, 102, 103, 115, 114, 101, 221, 157, 101, 101, 103, 101, 103, 410, 0, 157, 0, 1, 241, 131, 141, 0, 69, 120, 112, 49])

def set_exp2_device():
    print("Changing exp 2 values")
    EXP2_DEVICE[1].setValues(4, 999, [1] * 1000)
    EXP2_DEVICE[1].setValues(4, 1275, [0])

    # EXP2_DEVICE[1].setValues(4, 1030, [0] * 1) # UV/IR not fitted
    # EXP2_DEVICE[1].setValues(4, 1288, [4097] * 1)  # UV/IR not fitted
    #
    # EXP2_DEVICE[1].setValues(4, 1266, [1] * 1)  # Extract Fitted
    # EXP2_DEVICE[1].setValues(4, 1265, [1500] * 1)  # Extract Value
    #
    # EXP2_DEVICE[1].setValues(4, 1018, [1] * 1)  # Gas Detect Fitted
    # EXP2_DEVICE[1].setValues(4, 1069, [1] * 1)  # Gas Detect Value
    #
    # EXP2_DEVICE[1].setValues(4, 1021, [0] * 1)  # Water Detect Fitted
    # EXP2_DEVICE[1].setValues(4, 1073, [1] * 1)  # Water Detect Value

    EXP2_DEVICE[1].setValues(4, 2999,
                             [16855, 16385, 16385, 1675, 243, 0, 0, 0, 0, 0, 104, 105, 106, 104, 103, 102, 222, 155, 102, 102, 103, 101, 102, 420, 0, 155, 0, 2, 240, 132, 142, 0, 69, 120, 112, 50])

def set_exp3_device():
    print("Changing exp 3 values")
    EXP3_DEVICE[1].setValues(4, 999, [1] * 1000)
    EXP3_DEVICE[1].setValues(4, 1061, [0]) # Top pump not fitted
    EXP3_DEVICE[1].setValues(4, 1265, [600])  # Extract Pressure
    EXP3_DEVICE[1].setValues(4, 1272, [1024]) # 2RB RB1
    EXP3_DEVICE[1].setValues(4, 1275, [4])  # Top pump pipeline not fitted

    EXP3_DEVICE[1].setValues(4, 2999,
                             [33152, 16385, 16385, 10027, 243, 0, 0, 0, 0, 0, 104, 105, 106, 104, 103, 102, 222, 155, 102, 102, 103, 101, 102, 420, 0, 155, 0, 2, 240, 132, 142, 0, 82, 66, 49, 0])
    EXP3_DEVICE[1].setValues(4, 3047,
                             [82, 66, 49])

def set_exp4_device():
    print("Changing exp 4 values")
    EXP4_DEVICE[1].setValues(4, 999, [1] * 1000)
    EXP4_DEVICE[1].setValues(4, 1061, [0]) # Top pump not fitted
    EXP4_DEVICE[1].setValues(4, 1090, [900]) # FT-104 Value
    EXP4_DEVICE[1].setValues(4, 1265, [700])  # Extract Pressure
    EXP4_DEVICE[1].setValues(4, 1272, [2048])  # 2RB RB2
    EXP4_DEVICE[1].setValues(4, 1275, [4])  # Top pump pipeline not fitted

    EXP4_DEVICE[1].setValues(4, 2999,
                             [16768, 16385, 16385, 1835, 243, 0, 0, 0, 0, 0, 104, 105, 106, 104, 103, 102, 222, 155, 102, 102, 103, 101, 102, 420, 0, 155, 0, 2, 240, 132, 142, 0, 82, 66, 50, 0])
    EXP4_DEVICE[1].setValues(4, 3047,
                             [82, 66, 50])
def set_src1_device(): #IEA2B1123010_SS12
    print("Changing src 1 values")
    SRC1_DEVICE[1].setValues(4, 999, [1] * 1000)
    SRC1_DEVICE[1].setValues(4, 1275, [0])
    SRC1_DEVICE[1].setValues(4, 1090, [900]) # FT-104 Value
    SRC1_DEVICE[1].setValues(4, 1265, [800])  # Extract Pressure
    SRC1_DEVICE[1].setValues(4, 2999,
                             [16855, 16385, 16385, 1963, 130, 0, 0, 0, 0, 2, 201, 202, 203, 0, 0, 201, 231, 351, 201, 201, 103, 101, 201, 151, 0, 351, 0, 4, 251, 331, 341, 0, 83, 114, 99, 49])

def set_src2_device():
    print("Changing src 2 values")
    SRC2_DEVICE[1].setValues(4, 999, [1] * 1000)
    SRC2_DEVICE[1].setValues(4, 1275, [0])
    SRC2_DEVICE[1].setValues(4, 2999,
                             [49623, 16385, 16385, 1963, 243, 0, 0, 0, 0, 0, 301, 302, 303, 0, 0, 301, 232, 352, 301, 301, 103, 101, 301, 720, 0, 352, 0, 5, 252, 332, 342, 0, 83, 114, 99, 50])

def set_src3_device():
    print("Changing src 3 values")
    SRC3_DEVICE[1].setValues(4, 999, [1] * 1000)
    SRC3_DEVICE[1].setValues(4, 1275, [0])
    SRC3_DEVICE[1].setValues(4, 2999,
                             [49623, 16385, 16385, 1963, 243, 0, 0, 0, 0, 0, 401, 402, 403, 0, 0, 401, 2330, 353, 401, 401, 103, 101, 401, 730, 0, 353, 0, 6, 253, 333, 343, 0, 83, 114, 99, 51])

def set_src4_device():
    print("Changing src 4 values")
    SRC4_DEVICE[1].setValues(4, 999, [1] * 1000)
    SRC4_DEVICE[1].setValues(4, 1275, [0])
    SRC4_DEVICE[1].setValues(4, 2999,
                             [49623, 16385, 16385, 1963, 243, 0, 0, 0, 0, 0, 501, 502, 503, 0, 0, 501, 234, 354, 501, 501, 103, 101, 501, 740, 0, 354, 0, 7, 254, 334, 344, 0, 83, 114, 99, 52])

def set_src5_device():
    print("Changing src 5 values")
    SRC5_DEVICE[1].setValues(4, 999, [1] * 1000)
    SRC5_DEVICE[1].setValues(4, 1275, [0])
    SRC5_DEVICE[1].setValues(4, 2999,
                             [49623, 16385, 16385, 1963, 243, 0, 0, 0, 0, 0, 601, 602, 603, 0, 0, 601, 235, 355, 601, 601, 103, 101, 601, 750, 0, 355, 0, 8, 255, 335, 345, 0, 83, 114, 99, 53])

def set_src6_device():
    print("Changing src 6 values")
    SRC6_DEVICE[1].setValues(4, 999, [1] * 1000)
    SRC6_DEVICE[1].setValues(4, 1275, [0])
    SRC6_DEVICE[1].setValues(4, 2999,
                             [33238, 16385, 16385, 4011, 243, 0, 0, 0, 0, 0, 701, 702, 703, 0, 0, 701, 236, 355, 701, 701, 103, 101, 601, 760, 0, 356, 0, 9, 256, 336, 346, 0, 83, 114, 99, 54])

def set_src7_device():
    print("Changing src 7 values")
    SRC7_DEVICE[1].setValues(4, 999, [1] * 1000)

def set_src8_device():
    print("Changing src 8 values")
    SRC8_DEVICE[1].setValues(4, 999, [1] * 1000)

def set_src1_dp_device():
    print("Changing src 1 dp values")
    SRC1_DP_DEVICE[1].setValues(3, 256, [504] ) # pump status
    SRC1_DP_DEVICE[1].setValues(3, 257, [30] )  # pump DP current
    SRC1_DP_DEVICE[1].setValues(3, 258, [40] )  # pump MB current

def set_src1_bp_device():
    print("Changing src 1 bp values")
    SRC1_BP_DEVICE[1].setValues(3, 256, [504] ) # pump status
    SRC1_BP_DEVICE[1].setValues(3, 257, [30] )  # pump DP current
    SRC1_BP_DEVICE[1].setValues(3, 258, [40] )  # pump MB current

def set_exp1_dp_device():
    print("Changing exp 1 dp values")
    EXP1_DP_DEVICE[1].setValues(3, 256, [504] ) # pump status
    EXP1_DP_DEVICE[1].setValues(3, 257, [30] )  # pump DP current
    EXP1_DP_DEVICE[1].setValues(3, 258, [40] )  # pump MB current

def set_exp1_bp_device():
    print("Changing exp 1 bp values")
    EXP1_BP_DEVICE[1].setValues(3, 256, [504] ) # pump status
    EXP1_BP_DEVICE[1].setValues(3, 257, [30] )  # pump DP current
    EXP1_BP_DEVICE[1].setValues(3, 258, [40] )  # pump MB current

def set_rb1_dp_device():
    print("Changing rb 1 dp values")
    RB1_DP_DEVICE[1].setValues(3, 256, [504] ) # pump status
    RB1_DP_DEVICE[1].setValues(3, 257, [30] )  # pump DP current
    RB1_DP_DEVICE[1].setValues(3, 258, [40] )  # pump MB current

def set_rb2_dp_device():
    print("Changing rb 2 dp values")
    RB2_DP_DEVICE[1].setValues(3, 256, [504] ) # pump status
    RB2_DP_DEVICE[1].setValues(3, 257, [30] )  # pump DP current
    RB2_DP_DEVICE[1].setValues(3, 258, [40] )  # pump MB current

def oscillate_hrs_sensors():
    _flag = False
    while(True):
        if _flag:
            _flag = False
            anal_value = 7000
            alarm_value = 9
            # alarm_value = 4097
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


        time.sleep(8)

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

        time.sleep(15)

def oscillate_RSRB_sensors():
    _flag = False
    while(True):
        if _flag:
            _flag = False
            alarm_value = 2049
        else:
            _flag = True
            alarm_value = 1

        # SLAVE3_DEVICE[3].setValues(4, 999, [alarm_value] * 1000)
        EXP3_DEVICE[3].setValues(4, 1648, [alarm_value] * 1)
        time.sleep(15)

def source1_dp_simulation():
    while(True):
        pump_command = SRC1_DP_DEVICE[1].getValues(3, 512, 1)
        pump_status = SRC1_DP_DEVICE[1].getValues(3, 256, 1)

        if get_bit(pump_command[0], 0): # DP Pump run command
            pump_status[0] = set_bit(pump_status[0], True, 0)
            SRC1_DP_DEVICE[1].setValues(3, 256, [pump_status[0]])
        else:  # DP Pump stop command
            pump_status[0] = set_bit(pump_status[0], False, 0)
            SRC1_DP_DEVICE[1].setValues(3, 256, [pump_status[0]])

        if get_bit(pump_command[0], 1): # MB Pump run command
            pump_status[0] = set_bit(pump_status[0], True, 2)
            SRC1_DP_DEVICE[1].setValues(3, 256, [pump_status[0]])
        else:  # MB Pump stop command
            pump_status[0] = set_bit(pump_status[0], False, 2)
            SRC1_DP_DEVICE[1].setValues(3, 256, [pump_status[0]])

        time.sleep(1)

def source1_bp_simulation():
    while(True):
        pump_command = SRC1_BP_DEVICE[1].getValues(3, 512, 1)
        pump_status = SRC1_BP_DEVICE[1].getValues(3, 256, 1)

        if get_bit(pump_command[0], 0): # Pump run command
            pump_status[0] = set_bit(pump_status[0], True, 0)
            SRC1_BP_DEVICE[1].setValues(3, 256, [pump_status[0]])
        else:  # Pump stop command
            pump_status[0] = set_bit(pump_status[0], False, 0)
            SRC1_BP_DEVICE[1].setValues(3, 256, [pump_status[0]])

        time.sleep(1)

def exposure1_dp_simulation():
    while(True):
        pump_command = EXP1_DP_DEVICE[1].getValues(3, 512, 1)
        pump_status = EXP1_DP_DEVICE[1].getValues(3, 256, 1)

        if get_bit(pump_command[0], 0): # DP Pump run command
            pump_status[0] = set_bit(pump_status[0], True, 0)
            EXP1_DP_DEVICE[1].setValues(3, 256, [pump_status[0]])
        else:  # DP Pump stop command
            pump_status[0] = set_bit(pump_status[0], False, 0)
            EXP1_DP_DEVICE[1].setValues(3, 256, [pump_status[0]])

        if get_bit(pump_command[0], 1): # MB Pump run command
            pump_status[0] = set_bit(pump_status[0], True, 2)
            EXP1_DP_DEVICE[1].setValues(3, 256, [pump_status[0]])
        else:  # MB Pump stop command
            pump_status[0] = set_bit(pump_status[0], False, 2)
            EXP1_DP_DEVICE[1].setValues(3, 256, [pump_status[0]])

        time.sleep(1)

def exposure1_bp_simulation():
    while(True):
        pump_command = EXP1_BP_DEVICE[1].getValues(3, 512, 1)
        pump_status = EXP1_BP_DEVICE[1].getValues(3, 256, 1)

        if get_bit(pump_command[0], 0): # Pump run command
            pump_status[0] = set_bit(pump_status[0], True, 0)
            EXP1_BP_DEVICE[1].setValues(3, 256, [pump_status[0]])
        else:  # Pump stop command
            pump_status[0] = set_bit(pump_status[0], False, 0)
            EXP1_BP_DEVICE[1].setValues(3, 256, [pump_status[0]])

        time.sleep(1)

def rb1_dp_simulation():
    while(True):
        pump_command = RB1_DP_DEVICE[1].getValues(3, 512, 1)
        pump_status = RB1_DP_DEVICE[1].getValues(3, 256, 1)

        if get_bit(pump_command[0], 0): # DP Pump run command
            pump_status[0] = set_bit(pump_status[0], True, 0)
            RB1_DP_DEVICE[1].setValues(3, 256, [pump_status[0]])
        else:  # DP Pump stop command
            pump_status[0] = set_bit(pump_status[0], False, 0)
            RB1_DP_DEVICE[1].setValues(3, 256, [pump_status[0]])

        if get_bit(pump_command[0], 1): # MB Pump run command
            pump_status[0] = set_bit(pump_status[0], True, 2)
            RB1_DP_DEVICE[1].setValues(3, 256, [pump_status[0]])
        else:  # MB Pump stop command
            pump_status[0] = set_bit(pump_status[0], False, 2)
            RB1_DP_DEVICE[1].setValues(3, 256, [pump_status[0]])

        time.sleep(1)

def rb2_dp_simulation():
    while(True):
        pump_command = RB2_DP_DEVICE[1].getValues(3, 512, 1)
        pump_status = RB2_DP_DEVICE[1].getValues(3, 256, 1)

        if get_bit(pump_command[0], 0): # DP Pump run command
            pump_status[0] = set_bit(pump_status[0], True, 0)
            RB2_DP_DEVICE[1].setValues(3, 256, [pump_status[0]])
        else:  # DP Pump stop command
            pump_status[0] = set_bit(pump_status[0], False, 0)
            RB2_DP_DEVICE[1].setValues(3, 256, [pump_status[0]])

        if get_bit(pump_command[0], 1): # MB Pump run command
            pump_status[0] = set_bit(pump_status[0], True, 2)
            RB2_DP_DEVICE[1].setValues(3, 256, [pump_status[0]])
        else:  # MB Pump stop command
            pump_status[0] = set_bit(pump_status[0], False, 2)
            RB2_DP_DEVICE[1].setValues(3, 256, [pump_status[0]])

        time.sleep(1)

def set_bit(value, bit_value, position):
    if (bit_value) :
        value |= 1 << position
    else:
        value &= ~(1 << position)
    return value

def get_bit(value, position):
    return (value >> position) & 1

if __name__ == "__main__":
    set_src_master_device()
    set_exp_master_device()

    # set_hrs_device()
    # set_h2d1_device()
    # set_h2d2_device()
    # set_exp1_device()
    set_exp2_device()
    set_exp3_device()
    set_exp4_device()

    set_src1_device()
    set_src2_device()
    set_src3_device()
    set_src4_device()
    set_src5_device()
    set_src6_device()
    # set_src7_device()
    # set_src8_device()
    # set_src1_dp_device()
    # set_src1_bp_device()
    # set_exp1_dp_device()
    # set_exp1_bp_device()
    # set_rb1_dp_device()
    # set_rb2_dp_device()

    threading.Thread(target=start_src_master_device, daemon=True).start()
    threading.Thread(target=start_exp_master_device, daemon=True).start()
    # threading.Thread(target=start_hrs_device, daemon=True).start()
    # threading.Thread(target=start_h2d1_device, daemon=True).start()
    # threading.Thread(target=start_h2d2_device, daemon=True).start()

    # threading.Thread(target=start_exp1_device, daemon=True).start()
    threading.Thread(target=start_exp2_device, daemon=True).start()
    threading.Thread(target=start_exp3_device, daemon=True).start()
    threading.Thread(target=start_exp4_device, daemon=True).start()

    threading.Thread(target=start_src1_device, daemon=True).start()
    threading.Thread(target=start_src2_device, daemon=True).start()
    threading.Thread(target=start_src3_device, daemon=True).start()
    threading.Thread(target=start_src4_device, daemon=True).start()
    threading.Thread(target=start_src5_device, daemon=True).start()
    threading.Thread(target=start_src6_device, daemon=True).start()
    # threading.Thread(target=start_src7_device, daemon=True).start()
    # threading.Thread(target=start_src8_device, daemon=True).start()
    # threading.Thread(target=start_src1_dp_device, daemon=True).start()
    # threading.Thread(target=start_src1_bp_device, daemon=True).start()
    # threading.Thread(target=start_exp1_dp_device, daemon=True).start()
    # threading.Thread(target=start_exp1_bp_device, daemon=True).start()
    # threading.Thread(target=start_rb1_dp_device, daemon=True).start()
    # threading.Thread(target=start_rb2_dp_device, daemon=True).start()
    #
    # threading.Thread(target=oscillate_hrs_sensors, daemon=True).start()
    # threading.Thread(target=oscillate_RSRB_sensors, daemon=True).start()
    # threading.Thread(target=source1_dp_simulation, daemon=True).start()
    # threading.Thread(target=source1_bp_simulation, daemon=True).start()
    # threading.Thread(target=exposure1_dp_simulation, daemon=True).start()
    # threading.Thread(target=exposure1_bp_simulation, daemon=True).start()
    # threading.Thread(target=rb1_dp_simulation, daemon=True).start()
    # threading.Thread(target=rb2_dp_simulation, daemon=True).start()

    print("🟢 Servers running... Press Ctrl+C to stop.")

    while(True):
        command = input("Enter your command")
        if command.lower() == "exit":
            print("Stopping servers...")
            os._exit(0)  # Forcefully terminates all threads and sockets






