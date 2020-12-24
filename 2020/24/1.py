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

print(len(black))
