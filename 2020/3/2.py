import itertools

data = []

try:
    while True:
        data.append(input())
except EOFError:
    pass

pos = [0, 0]


def slope(data, right, down, pos):
    pos[0] += down
    pos[1] += right
    pos[1] %= len(data[pos[0]])
    return data[pos[0]][pos[1]] == "#"


def fullslope(data, right, down):
    pos = [0, 0]
    return sum((slope(data, right, down, pos) for _ in range(0, len(data) - 1, down)))


print(
    fullslope(data, 1, 1)
    * fullslope(data, 3, 1)
    * fullslope(data, 5, 1)
    * fullslope(data, 7, 1)
    * fullslope(data, 1, 2)
)
