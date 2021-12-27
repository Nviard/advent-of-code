data = input().split(",")
data = [d.split("=")[1] for d in data]
data = [list(map(int, d.split(".."))) for d in data]

res1 = 0
res2 = 0

maxy = abs(data[1][0]) - 1
res1 = int(maxy * (maxy + 1) / 2)

miny = data[1][0]

maxx = data[0][1]

x = 0
minx = 0
while x < data[0][0]:
    minx += 1
    x += minx

print(res1)

for x in range(minx, maxx + 1):
    for y in range(miny, maxy + 1):
        vx = x
        vy = y
        cx, cy = 0, 0
        while (cx <= data[0][1]) and (cy >= data[1][0]):
            cx += vx
            cy += vy
            if vx > 0:
                vx -= 1
            vy -= 1
            if (
                (cx <= data[0][1])
                and (cx >= data[0][0])
                and (cy <= data[1][1])
                and (cy >= data[1][0])
            ):
                res2 += 1
                break


print(res2)
