def INFO(z):
    if z in ['×', '*', '/']:
        return 2
    elif z in ['+', '-']:
        return 1


def Check(expr):
    stack = []
    post = []
    for z in expr:
        if z not in ['×', '*', '/', '+', '-', '(', ')']:
            post.append(z)
        else:
            if z != ')' and (not stack or z == '(' or stack[-1] == '('
                             or INFO(z) > INFO(stack[-1])):
                stack.append(z)
            elif z == ')':
                while True:
                    x = stack.pop()
                    if x != '(':
                        post.append(x)
                    else:
                        break
            else:
                while True:
                    if stack and stack[-1] != '(' and INFO(z) <= INFO(stack[-1]):
                        post.append(stack.pop())
                    else:
                        stack.append(z)
                        break
    while stack:
        post.append(stack.pop())
    return post
if __name__ == '__main__':
    s = input()
    post = Check(s)
    print(post)