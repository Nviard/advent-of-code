data = []

try:
    while True:
        l = input()
        data.append((l[0], int(l[1:])))
except EOFError:
    pass

directions = ("S", "E", "N", "W")

pos = [0, 0]
direction = 1

for d, l in data:
    if d == "N":
        pos[0] -= l
    elif d == "S":
        pos[0] += l
    elif d == "W":
        pos[1] -= l
    elif d == "E":
        pos[1] += l
    elif d == "R":
        direction -= l // 90
        direction %= 4
    elif d == "L":
        direction += l // 90
        direction %= 4
    elif d == "F":
        if directions[direction] == "N":
            pos[0] -= l
        elif directions[direction] == "S":
            pos[0] += l
        elif directions[direction] == "W":
            pos[1] -= l
        elif directions[direction] == "E":
            pos[1] += l

print(abs(pos[0]) + abs(pos[1]))
