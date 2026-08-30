import socket
import threading

HOST = "127.0.0.1"
PORT = 9999

def start_server():
    server = socket.socket(
        socket.AF_INET,
        socket.SOCK_STREAM
    )

    server.bind((HOST, PORT))
    server.listen()

    print(f"Socket server: {HOST}:{PORT}")

    conn, addr = server.accept()
    print(f"A client connected. {conn}, {addr}")
    buffer = ""
    try:
        while True:
            data = conn.recv(4096)

            if not data:
                break

            buffer += data.decode()

            while "\n" in buffer:
                line, buffer = buffer.split("\n", 1)

                if line == "exit":
                    break

                print(f"Message received : {line}")
    finally:
        conn.close()
        print(f"Worker disconnected: {addr}")

if __name__ == "__main__":
    print("Server starts")
    start_server()