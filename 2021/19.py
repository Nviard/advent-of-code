data = []
try:
    while True:
        input()
        data.append([])
        while l := input():
            data[-1].append(tuple(map(int, l.split(","))))
except EOFError:
    pass

res1 = 0
res2 = 0


def rotate(x, y, z):
    return (
        (x, y, z),
        (x, z, -y),
        (y, x, -z),
        (y, z, x),
        (z, x, y),
        (z, y, -x),
        (-x, -y, z),
        (-x, -z, -y),
        (-y, -x, -z),
        (-y, -z, x),
        (-z, -x, y),
        (-z, -y, -x),
        (-x, y, -z),
        (-x, z, y),
        (-y, x, z),
        (-y, z, -x),
        (-z, x, -y),
        (-z, y, x),
        (x, -y, -z),
        (x, -z, y),
        (y, -x, z),
        (y, -z, -x),
        (z, -x, -y),
        (z, -y, x),
    )


distances = []

for d in data:
    distances.append({p: set() for p in d})
    for p1 in d:
        for p2 in d:
            if p1 != p2:
                m = sum((p1[i] - p2[i]) ** 2 for i in range(3))
                distances[-1][p1].add(m)
                distances[-1][p2].add(m)


equiv = []
for i1, d1 in enumerate(distances):
    for i2, d2 in enumerate(distances):
        if i1 != i2:
            for p1 in d1:
                for p2 in d2:
                    if len(d1[p1].intersection(d2[p2])) >= 11:
                        equiv.append((i1, p1, i2, p2))
transformations = {}


for i in range(0, len(data)):
    for j in range(0, len(data)):
        if i != j:
            eq = [e for e in equiv if e[0] == i and e[2] == j]
            if len(eq) >= 12:
                rotations = rotate(*eq[0][3])
                transformations[(j, i)] = {
                    r: (
                        eq[0][1][0] - rotations[r][0],
                        eq[0][1][1] - rotations[r][1],
                        eq[0][1][2] - rotations[r][2],
                    )
                    for r in range(len(rotations))
                }
                for e in eq[1:]:
                    rotations = rotate(*e[3])
                    translations = [
                        (
                            e[1][0] - rotations[r][0],
                            e[1][1] - rotations[r][1],
                            e[1][2] - rotations[r][2],
                        )
                        for r in range(len(rotations))
                    ]
                    transformations[(j, i)] = {
                        r: t
                        for r, t in transformations[(j, i)].items()
                        if translations[r] == t
                    }
                    if len(transformations[(j, i)]) == 1:
                        break

transformations = {k: list(v.items())[0] for k, v in transformations.items()}

beacons = [set(d) for d in data]

while True:
    for i1, b1 in enumerate(beacons):
        for i2, b2 in enumerate(beacons):
            if (i1, i2) in transformations:
                for p in b1:
                    r, t = transformations[(i1, i2)]
                    p = rotate(*p)[r]
                    p = (p[0] + t[0], p[1] + t[1], p[2] + t[2])
                    b2.add(p)

    lengths = [len(b) for b in beacons]
    if max(lengths) == min(lengths):
        break

res1 = len(beacons[0])


scanners = [set(((0, 0, 0),)) for d in data]

while True:
    for i1, b1 in enumerate(scanners):
        for i2, b2 in enumerate(scanners):
            if (i1, i2) in transformations:
                for p in b1:
                    r, t = transformations[(i1, i2)]
                    p = rotate(*p)[r]
                    p = (p[0] + t[0], p[1] + t[1], p[2] + t[2])
                    b2.add(p)

    lengths = [len(b) for b in scanners]
    if max(lengths) == min(lengths):
        break

res2 = max(max(sum(map(abs, y)) for y in x) for x in scanners)

print(res1)
print(res2)
