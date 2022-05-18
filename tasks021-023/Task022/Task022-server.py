import socket

sock = socket.socket()
sock.bind(('192.168.43.132', 4000))
sock.listen(2)

user = [sock.accept()[0], sock.accept()[0]]
lives = [3, 3]

start, i, words = True, 0, []
while start:
    user[i].send('Your turn'.encode('UTF-8') if not words else
                 f'Your move to the letter "{words[-1]}"'.encode('UTF-8'))

    user[not i].send('We are waiting for the opponent response '.encode('UTF-8'))

    word = user[i].recv(1024).decode('UTF-8').lower()

    if word in words:
        user[i].send('You can not repeat the words '.encode('UTF-8'))
    elif words and words[-1][-1] != word[0]:
        user[i].send('Minus one life'.encode('UTF-8'))
        lives[i] -= 1
        if lives[i] == 0:
            user[not i].send('You won '.encode('UTF-8'))
            user[not i].close()
            user[i].send('You lose '.encode('UTF-8'))
            user[i].close()
            start = False
    else:
        words.append(word)
        i = not i