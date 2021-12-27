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
    for dx, dy in (
        (1, 0),
        (-1, 0),
        (0, 1),
        (0, -1),
        (-1, -1),
        (1, -1),
        (-1, 1),
        (1, 1),
    ):
        if not (
            (x + dx < 0)
            or (y + dy < 0)
            or (x + dx == len(data))
            or (y + dy == len(data[x]))
        ):
            yield ((x + dx, y + dy))


step = 0

while not res2:
    flashes = set()
    for x in range(len(data)):
        for y in range(len(data[x])):
            data[x][y] += 1
            if data[x][y] == 10:
                data[x][y] = 0
                flashes.add((x, y))
    if flashes:
        current = set(flashes)
        while current:
            c = current.pop()
            flashes.add(c)
            for n in neighbors(data, *c):
                if n not in flashes and n not in current:
                    data[n[0]][n[1]] += 1
                    if data[n[0]][n[1]] == 10:
                        data[n[0]][n[1]] = 0
                        current.add(n)
    if step < 100:
        res1 += len(flashes)
    step += 1
    if len(flashes) == 100:
        res2 = step


print(res1)
print(res2)
