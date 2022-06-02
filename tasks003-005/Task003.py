# data = input().split()
# stack = []
# for x in data:
#     if x in '+-*':
#         z1 = stack.pop()
#         z2 = stack.pop()
#         if x == '+':
#             res = z1 + '+' + z2
#         elif x == '-':
#             res = z1 + '-' + z2
#         else:
#             res = z1 + '*' + z2
#         stack.append(res + '')
#     else:
#         stack.append(x + '')
# print(stack[0])
from pythonds.basic.stack import Stack


def postfixEval(postfixExpr):
    opStack = Stack()
    tokenList = postfixExpr.split()

    for token in tokenList:
        if token in "QAZWSXEDCRFVTGBYHNUJMIKOLP":
            opStack.push(str(token))
        else:
            op2 = opStack.pop()
            op1 = opStack.pop()
            result = ourMath(token,op1,op2)
            opStack.push(result)
    return opStack.pop()

def ourMath(op, op1, op2):
    if op == "*":
        return op1, '*', op2
    elif op == "/":
        return op1, '/', op2
    elif op == "+":
        return op1, '+', op2
    else:
        return op1, '-', op2

print(postfixEval('A B C + -'))