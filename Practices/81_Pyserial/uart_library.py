import serial
import threading

class UART:
    def __init__(self, port, baudrate, timeout):
        self.port = port
        self.baudrate = baudrate
        self.timeout = timeout
        
        self.__comms_obj = serial.Serial(
            
        )
    
    def connect(self):
        pass
    
    def disconnect(self):
        pass
    
    def send_data(self):
        pass
    
    def __sender(self):
        pass
    
    def get_data(self):
        pass
    
    def __receiver(self):
        pass
    
    