data = []

try:
    numbers = list(map(int, input().split(",")))
    input()
    while True:
        data.append([])
        for i in range(5):
            data[-1].extend(list(map(int, input().split())))
        input()
except EOFError:
    pass

res1 = 0
res2 = 0

size = len(data)
winners = set()

for n in numbers:
    for c, d in enumerate(data):
        if c not in winners:
            try:
                i = d.index(n)
                d[i] = None
                if any(
                    (
                        all(v is None for v in d[a:b:c])
                        for a, b, c in (
                            (0, 5, 1),
                            (5, 10, 1),
                            (10, 15, 1),
                            (15, 20, 1),
                            (20, 25, 1),
                            (0, 25, 5),
                            (1, 25, 5),
                            (2, 25, 5),
                            (3, 25, 5),
                            (4, 25, 5),
                        )
                    )
                ):
                    winners.add(c)
                    if not res1:
                        res1 = sum(filter(None, d)) * n
                    if len(winners) == size:
                        res2 = sum(filter(None, d)) * n
            except ValueError:
                pass
    if res2:
        break

print(res1)
print(res2)
