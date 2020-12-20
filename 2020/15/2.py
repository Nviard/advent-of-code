data = tuple(map(int, "14,8,16,0,1,17".split(",")))

spoken = {n: i for i, n in enumerate(data[:-1])}
current = data[-1]

for i in range(len(data) - 1, 29999999):
    if current not in spoken:
        nex = 0
    else:
        nex = i - spoken[current]
    spoken[current] = i
    current = nex

print(current)
