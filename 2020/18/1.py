import re

data = []
parenthesis = re.compile(r"\(([\d+* ]+)\)")

try:
    while True:
        data.append(input())
except EOFError:
    pass


def eval2(expr):
    tokens = expr.split()
    res = int(tokens[0])
    for i in range(1, len(tokens), 2):
        if tokens[i] == "*":
            res *= int(tokens[i + 1])
        elif tokens[i] == "+":
            res += int(tokens[i + 1])
    return res


def eval(expr):
    m = parenthesis.search(expr)
    while m:
        expr = expr.replace(m.group(0), str(eval2(m.group(1))))
        m = parenthesis.search(expr)
    return eval2(expr)


print(sum(map(eval, data)))
