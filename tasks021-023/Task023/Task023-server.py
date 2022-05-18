import os
from threading import Thread
import requests
import socket
sock = socket.socket()
sock.bind(('192.168.0.104', 50000))
sock.listen()


def load_image(client):
    name = client.recv(1024).decode('utf-8')
    client.close()
    resp = requests.get('https://www.thecocktaildb.com/api/json/v1/1/search.php', params={'s': name})
    if not os.path.isdir(name) and resp.json()['drinks'] is not None:
        os.mkdir(name)
    else:
        print('Nothing was found , you can repeat the request ')
        return 0
    for drink in resp.json()['drinks']:
        photo = requests.get(drink['strDrinkThumb']).content
        with open(f'{name}\\{drink["strDrink"]}.png', 'wb') as f:
            f.write(photo)


start = True
i = 0
while start:
    client = sock.accept()[0]
    Thread(target=load_image, args=(client,)).start()