data = []

try:
    while True:
        d = input().split()
        data.append((d[0], int(d[1])))
except EOFError:
    pass

res1 = 0
res2 = 0

horizontal = 0
depth = 0

for d in data:
    if d[0] == "forward":
        horizontal += d[1]
    elif d[0] == "up":
        depth -= d[1]
    else:
        depth += d[1]

res1 = horizontal * depth

horizontal = 0
depth = 0
aim = 0

for d in data:
    if d[0] == "forward":
        horizontal += d[1]
        depth += d[1] * aim
    elif d[0] == "up":
        aim -= d[1]
    else:
        aim += d[1]

res2 = horizontal * depth

print(res1)
print(res2)
