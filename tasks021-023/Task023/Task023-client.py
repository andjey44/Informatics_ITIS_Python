import socket
sock = socket.socket()
sock.connect(('192.168.0.104', 50000))
sock.send(input('Your request: ').encode('utf-8'))
sock.close()