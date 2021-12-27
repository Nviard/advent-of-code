import itertools

data = []
try:
    while True:
        i, xyz = input().split()
        x, y, z = xyz.split(",")
        x = tuple(map(int, x[2:].split("..")))
        y = tuple(map(int, y[2:].split("..")))
        z = tuple(map(int, z[2:].split("..")))
        data.append((i == "on", x, y, z))
except EOFError:
    pass

res1 = 0
res2 = 0

fixed = set()

for i, x, y, z in data[::-1]:
    if i:
        a, b, c = (
            (max(x[0], -50), min(x[1], 50)),
            (max(y[0], -50), min(y[1], 50)),
            (max(z[0], -50), min(z[1], 50)),
        )
        if a[1] <= a[0] or b[1] <= b[0] or c[1] <= c[0]:
            continue
        regions = set(((a, b, c),))
        for f in fixed:
            minx, maxx = f[0]
            miny, maxy = f[1]
            minz, maxz = f[2]
            current = set()
            for r in regions:
                mina, maxa = r[0]
                minb, maxb = r[1]
                minc, maxc = r[2]
                minxa, maxxa = max(minx, mina), min(maxx, maxa)
                minyb, maxyb = max(miny, minb), min(maxy, maxb)
                minzc, maxzc = max(minz, minc), min(maxz, maxc)
                if minxa > maxxa or minyb > maxyb or minzc > maxzc:
                    current.add(r)
                else:
                    if mina <= minxa <= maxa:
                        current.add(((mina, minxa - 1), (minb, maxb), (minc, maxc)))
                        mina = minxa
                    if mina <= maxxa <= maxa:
                        current.add(((maxxa + 1, maxa), (minb, maxb), (minc, maxc)))
                        maxa = maxxa
                    if minb <= minyb <= maxb:
                        current.add(((mina, maxa), (minb, minyb - 1), (minc, maxc)))
                        minb = minyb
                    if minb <= maxyb <= maxb:
                        current.add(((mina, maxa), (maxyb + 1, maxb), (minc, maxc)))
                        maxb = maxyb
                    if minc <= minzc <= maxc:
                        current.add(((mina, maxa), (minb, maxb), (minc, minzc - 1)))
                        minc = minzc
                    if minc <= maxzc <= maxc:
                        current.add(((mina, maxa), (minb, maxb), (maxzc + 1, maxc)))
                        maxc = maxzc
            regions = current
        for a, b, c in regions:
            res1 += (a[1] - a[0] + 1) * (b[1] - b[0] + 1) * (c[1] - c[0] + 1)
    fixed.add((x, y, z))

fixed = set()

for i, x, y, z in data[::-1]:
    if i:
        regions = set(((x, y, z),))
        for f in fixed:
            minx, maxx = f[0]
            miny, maxy = f[1]
            minz, maxz = f[2]
            current = set()
            for r in regions:
                mina, maxa = r[0]
                minb, maxb = r[1]
                minc, maxc = r[2]
                minxa, maxxa = max(minx, mina), min(maxx, maxa)
                minyb, maxyb = max(miny, minb), min(maxy, maxb)
                minzc, maxzc = max(minz, minc), min(maxz, maxc)
                if minxa > maxxa or minyb > maxyb or minzc > maxzc:
                    current.add(r)
                else:
                    if mina <= minxa <= maxa:
                        current.add(((mina, minxa - 1), (minb, maxb), (minc, maxc)))
                        mina = minxa
                    if mina <= maxxa <= maxa:
                        current.add(((maxxa + 1, maxa), (minb, maxb), (minc, maxc)))
                        maxa = maxxa
                    if minb <= minyb <= maxb:
                        current.add(((mina, maxa), (minb, minyb - 1), (minc, maxc)))
                        minb = minyb
                    if minb <= maxyb <= maxb:
                        current.add(((mina, maxa), (maxyb + 1, maxb), (minc, maxc)))
                        maxb = maxyb
                    if minc <= minzc <= maxc:
                        current.add(((mina, maxa), (minb, maxb), (minc, minzc - 1)))
                        minc = minzc
                    if minc <= maxzc <= maxc:
                        current.add(((mina, maxa), (minb, maxb), (maxzc + 1, maxc)))
                        maxc = maxzc
            regions = current
        for a, b, c in regions:
            res2 += (a[1] - a[0] + 1) * (b[1] - b[0] + 1) * (c[1] - c[0] + 1)
    fixed.add((x, y, z))


print(res1)
print(res2)
