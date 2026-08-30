import socket
import subprocess
import time
from pathlib import Path
import threading

def process(message, sleep_time):
    commands = ["cmd", "/c"]
    temp = f"echo {message}"
    for i in range(sleep_time):
        timeout = "&timeout /t 1"
        temp += timeout
    commands.append(temp)
    subprocess.Popen(commands, creationflags=subprocess.CREATE_NEW_CONSOLE)

class ProcessManager():
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.conn = None
        server_th = threading.Thread(target=self.start_server)
        server_th.start()

    def start_server(self):
        server = socket.socket(
            socket.AF_INET,
            socket.SOCK_STREAM
        )

        server.bind((self.host, self.port))
        print(f"Socket server: {self.host}:{self.port}")

        server.listen()

        while True:
            conn, addr = server.accept()
            print(f"A client connected. {conn}, {addr}")
            client_handler = threading.Thread(target=self.client_handling, args=(conn,))
            client_handler.start()

    def client_handling(self, conn):
        buffer = ""
        while True:
            data = conn.recv(4096)

            if not data:
                break

            buffer += data.decode()

            while "\n" in buffer:
                line, buffer = buffer.split("\n", 1)
                if line == "exit":
                    break

                print(f"message received : {line}")

    def close_server(self):
        if self.conn is not None:
            print(f"closing server..{self.conn}")
            self.conn.close()

    def exit(self):
        self.close_server()

    def start_py(self, file_path, *args):
        commands = ["cmd", "/c"]
        parent_path = Path(__file__).resolve().parent
        path = Path.joinpath(parent_path, file_path)
        print(f"execute path : {path}")
        subprocess.Popen(
            ["python", str(path), *args],
            creationflags=subprocess.CREATE_NEW_CONSOLE
    )

if __name__ == "__main__":
    print("Main starts")

    try:
        print("Start process")
        manager = ProcessManager("127.0.0.1", 9998)
        manager.start_py("8_process.py", "work 1", "3")
        manager.start_py("8_process.py", "work 2", "5")
    finally:
        manager.exit()

    print("Main ends")