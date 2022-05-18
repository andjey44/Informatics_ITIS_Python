import socket
sock = socket.socket()
sock.connect(('192.168.0.104', 4000))
start = True

while start:
    message = ''
    while 'Your turn ' not in message and 'The game is over ' not in message:
        msg = sock.recv(1024).decode('UTF-8')
        print('server: ' + msg)
    if 'Your turn' in message:
        sock.send(input('I: ').encode('UTF-8'))
    else:
        sock.close()
        start = False