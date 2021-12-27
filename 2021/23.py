import bisect

input()
input()
_, _, _, a, _, b, _, c, _, d, _, _, _ = input()
_, _, _, e, _, f, _, g, _, h, _ = input()

res1 = 0
res2 = 0

cost = {"A": 1, "B": 10, "C": 100, "D": 1000}

PATHS = (
    ("A", 0, 1, 2, 11),
    ("A", 1, 2, 11),
    ("A", 3, 2, 11),
    ("A", 5, 4, 3, 2, 11),
    ("A", 7, 6, 5, 4, 3, 2, 11),
    ("A", 9, 8, 7, 6, 5, 4, 3, 2, 11),
    ("A", 10, 9, 8, 7, 6, 5, 4, 3, 2, 11),
    ("B", 0, 1, 2, 3, 4, 12),
    ("B", 1, 2, 3, 4, 12),
    ("B", 3, 4, 12),
    ("B", 5, 4, 12),
    ("B", 7, 6, 5, 4, 12),
    ("B", 9, 8, 7, 6, 5, 4, 12),
    ("B", 10, 9, 8, 7, 6, 5, 4, 12),
    ("C", 0, 1, 2, 3, 4, 5, 6, 13),
    ("C", 1, 2, 3, 4, 5, 6, 13),
    ("C", 3, 4, 5, 6, 13),
    ("C", 5, 6, 13),
    ("C", 7, 6, 13),
    ("C", 9, 8, 7, 6, 13),
    ("C", 10, 9, 8, 7, 6, 13),
    ("D", 0, 1, 2, 3, 4, 5, 6, 7, 8, 14),
    ("D", 1, 2, 3, 4, 5, 6, 7, 8, 14),
    ("D", 3, 4, 5, 6, 7, 8, 14),
    ("D", 5, 6, 7, 8, 14),
    ("D", 7, 8, 14),
    ("D", 9, 8, 14),
    ("D", 10, 9, 8, 14),
)

current = [""] * 11
current.extend([a, b, c, d, e, f, g, h])
current = tuple(current)

target = [""] * 11
target = (*target, "A", "B", "C", "D", "A", "B", "C", "D")

evaluated = set()
states = [(0, current)]

paths = []
for p in PATHS:
    paths.append(p)
    paths.append((*p, p[-1] + 4))

paths = tuple(paths)

while True:
    V, K = states.pop(0)
    if K in evaluated:
        continue
    if K == target:
        res1 = V
        break
    cols = {}
    cols["A"] = next((i for i in range(11, len(K), 4) if K[i] != "A" and K[i] != ""), 0)
    cols["B"] = next((i for i in range(12, len(K), 4) if K[i] != "B" and K[i] != ""), 0)
    cols["C"] = next((i for i in range(13, len(K), 4) if K[i] != "C" and K[i] != ""), 0)
    cols["D"] = next((i for i in range(14, len(K), 4) if K[i] != "D" and K[i] != ""), 0)
    for p in paths:
        if cols[p[0]] == 0:
            if (
                K[p[1]] == p[0]
                and all(K[x] == "" for x in p[2:])
                and all(K[x] == p[0] for x in range(p[-1] + 4, len(K), 4))
            ):
                k = list(K)
                k[p[-1]] = p[0]
                k[p[1]] = ""
                k = tuple(k)
                if k not in evaluated:
                    v = V + cost[p[0]] * (len(p) - 2)
                    bisect.insort_left(states, (v, k))
        if (
            K[p[-1]] != ""
            and chr(ord("A") + (p[-1] - 11) % 4) != 0
            and all(K[x] == "" for x in p[1:-1])
        ):
            k = list(K)
            k[p[1]] = k[p[-1]]
            k[p[-1]] = ""
            k = tuple(k)
            if k not in evaluated:
                v = V + cost[k[p[1]]] * (len(p) - 2)
                bisect.insort_left(states, (v, k))

    evaluated.add(K)


print(res1)

current = [""] * 11
current.extend([a, b, c, d, "D", "C", "B", "A", "D", "B", "A", "C", e, f, g, h])
current = tuple(current)

target = [""] * 11
target = (
    *target,
    "A",
    "B",
    "C",
    "D",
    "A",
    "B",
    "C",
    "D",
    "A",
    "B",
    "C",
    "D",
    "A",
    "B",
    "C",
    "D",
)

evaluated = set()
states = [(0, current)]

paths = []
for p in PATHS:
    paths.append(p)
    paths.append((*p, p[-1] + 4))
    paths.append((*p, p[-1] + 4, p[-1] + 8))
    paths.append((*p, p[-1] + 4, p[-1] + 8, p[-1] + 12))

paths = tuple(paths)

while True:
    V, K = states.pop(0)
    if K in evaluated:
        continue
    if K == target:
        res2 = V
        break
    cols = {}
    cols["A"] = next((i for i in range(11, len(K), 4) if K[i] != "A" and K[i] != ""), 0)
    cols["B"] = next((i for i in range(12, len(K), 4) if K[i] != "B" and K[i] != ""), 0)
    cols["C"] = next((i for i in range(13, len(K), 4) if K[i] != "C" and K[i] != ""), 0)
    cols["D"] = next((i for i in range(14, len(K), 4) if K[i] != "D" and K[i] != ""), 0)
    for p in paths:
        if cols[p[0]] == 0:
            if (
                K[p[1]] == p[0]
                and all(K[x] == "" for x in p[2:])
                and all(K[x] == p[0] for x in range(p[-1] + 4, len(K), 4))
            ):
                k = list(K)
                k[p[-1]] = p[0]
                k[p[1]] = ""
                k = tuple(k)
                if k not in evaluated:
                    v = V + cost[p[0]] * (len(p) - 2)
                    bisect.insort_left(states, (v, k))
        if (
            K[p[-1]] != ""
            and chr(ord("A") + (p[-1] - 11) % 4) != 0
            and all(K[x] == "" for x in p[1:-1])
        ):
            k = list(K)
            k[p[1]] = k[p[-1]]
            k[p[-1]] = ""
            k = tuple(k)
            if k not in evaluated:
                v = V + cost[k[p[1]]] * (len(p) - 2)
                bisect.insort_left(states, (v, k))

    evaluated.add(K)

print(res2)
