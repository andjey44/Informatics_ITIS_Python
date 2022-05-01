# def infinite_sequence():
#     a = int(input())
#     num = 0
#     while True:
#         yield a ** num
#         num += 1


# def infinite_sequence1():
#     b = int(input())
#     while b!=0:
#         if (b%10)%2==0:
#             yield b%10
#             b=b//10
#         else:
#             b=b//10


# def infinite_sequence2():
#     N = int(input())
#     for k in range(2, N + 1):
#         prime = True
#         for i in range(2, k):
#             if k % i == 0:
#                 prime = False
#                 break
#         if prime:
#             yield k


def infinite_sequence3():
    b = int(input())
    e=list()
    z1=b
    while z1!=0:
        z=z1%10
        e.append(z)
        z1=z1//10
    for i in range(b):
        d = list()
        for c in range(2,b+1):
            if i%c==0:
                flag=True
                for c1 in range(2,c):
                    if c%c1==0:
                        flag=False
                if flag==True:
                    d.append(c)
#       print(i, d, set(d), set(e))
        if set(d)|set(e) == set(e):
            yield i


# for i in infinite_sequence():
#     print(i)
# for i in infinite_sequence1():
#     print(i)
print(list(infinite_sequence3()))
