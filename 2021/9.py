data = []
outputs = []

try:
    while True:
        data.append(list(map(int, input())))
except EOFError:
    pass

res1 = 0
res2 = 0


def neighbors(data, x, y):
    for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
        if (
            (x + dx < 0)
            or (y + dy < 0)
            or (x + dx == len(data))
            or (y + dy == len(data[x]))
        ):
            yield ((None, None))
        elif data[x + dx][y + dy] > data[x][y]:
            yield ((x + dx, y + dy))


basins = []
for x in range(len(data)):
    for y in range(len(data[x])):
        if len(list(neighbors(data, x, y))) == 4:
            res1 += data[x][y] + 1
            basins.append(set(((x, y),)))

for b in basins:
    candidates = set(b)
    while candidates:
        c = candidates.pop()
        b.add(c)
        for n in neighbors(data, *c):
            if (
                (n != (None, None))
                and (n not in candidates)
                and (n not in b)
                and (data[n[0]][n[1]] < 9)
            ):
                candidates.add(n)

basins = sorted(len(b) for b in basins)
res2 = basins[-1] * basins[-2] * basins[-3]

print(res1)
print(res2)
