def generator(s1):
    s = ''
    index=0
    i=0
    while True:
        if index==0:
            yield s
            index+=1
        elif index==len(s1)+1:
            index=0
            i=0
        else:
            yield s1[i]
            i+=1
            index+=1


s1 = input()
for i in generator(s1):
    print(i)