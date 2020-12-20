import itertools

data = []

try:
    while True:
        data.append(int(input()))
except EOFError:
    pass

for entries in itertools.permutations(data, 2):
    if sum(entries) == 2020:
        print(entries[0] * entries[1])
        break
