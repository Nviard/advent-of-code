import itertools

data = [set()]

try:
    while True:
        line = input().split()
        if line:
            data[-1].update(*line)
        else:
            data.append(set())
except EOFError:
    pass

print(sum(map(len, data)))
