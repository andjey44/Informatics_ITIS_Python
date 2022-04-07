def generator(s1, s2):
    c=0
    i=0
    while True:
        yield s1[i%len(s1)]
        yield s2[i%len(s2)]
        i+=1


s1 = input()
s2 = input()
for i in generator(s1, s2):
    print(i)
