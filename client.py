import socket

HOST = "127.0.0.1"
PORT = 8835

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST,PORT))
    s.sendall("Hello World".encode())

    data = s.recv(1024)
    print("received data:",data.decode())


