import requests
n = int(input())
resperence = requests.get(f'https://picsum.photos/v2/list?limit={n * 3}').json()
large = sorted(resperence, reverse=True, key=lambda size: size['width'] * size['height'])[:n]
with open('fr/fr.txt', 'w') as f:
    f.write(str([(data['id'], data['author']) for data in large]))
for picture in large:
    photo = requests.get(f'https://picsum.photos/id/{picture["id"]}/{picture["width"]}/{picture["height"]}')
    with open(f'fr/photo{picture["id"]}.jpg', 'wb') as f:
        f.write(photo.content)