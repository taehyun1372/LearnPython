from pymodbus.server import StartTcpServer
from pymodbus.datastore import ModbusServerContext, ModbusSequentialDataBlock, ModbusDeviceContext

store = ModbusDeviceContext(
    di=ModbusSequentialDataBlock(0, [0]*100),
    co=ModbusSequentialDataBlock(0, [0]*100),
    hr=ModbusSequentialDataBlock(0, [0]*100),
    ir=ModbusSequentialDataBlock(0, [0]*100),
)

context = ModbusServerContext(devices=store, single=True)

StartTcpServer(
    context=context,
    address=("0.0.0.0", 5020)
)