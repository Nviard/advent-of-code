from collections import Counter

data = []

try:
    while True:
        line = input().split(" -> ")
        data.append(list(map(int, line[0].split(","))))
        data[-1].extend(map(int, line[1].split(",")))

except EOFError:
    pass

res1 = Counter()
res2 = Counter()

for x1, y1, x2, y2 in data:
    if x1 == x2:
        res1.update((x1, y) for y in range(min(y1, y2), max(y1, y2) + 1))
    elif y1 == y2:
        res1.update((x, y1) for x in range(min(x1, x2), max(x1, x2) + 1))
    else:
        if x1 > x2:
            if y1 > y2:
                res2.update((x2 + d, y2 + d) for d in range(x1 - x2 + 1))
            else:
                res2.update((x2 + d, y2 - d) for d in range(x1 - x2 + 1))
        else:
            if y1 > y2:
                res2.update((x1 + d, y1 - d) for d in range(x2 - x1 + 1))
            else:
                res2.update((x1 + d, y1 + d) for d in range(x2 - x1 + 1))

res2.update(res1)
res1 = len([k for k, v in res1.items() if v > 1])
res2 = len([k for k, v in res2.items() if v > 1])

print(res1)
print(res2)
