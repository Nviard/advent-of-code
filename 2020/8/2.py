from copy import deepcopy

data = []
visited = set()

try:
    while True:
        line = input().split()
        data.append([line[0], int(line[1])])
except EOFError:
    pass


def step(data, visited):
    global pointer
    global acc
    visited.add(pointer)
    if data[pointer][0] == "nop":
        pointer += 1
    elif data[pointer][0] == "jmp":
        pointer += data[pointer][1]
    elif data[pointer][0] == "acc":
        acc += data[pointer][1]
        pointer += 1


def processTilLoop(data):
    global pointer
    global acc
    visited = set()
    pointer = 0
    acc = 0

    while pointer not in visited:
        if pointer == len(data):
            return acc
        step(data, visited)

    return None


for i, d in enumerate(data):
    if (d[0]) == "nop":
        copy = deepcopy(data)
        copy[i][0] = "jmp"
        res = processTilLoop(copy)
        if res is not None:
            break
    elif (d[0]) == "jmp":
        copy = deepcopy(data)
        copy[i][0] = "nop"
        res = processTilLoop(copy)
        if res is not None:
            break

print(acc)
