data = [0]

try:
    while True:
        data.append(int(input()))
except EOFError:
    pass

data.sort()

paths = {0: 1}

for i in range(1, len(data)):
    paths[i] = paths[i - 1]
    if (i > 1) and (data[i] - data[i - 2] < 4):
        paths[i] += paths[i - 2]
    if (i > 2) and (data[i] - data[i - 3] < 4):
        paths[i] += paths[i - 3]

print(paths[len(data) - 1])
