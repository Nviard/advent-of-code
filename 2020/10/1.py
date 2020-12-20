data = [0]

try:
    while True:
        data.append(int(input()))
except EOFError:
    pass

data.sort()

data.append(data[-1] + 3)

d1 = 0
d3 = 0
for i in range(1, len(data)):
    if (data[i] - data[i - 1]) == 1:
        d1 += 1
    elif (data[i] - data[i - 1]) == 3:
        d3 += 1

print(d1 * d3)
