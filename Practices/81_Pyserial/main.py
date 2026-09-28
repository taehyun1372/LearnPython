import serial

with serial.Serial(
    port='COM3', 
    baudrate=19200, 
    timeout=1) as ser:
    print(ser.name)
    ser.write(b'hello')
    
    x = ser.read()
    s = ser.read(10)
    line = ser.readline()
    
    print(x)
    print(s)
    print(line)
    ser.close()
    
    