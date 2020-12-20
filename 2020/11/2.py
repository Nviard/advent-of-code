data = {}

row = 0

try:
    while True:
        for col, c in enumerate(input()):
            if c == "#":
                data[(row, col)] = 0
            elif c == "L":
                data[(row, col)] = 1
        row += 1
except EOFError:
    pass

col += 1

adjacents = {}
for k in data:
    adjacents[k] = []
    for d in ((-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1)):
        c = (k[0] + d[0], k[1] + d[1])
        while c[0] >= 0 and c[1] >= 0 and c[0] < row and c[1] < col:
            if c in data:
                adjacents[k].append(c)
                break
            c = (c[0] + d[0], c[1] + d[1])


def updateseats(data):
    res = {}
    for k, v in data.items():
        a = sum(((data[a] for a in adjacents[k])))
        res[k] = 1 if (v == 0 and a == 0) or ((v == 1 and a < 5)) else 0
    return res


res = data
data = None
while res != data:
    data = res
    res = updateseats(data)

print(sum(data.values()))
