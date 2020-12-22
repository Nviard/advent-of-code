from collections import deque

data = (deque(), deque())

try:
    input()
    while l := input():
        data[0].append(int(l))
    input()
    while True:
        data[1].append(int(input()))
except EOFError:
    pass


def game(data):
    firstround = (tuple(data[0]), tuple(data[1]))
    previousrounds = set()
    while data[0] and data[1]:
        currentround = (tuple(data[0]), tuple(data[1]))
        if currentround in previousrounds:
            break
        previousrounds.add(currentround)
        p0 = data[0].popleft()
        p1 = data[1].popleft()
        if (p0 > len(data[0])) or (p1 > len(data[1])):
            if p0 > p1:
                data[0].append(p0)
                data[0].append(p1)
            else:
                data[1].append(p1)
                data[1].append(p0)
        else:
            subgame = game((deque(tuple(data[0])[:p0]), deque(tuple(data[1])[:p1])))
            if subgame[0]:
                data[0].append(p0)
                data[0].append(p1)
            else:
                data[1].append(p1)
                data[1].append(p0)
    return data


data = game(data)

print(sum((x * (i + 1) for i, x in enumerate(list(data[0] or data[1])[::-1]))))
