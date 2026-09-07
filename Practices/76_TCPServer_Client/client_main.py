import socket

class TCPClient:
    def __init__(self, ip_addr: str, port: int):
        self.__server = None
        self.ip_addr = ip_addr
        self.port = port
    
    def connect(self):
        try:
            print(f"Connecting to..{self.ip_addr}, {self.port}")
            self.__server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.__server.connect((self.ip_addr, self.port))
            print(f"Connected successfully")
        except Exception as e:
            print(f"Connection failed - {e}")
    
    def close(self):
        try:
            print("Closing client connection")
            self.__server.close()
        except Exception as e:
            print(f"Closing client failed - {e}")
        
if __name__ == "__main__":
    try:
        print("Starting client process")
        client = TCPClient("127.0.0.1", 9999)
        client.connect()
        while True:
            command = input("Enter a clinet command here >>")
            match command.upper():
                case "STOP":
                    raise KeyboardInterrupt
    except KeyboardInterrupt:
        print("Keyboard interrupt detected")
        client.close()
    finally:
        print("Main process finishes")
        
        