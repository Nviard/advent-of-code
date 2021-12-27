data = []

try:
    while True:
        d = list(map(int, input()))
        data.append(d)
except EOFError:
    pass
size = len(data)

data = list(map(list, zip(*data)))

res1 = 0
res2 = 0

gamma = 0
epsilon = 0

value = 1

for d in data[::-1]:
    d = sum(d)
    if d >= size / 2:
        gamma += value
    else:
        epsilon += value
    value *= 2

res1 = int(gamma * epsilon)

o2 = 0
co2 = 0

value = 2 ** (len(data) - 1)

remove_o2 = set()
remove_co2 = set()
for d in range(len(data)):
    d_o2 = sum((data[d][x] for x in range(len(data[d])) if x not in remove_o2))
    if d_o2 >= (len(data[d]) - len(remove_o2)) / 2:
        o2 += value
        remove_o2 = remove_o2.union((x for x in range(len(data[d])) if data[d][x] == 0))
    else:
        remove_o2 = remove_o2.union((x for x in range(len(data[d])) if data[d][x] == 1))
    d_co2 = sum((data[d][x] for x in range(len(data[d])) if x not in remove_co2))
    if (
        d_co2 < (len(data[d]) - len(remove_co2)) / 2
        or d_co2 == (len(data[d]) - len(remove_co2))
    ) and d_co2:
        co2 += value
        remove_co2 = remove_co2.union(
            (x for x in range(len(data[d])) if data[d][x] == 0)
        )
    else:
        remove_co2 = remove_co2.union(
            (x for x in range(len(data[d])) if data[d][x] == 1)
        )
    value /= 2

res2 = int(o2 * co2)

print(res1)
print(res2)
