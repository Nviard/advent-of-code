inputs = []
outputs = []

try:
    while True:
        i, o = input().split("|")
        inputs.append(tuple(frozenset(x) for x in i.split()))
        outputs.append(tuple(frozenset(x) for x in o.split()))
except EOFError:
    pass

res1 = 0
res2 = 0

for o in outputs:
    for n in o:
        if len(n) in [2, 4, 3, 7]:
            res1 += 1

print(res1)


for i in range(len(inputs)):
    current = 0
    numbers = tuple(inputs[i])
    values = [None] * 10
    for n in numbers:
        if len(n) == 2:
            values[1] = n
        elif len(n) == 4:
            values[4] = n
        elif len(n) == 3:
            values[7] = n
        elif len(n) == 7:
            values[8] = n
    for n in numbers:
        if len(n) == 6:
            if values[4].issubset(n):
                values[9] = n
            elif values[1].issubset(n):
                values[0] = n
            else:
                values[6] = n
        if len(n) == 5:
            if values[1].issubset(n):
                values[3] = n
            elif values[4].difference(values[1]).issubset(n):
                values[5] = n
            else:
                values[2] = n
    values = {k: v for v, k in enumerate(values)}
    for x in outputs[i]:
        current *= 10
        current += values[x]
    res2 += current

print(res2)
