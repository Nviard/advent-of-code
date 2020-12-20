data = []

try:
    while True:
        l = input()
        data.append((l[0], int(l[1:])))
except EOFError:
    pass

directions = ("S", "E", "N", "W")

pos = [0, 0]
waypoint = [-1, 10]
direction = 1

for d, l in data:
    if d == "N":
        waypoint[0] -= l
    elif d == "S":
        waypoint[0] += l
    elif d == "W":
        waypoint[1] -= l
    elif d == "E":
        waypoint[1] += l
    elif d == "R":
        for _ in range(0, l, 90):
            waypoint = [waypoint[1], -waypoint[0]]
    elif d == "L":
        for _ in range(0, l, 90):
            waypoint = [-waypoint[1], waypoint[0]]
    elif d == "F":
        pos[0] += waypoint[0] * l
        pos[1] += waypoint[1] * l

print(abs(pos[0]) + abs(pos[1]))
