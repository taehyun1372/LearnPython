import socket

HOST = "127.0.0.1"
PORT = 9999

def send_message(sock, message):
    sock.sendall(message.encode("utf-8"))
    print(f"Sent message : {message}")

if __name__ == "__main__":
    print("Try connection")

    sock = socket.socket(
        socket.AF_INET,
        socket.SOCK_STREAM
    )

    sock.connect((HOST, PORT))

    try:
        while True:
            message = input("Enter a message to send>>")
            message += "\n"
            send_message(sock, message)
            if message == "exit\n":
                break
    finally:
        print(f"Closing the connection {sock}")
        sock.close()