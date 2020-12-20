import itertools

data = []

try:
    while True:
        data.append(input())
except EOFError:
    pass

pos = [0, 0]


def slope(data, pos):
    pos[0] += 1
    pos[1] += 3
    pos[1] %= len(data[pos[0]])
    return data[pos[0]][pos[1]] == "#"


print(sum((slope(data, pos) for _ in range(len(data) - 1))))
