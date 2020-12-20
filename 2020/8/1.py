global data
data = []

global visited
visited = set()

try:
    while True:
        line = input().split()
        data.append((line[0], int(line[1])))
except EOFError:
    pass

pointer = 0
acc = 0


def step():
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


while pointer not in visited:
    step()

print(acc)
