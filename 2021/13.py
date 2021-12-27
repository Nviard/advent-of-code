data = set()
folds = []

try:
    while l := input():
        data.add(tuple(map(int, l.split(","))))
    while l := input():
        i, n = l.split("=")
        folds.append((i[-1], int(n)))
except EOFError:
    pass

res1 = 0
res2 = []

f = folds.pop(0)
current = set()
if f[0] == "x":
    for d in data:
        if d[0] > f[1]:
            current.add((f[1] * 2 - d[0], d[1]))
        else:
            current.add((d[0], d[1]))
else:
    for d in data:
        if d[1] > f[1]:
            current.add((d[0], f[1] * 2 - d[1]))
        else:
            current.add((d[0], d[1]))
data = current

res1 = len(current)

while folds:
    f = folds.pop(0)
    current = set()
    if f[0] == "x":
        for d in data:
            if d[0] > f[1]:
                current.add((f[1] * 2 - d[0], d[1]))
            else:
                current.add((d[0], d[1]))
    else:
        for d in data:
            if d[1] > f[1]:
                current.add((d[0], f[1] * 2 - d[1]))
            else:
                current.add((d[0], d[1]))
    data = current

res2 = (max(x for x, y in data) + 1, max(y for x, y in data) + 1)

print(res1)

for y in range(res2[1]):
    for x in range(res2[0]):
        print("#" if (x, y) in data else " ", end="")
    print("")
