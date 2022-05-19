import socket
socket = socket.socket()
socket.bind(('192.168.0.104', 4000))
socket.listen(2)
client0,d0 = socket.accept()
client1, d1 = socket.accept()
user = [client0, client1]
number = 0
array = []
while True:
    message = user[number].recv(1024).decode('utf-8')
    if message == 'get':
        user[number].send(' '.join(array).encode('utf-8'))
    else:
        array.append(message)
    if number==0:
        number+=1
    else:
        number=0