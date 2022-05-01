data = input().split()
stack = []
for x in data:
    if x in '+-*':
        z1 = stack.pop()
        z2 = stack.pop()
        if x == '+':
            res = z1 + '+' + z2
        elif x == '-':
            res = z1 + '-' + z2
        else:
            res = z1 + '*' + z2
        stack.append(res + '')
    else:
        stack.append(x + '')
print(stack[0])