data = list(map(int, "389547612"))
cups = {}
for i in range(0, 1000000):
    if i < len(data) - 1:
        cups[data[i]] = data[i + 1]
    elif i == (len(data) - 1):
        cups[data[i]] = len(data) + 1
    elif i == 999999:
        cups[i + 1] = data[0]
    else:
        cups[i + 1] = i + 2

current = data[0]
for _ in range(10000000):
    p1 = cups[current]
    p2 = cups[p1]
    p3 = cups[p2]

    cups[current] = cups[p3]

    d = current - 1

    while d in (0, p1, p2, p3):
        d -= 1
        d %= 1000001

    cups[p3] = cups[d]
    cups[d] = p1

    current = cups[current]

print(cups[1] * cups[cups[1]])
