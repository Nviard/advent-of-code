data = []

try:
    while True:
        data.append(input())
except EOFError:
    pass

black = set()

for d in data:
    pos = [0, 0]
    while d:
        if d.startswith("e"):
            pos[1] += 1
            d = d[1:]
        elif d.startswith("w"):
            pos[1] -= 1
            d = d[1:]
        elif d.startswith("ne"):
            pos[1] += 0.5
            pos[0] -= 1
            d = d[2:]
        elif d.startswith("nw"):
            pos[1] -= 0.5
            pos[0] -= 1
            d = d[2:]
        elif d.startswith("se"):
            pos[1] += 0.5
            pos[0] += 1
            d = d[2:]
        elif d.startswith("sw"):
            pos[1] -= 0.5
            pos[0] += 1
            d = d[2:]

    pos = tuple(pos)

    if pos in black:
        black.remove(pos)
    else:
        black.add(pos)


for _ in range(100):
    white = set()
    orange = set()
    for b in black:
        for d in ((0, 0), (0, -1), (0, 1), (1, -0.5), (1, 0.5), (-1, -0.5), (-1, 0.5)):
            c = (b[0] + d[0], b[1] + d[1])
            if c not in white and c not in orange:
                a = sum(
                    (
                        1
                        for e in (
                            (0, -1),
                            (0, 1),
                            (1, -0.5),
                            (1, 0.5),
                            (-1, -0.5),
                            (-1, 0.5),
                        )
                        if (c[0] + e[0], c[1] + e[1]) in black
                    )
                )
                if (c in black and a in [1, 2]) or (c not in black and a == 2):
                    orange.add(c)
                else:
                    white.add(c)

    black = orange
print(len(black))
