import time
import sys
import socket

HOST = "127.0.0.1"
PORT = 9998

class Process():
    def __init__(self, title, HOST, PORT):
        self.host = HOST
        self.port = PORT
        self.title = title
        self.socket = None
        self.connect()

    def connect(self):
        self.sock = socket.socket(
            socket.AF_INET,
            socket.SOCK_STREAM
        )

        self.sock.connect((self.host, self.port))

    def work(self, content, counts):
        for i in range(counts):
            message = f"[{self.title}], [{i}]th : {content}"
            print(message) 
            self.report_message(message)
            time.sleep(1)  
        self.close_connection()

    def report_message(self, message:str):
        if self.sock is not None:
            message += "\n"
            print(f"message sent : {message}")
            self.sock.sendall(message.encode("utf-8"))

    def close_connection(self):
        if self.sock is not None:
            print(f"closign connection : {self.sock}")
            self.sock.close()


if __name__ == "__main__":
    if len(sys.argv) > 1:
        process = Process(str(sys.argv[1]), HOST, PORT)
    else:
        process = Process("work", HOST, PORT)

    if len(sys.argv) > 2:
        process.work("Hello", int(sys.argv[2]))
    else:
        process.work("Hello", 5)