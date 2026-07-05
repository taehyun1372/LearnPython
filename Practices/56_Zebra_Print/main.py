import socket

printer_ip = "192.168.1.111"  # 프린터 IP
printer_port = 9100

zpl = """
^XA
^FO50,50
^A0N,40,40
^FDHello Zebra!^FS
^BQN,2,2
^XZ
"""

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((printer_ip, printer_port))
    s.sendall(zpl.encode("utf-8"))

print("전송 완료")