from pymodbus.client.sync import ModbusUdpClient

# # Connect
# client = ModbusUdpClient(SRC1_IP, port=PORT)
#
# # Connect
# client.connect()
# print("PLC connected")
# # Writing simulation data
# client.write_register(SIMULATION_OFFSET + 0, SIMULATION_PASSWORD_H)
# client.write_register(SIMULATION_OFFSET + 59, SIMULATION_PASSWORD_L)
#
# print("Enabling simulation mode")
#
# client.close()

def set_register_bit(client, word, bit):
    rr = client.read_holding_registers(word, 1)
    if rr.isError():
        return False
    value = rr.registers[0]
    value |= (1 << bit)
    print(f"Setting {client.host} holding register {word} address {bit} bit")
    client.write_register(word, value)
    return True

def reset_register_bit(client, word, bit):
    rr = client.read_holding_registers(word, 1)
    if rr.isError():
        return False
    value = rr.registers[0]
    value &= ~(1 << bit)
    print(f"Resetting {client.host} holding register {word} address {bit} bit")
    client.write_register(word, value)
    return True

def read_register(client, word):
    rr = client.read_holding_registers(word, 1)
    if rr.isError():
        return False
    value = rr.registers[0]
    print(f"Reading {client.host} holding register {word} address")
    return value

def write_register(client, word, value):
    client.write_register(word, value)
    print(f"Writing {client.host} holding register {word} address")
    return True

def read_register_bit(client, word, bit):
    rr = client.read_holding_registers(word, 1)
    if rr.isError():
        return False
    value = rr.registers[0]
    bit_state  = (value >> bit) & 1
    return bit_state

def set_bit(value, bit_value, position):
    if (bit_value) :
        value |= 1 << position
    else:
        value &= ~(1 << position)
    return value

def get_bit(value, position):
    return (value >> position) & 1