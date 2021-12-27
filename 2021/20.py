data = []

decode = input().replace(".", "0").replace("#", "1")

input()
try:
    while True:
        data.append("0" + input().replace(".", "0").replace("#", "1") + "00")
except EOFError:
    pass

data.insert(0, "0" * len(data[0]))
data.insert(0, "0" * len(data[0]))
data.append("0" * len(data[0]))
data.append("0" * len(data[0]))

res1 = 0
res2 = 0

for i in range(2):
    result = []
    for y in range(1, len(data) - 1):
        line = "00" if i % 2 == 1 else "11"
        for x in range(1, len(data[y]) - 1):
            line += decode[
                int(
                    data[y - 1][x - 1 : x + 2]
                    + data[y][x - 1 : x + 2]
                    + data[y + 1][x - 1 : x + 2],
                    2,
                )
            ]
        line += "00" if i % 2 == 1 else "11"
        result.append(line)
    data = result
    data.insert(0, ("0" if i % 2 == 1 else "1") * len(data[0]))
    data.insert(0, ("0" if i % 2 == 1 else "1") * len(data[0]))
    data.append(("0" if i % 2 == 1 else "1") * len(data[0]))
    data.append(("0" if i % 2 == 1 else "1") * len(data[0]))

res1 = sum(sum(map(int, l)) for l in data)

for i in range(48):
    result = []
    for y in range(1, len(data) - 1):
        line = "00" if i % 2 == 1 else "11"
        for x in range(1, len(data[y]) - 1):
            line += decode[
                int(
                    data[y - 1][x - 1 : x + 2]
                    + data[y][x - 1 : x + 2]
                    + data[y + 1][x - 1 : x + 2],
                    2,
                )
            ]
        line += "00" if i % 2 == 1 else "11"
        result.append(line)
    data = result
    data.insert(0, ("0" if i % 2 == 1 else "1") * len(data[0]))
    data.insert(0, ("0" if i % 2 == 1 else "1") * len(data[0]))
    data.append(("0" if i % 2 == 1 else "1") * len(data[0]))
    data.append(("0" if i % 2 == 1 else "1") * len(data[0]))

res = sum(sum(map(int, l)) for l in data)

print(res1)
print(res2)
