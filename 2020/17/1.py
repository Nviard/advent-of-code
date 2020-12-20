import itertools

data = set()

try:
    y = 0
    while True:
        line = input()
        data.update(((x, y, 0) for x, a in enumerate(line) if a == "#"))
        y += 1
except:
    pass

for _ in range(6):
    active = set()
    inactive = set()
    for x, y, z in data:
        for dx, dy, dz in itertools.product((-1, 1, 0), repeat=3):
            cx, cy, cz = (x + dx, y + dy, z + dz)
            if (cx, cy, cz) not in active and (cx, cy, cz) not in inactive:
                neighbors = sum(
                    (
                        1
                        for nx, ny, nz in itertools.product((-1, 1, 0), repeat=3)
                        if (cx + nx, cy + ny, cz + nz) in data
                    )
                )
                if (((cx, cy, cz) in data) and (neighbors == 3 or neighbors == 4)) or (
                    ((cx, cy, cz) not in data) and (neighbors == 3)
                ):
                    active.add((cx, cy, cz))
                else:
                    inactive.add((cx, cy, cz))
    data = active

print(len(data))
