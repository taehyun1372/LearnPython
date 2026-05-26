import socket

HOST = "192.168.1.104"
PORT = 9999

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))

print("서버 연결됨 (종료: exit)")

try:
    while True:
        msg = input("보낼 메시지: ")

        if msg == "exit":
            break

        client_socket.sendall(msg.encode())

        data = client_socket.recv(1024)
        print("서버 응답:", data.decode())

finally:
    client_socket.close()
    print("연결 종료")