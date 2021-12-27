data = []
try:
    while True:
        data.append(tuple(input()))
except EOFError:
    pass

res1 = 0
res2 = 0

e = set()
s = set()

for i, l in enumerate(data):
    for j, c in enumerate(l):
        if c == "v":
            s.add((i, j))
        elif c == ">":
            e.add((i, j))

I = i + 1
J = j + 1

E = set()
S = set()

while e != E or s != S:
    E = e
    S = s
    e = set()
    s = set()
    for a, b in E:
        i = a
        j = (b + 1) % J
        if (i, j) not in E and (i, j) not in S:
            e.add((i, j))
        else:
            e.add((a, b))
    for a, b in S:
        i = (a + 1) % I
        j = b
        if (i, j) not in e and (i, j) not in S:
            s.add((i, j))
        else:
            s.add((a, b))
    res1 += 1

print(res1)
