
class my_iter:
    def __init__(self, st,n):
        self.n, self.ind = n, -1
        s=st+st[::-1]
        self.st_new= s*(n//len(s))+ s[:n%len(s)]

    def __next__(self):
        self.ind += 1
        return self.st_new[self.ind % len(self.st_new)]

    def __iter__(self):
        return iter(self.st_new)


for i in my_iter('mythic', 20):
    print(i)


