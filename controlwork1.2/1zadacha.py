from functools import reduce
a = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def con(s1, s2):
    return str(s1) + str(s2)


foo = lambda x: reduce(con, x)
print(foo(a))


def app(x, e):
    if type(x) is int:
        x = [x, e]
    else:
        x.append(e)
    return x


foo1 = lambda st: reduce(app, filter(lambda n: n % 3 == 0, list(map(int, st))))
print(foo1(foo(a)))