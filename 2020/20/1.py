import numpy as np
from collections import Counter
from operator import mul
from functools import reduce

data = {}

try:
    while True:
        _, n = input().split()
        n = int(n[:-1])
        data[n] = np.array([list(input()) for _ in range(10)])
        input()
except EOFError:
    pass

edges = {}
for n, x in data.items():
    for c in (x[0, :], x[9, :], x[:, 0], x[:, 9]):
        c = "".join(c)
        c = min(c, c[::-1])
        if c not in edges:
            edges[c] = []
        edges[c].append(n)

res = Counter()
for e in edges.values():
    if len(e) == 1:
        res.update(e)

print(reduce(mul, (x for x, _ in res.most_common(4))))
