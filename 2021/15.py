data = []

try:
    while True:
        data.append(list(map(int, input())))
except EOFError:
    pass

dest = (len(data) - 1, len(data[0]) - 1)

res1 = 0
res2 = 0


def neighbors(data, x, y):
    for dx, dy in (
        (1, 0),
        (-1, 0),
        (0, 1),
        (0, -1),
    ):
        if not (
            (x + dx < 0)
            or (y + dy < 0)
            or (x + dx == len(data))
            or (y + dy == len(data[x]))
        ):
            yield ((x + dx, y + dy))


current = [(0, 0, 0)]
paths = {(0, 0): 0}

while dest not in paths:
    current = sorted(current)
    c = current.pop(0)
    for n in neighbors(data, c[1], c[2]):
        if n not in paths:
            paths[n] = data[n[0]][n[1]] + c[0]
            current.append((data[n[0]][n[1]] + c[0], *n))

res1 = paths[dest]

print(res1)

current = [(0, 0, 0)]
paths = {(0, 0): 0}

for _ in range(4):
    for _ in range(dest[0] + 1):
        data.append([((n + 1) % 10) or 1 for n in data[-dest[0] - 1]])

for _ in range(4):
    for d in data:
        d.extend([((n + 1) % 10) or 1 for n in d[-dest[1] - 1 :]])

dest = (len(data) - 1, len(data[0]) - 1)

while dest not in paths:
    current = sorted(current)
    c = current.pop(0)
    for n in neighbors(data, c[1], c[2]):
        if n not in paths:
            paths[n] = data[n[0]][n[1]] + c[0]
            current.append((data[n[0]][n[1]] + c[0], *n))

res2 = paths[dest]

print(res2)
