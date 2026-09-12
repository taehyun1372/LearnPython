import socket
import time
import threading

class TCPServer:
    def __init__(self, ip_addr: str, port: int):
        self.ip_addr = ip_addr
        self.port = port
        self.__is_initialized = False
        self.__new_client_handler_thread = None
        self.__client_handler_threads = []
        self.__client_connections = []
        self.__server = None
        self.__server_stop_event = threading.Event()
        
    @property
    def ip_addr(self) -> str:
        return self._ip_addr
        
    @ip_addr.setter
    def ip_addr(self, value: str):
        self._ip_addr = value
        
    @property
    def port(self) -> int:
        return self._port
    
    @port.setter
    def port(self, port):
        self._port = port
    
    def start_server(self):
        try:
            if not self.__is_initialized:
                self.__is_initialized = True
                self.__server_stop_event.clear()
                print("Server is being initialized")
                self.__server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                self.__server.bind((self.ip_addr, self.port))
                self.__server.listen(1)
                self.__new_client_handler_thread = threading.Thread(target=self.__new_client_handler, daemon=True)
                self.__new_client_handler_thread.start()
                print("Server initialized successfully")
            else:
                print("Server is already initialized")
        except Exception as e:
            self.__is_initialized = False
            print(f"Server initialization failed - {e}")

    def stop_server(self):
        try:
            print("Stopping sever safely")
            # Close new client handler thread
            self.__server_stop_event.set()
            if self.__new_client_handler_thread and self.__new_client_handler_thread.is_alive():
                print("Clsoing new client handler thread")
                self.__new_client_handler_thread.join()
            
            # Close client handler threads
            print("Clsoing client handler threads")
            for thread in self.__client_handler_threads:
                if thread.is_alive():
                    thread.join()
            
            # Close server socket 
            if self.__server:
                print("Closing server socket")
                self.__server.close()
            print("Stopped server successfully")
            self.__is_initialized = False
        except Exception as e:
            print(f"Stopping server failed - {e}")
    
    def get_client_request(self):
        pass
    
    def broadcase(self):
        pass
    
    def get_number_of_clients(self):
        return len(self.__client_connections)
    
    def get_connected_clients(self):
        return self.__client_connections
    
    def __new_client_handler(self):
        try:
            count = 0
            while not self.__server_stop_event.is_set():
                count += 1
                connection = self.__server.accept()
                self.__client_connections.append(connection)
                thread = threading.Thread(target=self.__client_handler, args=(connection,), daemon=True)
                thread.start()
                self.__client_handler_threads.append(thread)
                print(f"A new client is added - {connection}")
        except Exception as e:
            print(f"New client handler failed - {e}")
        finally:
            print("New client handler finished")
    
    def __client_handler(self, args):
        try:
            connection = args[0]
            while not self.__server_stop_event.is_set():
                data = connection.recv(64)
                if not data:
                    break
                
                message = data.decode("utf-8")
                print(f"Received data from client - {message}")
        except Exception as e:
            print(f"Client handler failed - {e}")
        finally:
            connection.close()
            print("Client handler finished")
    
if __name__ == "__main__":
    try:
        print("Starting server process")
        server = TCPServer("127.0.0.1", 9999)
        server.stop_server()
        server.start_server()
        server.start_server()
        server.get_number_of_clients()
        server.get_connected_clients()
        count = 0
        while True:
            count += 1
            print(f"Process is running successfully")
            command = input("Enter a server command to send >>")
            match command.upper():
                case "STOP":
                    print("Stop command detected. Finishing main process")
                    raise KeyboardInterrupt
    except KeyboardInterrupt:
        print("Keyboard interruption happened. Closng the server")
        server.stop_server()
    finally:
        print("Main process finished")