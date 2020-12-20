import itertools

data = set()

try:
    y = 0
    while True:
        line = input()
        data.update(((x, y, 0, 0) for x, a in enumerate(line) if a == "#"))
        y += 1
except:
    pass

for _ in range(6):
    active = set()
    inactive = set()
    for x, y, z, w in data:
        for dx, dy, dz, dw in itertools.product((-1, 1, 0), repeat=4):
            cx, cy, cz, cw = (x + dx, y + dy, z + dz, w + dw)
            if (cx, cy, cz, cw) not in active and (cx, cy, cz, cw) not in inactive:
                neighbors = sum(
                    (
                        1
                        for nx, ny, nz, nw in itertools.product((-1, 1, 0), repeat=4)
                        if (cx + nx, cy + ny, cz + nz, cw + nw) in data
                    )
                )
                if (
                    ((cx, cy, cz, cw) in data) and (neighbors == 3 or neighbors == 4)
                ) or (((cx, cy, cz, cw) not in data) and (neighbors == 3)):
                    active.add((cx, cy, cz, cw))
                else:
                    inactive.add((cx, cy, cz, cw))
    data = active

print(len(data))
