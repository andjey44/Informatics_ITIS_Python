import asyncio
a=input().split()
d=0
z=0
for i in range(len(a)):
    if d==0:
        d=a[i]
    else:
        z=a[i]
async def f1():
    d1 = int(d)
    while d1>-1:
        if d1 > 0:
            d1 -= 1
            await asyncio.sleep(0.1)
            print('Игрок0 ударил Игрок1')
        else:
            d1-=1
            print('Игрок1 проиграл, у него осталось 0 жизней')
            break

async def f2():
    z1 = int(z)
    while z1>0:
        if z1 > 1:
            z1-=1
            await asyncio.sleep(0.1)
            print('Игрок1 ударил Игрок0')
        else:
            print(f'Игрок0 победил, у него осталось {z1} жизней')
            break

async def main():
    await asyncio.gather(f1(), f2())


if __name__ == '__main__':
    asyncio.run(main())

