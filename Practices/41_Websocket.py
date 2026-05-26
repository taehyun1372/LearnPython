import socket

HOST = "192.168.1.104"  # 모든 IP에서 접속 허용
PORT = 9999

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen()

print(f"서버 시작: {HOST}:{PORT}")

conn, addr = server_socket.accept()
print(f"클라이언트 접속: {addr}")

while True:
    data = conn.recv(1024)
    if not data:
        break

    print(f"받은 데이터: {data.decode()}")

    # echo
    conn.sendall(data)

conn.close()
server_socket.close()