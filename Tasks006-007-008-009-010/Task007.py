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
    while b!=0:
        prime = True
        for i in range(2, b%10):
            if b%10 % i == 0:
                prime = False
                break
        if prime:
            yield b%10
        b=b//10


# for i in infinite_sequence():
#     print(i)
# for i in infinite_sequence1():
#     print(i)
for i in infinite_sequence3():
    print(i)
