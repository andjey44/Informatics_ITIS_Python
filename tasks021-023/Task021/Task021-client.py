import socket
sock = socket.socket()
sock.connect(('192.168.0.104', 50000))

while True:
    message = sock.recv(1024)
    print(message.decode('utf-8'))
    sock.send(input().encode('utf-8'))