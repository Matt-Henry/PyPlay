import socket

conn_addr = "127.0.0.1"
conn_port = 1337

connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

connection.connect((conn_addr, conn_port))
connection.send(b"You are connected!")

info = connection.recv(1024)

print(info)

connection.close()