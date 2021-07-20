import socket

listenAddr = '0.0.0.0'
listenPort = 1337

sock_serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sock_serv.bind((listenAddr, listenPort))

sock_serv.listen(10)

while True:
    conn, addr = sock_serv.accept()
    conn.send("Welcome! Who are you?")
    recvd = conn.recv(1024)
    print(recvd)


sock_serv.close()

