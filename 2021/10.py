data = []

try:
    while True:
        data.append(input())
except EOFError:
    pass

res1 = 0
res2 = []

for l in data:
    current = []
    for c in l:
        if c in ["<", "(", "[", "{"]:
            current.append(c)
        else:
            if c == ">":
                if current.pop(-1) != "<":
                    res1 += 25137
                    current = []
                    break
            elif c == ")":
                if current.pop(-1) != "(":
                    res1 += 3
                    current = []
                    break
            elif c == "]":
                if current.pop(-1) != "[":
                    res1 += 57
                    current = []
                    break
            elif c == "}":
                if current.pop(-1) != "{":
                    res1 += 1197
                    current = []
                    break
    if current:
        res2.append(0)
        while current:
            res2[-1] *= 5
            c = current.pop(-1)
            if c == "<":
                res2[-1] += 4
            elif c == "(":
                res2[-1] += 1
            elif c == "[":
                res2[-1] += 2
            elif c == "{":
                res2[-1] += 3

res2 = sorted(res2)
print(res2)
res2 = res2[int(len(res2) / 2)]

print(res1)
print(res2)
