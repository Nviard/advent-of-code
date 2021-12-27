data = []
try:
    while True:
        data.append(input())
except EOFError:
    pass

res1 = 0
res2 = 0


def snailfish(data):
    depth = 0
    s = []
    for d in data:
        if d == "[":
            depth += 1
        elif d == "]":
            depth -= 1
        elif d != ",":
            s.append([depth, int(d)])
    return s


def add(d1, d2):
    res = [*d1, *d2]
    for r in res:
        r[0] += 1
    res = reduce(res)
    return res


def reduce(data):
    changed = True
    while changed:
        changed, data = explode(data)
        if not changed:
            changed, data = split(data)
    return data


def explode(data):
    for i, d in enumerate(data):
        if d[0] == 5:
            if i > 0:
                data[i - 1][1] += d[1]
            if (i + 2) < len(data):
                data[i + 2][1] += data[i + 1][1]
            d[0] = 4
            d[1] = 0
            data.pop(i + 1)
            return True, data

    return False, data


def split(data):
    for i, d in enumerate(data):
        if d[1] > 9:
            data.insert(i + 1, [d[0] + 1, int(d[1] / 2 + 0.5)])
            d[1] = int(d[1] / 2)
            d[0] += 1
            return True, data

    return False, data


def magnitude(data):
    while len(data) > 1:
        for i, d in enumerate(data):
            if d[0] == data[i + 1][0]:
                d[0] -= 1
                d[1] = d[1] * 3 + data[i + 1][1] * 2
                data.pop(i + 1)
                break
    return data[0][1]


current = snailfish(data[0])
for d in data[1:]:
    current = add(current, snailfish(d))

res1 = magnitude(current)


for d in data:
    for d2 in data:
        if d != d2:
            res2 = max(res2, magnitude(add(snailfish(d), snailfish(d2))))


print(res1)
print(res2)
