import socket

word = input('Введите слово, которое будут отгадывать: ')

sock = socket.socket()
sock.bind(('192.168.0.104', 50000))
sock.listen(1)
user, _ = sock.accept()
user_word = '_' * len(word)
all = []
err = 0
user.send(user_word.encode('utf-8'))
Gallows = True
while Gallows:
    c = user.recv(1024).decode('utf-8').lower()
    if len(c) != 1 or ord('a') >= ord(c) >= ord('z'):
        user.send('Нужно отправить одну букву английского алфавита'.encode('utf-8'))
        continue
    if c in all:
        user.send('Эта буква уже была названа'.encode('utf-8'))
        continue
    all.append(c)
    if c not in word:
        err += 1
        vsc = '|--|  \n' \
              '|     \n' \
              '|     \n' \
              '|     '
        if err >= 2:
            vsc = vsc[:10] + 'o' + vsc[11:]
        if err >= 3:
            vsc = vsc[:17] + '|' + vsc[18:]
        if err >= 4:
            vsc = vsc[:16] + '/' + vsc[17:]
            vsc = vsc[:18] + '\\' + vsc[19:]
        if err >= 5:
            vsc = vsc[:23] + '/' + vsc[24:]
            vsc = vsc[:25] + '\\' + vsc[26:]
        if err == 6:
            vsc = 'Ты проиграл лох, извините:)'
            game = False
        user.send(vsc.encode('utf-8'))
        continue
    else:
        user_word = ''
        for c in word:
            user_word += c if c in all else '_'

    if user_word == word:
        user.send('Ты выиграл!'.encode('utf-8'))
        game = False
    else:
        user.send(user_word.encode('utf-8'))