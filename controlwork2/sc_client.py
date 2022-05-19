import socket
socket = socket.socket()
socket.connect(('192.168.0.104', 4000))
while True:
    s = input()
    socket.send(s.encode('utf-8'))
    if s == 'get':
        print(socket.recv(1024).decode('utf-8'))