from multiprocessing import Queue
import serial
import threading
import time

class UART:
    def __init__(self, port, baudrate, timeout):
        self.port = port
        self.baudrate = baudrate
        self.timeout = timeout
        self.__comms_obj = None
        self.__send_th = None
        self.__recv_th = None
        self.__send_queue = Queue()
        self.__recv_queue = Queue()
        self.__comms_lock = threading.Lock()
        self.__stop_event = threading.Event()
    
    def connect(self):
        try:
            if self.__comms_obj:
                raise Exception("Connection already exists!")

            # Initializing pyserial obj 
            self.__comms_obj = serial.Serial(
            baudrate=self.baudrate,
            port=self.port,
            timeout=self.timeout
            )

            # Starting worker threads
            if self.__send_th or self.__recv_th:
                raise Exception("Thread already exists!")
            self.__send_th = threading.Thread(target=self.__sender)
            self.__recv_th = threading.Thread(target=self.__receiver)
            self.__stop_event.clear()
            self.__send_th.start()
            self.__recv_th.start()
            print("Connected successfully")
        except Exception as e:
            print("Connection failed! ", e)
    
    def disconnect(self):
        try:
            if not self.__comms_obj:
                raise Exception("Connection already closed!")
            
            # Closing the communication port
            self.__comms_obj.close()

            # Stopping the threads
            if not self.__recv_th or not self.__send_th:
                raise Exception("Thread already stopped!")
            self.__stop_event.set()
            for th in [self.__recv_th, self.__send_th]:
                th.join()
            print("Disconnected successfully")
        except Exception as e:
            print("Failed to disconnect! ", e)
        else:
            self.__comms_obj = None
            self.__send_th = None
            self.__recv_th = None
    
    def send_data(self):
        pass
    
    def __sender(self):
        while True:
            if self.__stop_event.is_set():
                break

            # TODO Actually send something here
            print("Sender thread is running") 
            time.sleep(1)
    
    def get_data(self):
        pass
    
    def __receiver(self):
        while True:
            if self.__stop_event.is_set():
                break

            # TODO Actually receive something here
            print("Receiver thread is running") 
            time.sleep(1)

if __name__ == "__main__":
    print("Something")
    try:
        uart = UART(
            port = "COM3",
            baudrate=19200,
            timeout=1
        )
        
        while True:
            command = input("Enter a command..")
            if command.upper() == "CONNECT":
                uart.connect()
            elif command.upper() == "DISCONNECT":
                uart.disconnect()

        uart.disconnect()
    except Exception as e:
        print("Application safe net. Disconnecting everything ", e)
        uart.disconnect()