import functools
n=int(input())
print (functools.reduce(lambda x,y:x*y+1,range(1,n+1)))
print(functools.reduce(lambda x,y:x*y,[i for i in  range(1,n+1) if i%3==0] ))