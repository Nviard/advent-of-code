import itertools

data = [None]

try:
    while True:
        line = input().split()
        if line:
            if data[-1] is None:
                data[-1] = set(*line)
            else:
                data[-1].intersection_update(*line)
        else:
            data.append(None)
except EOFError:
    pass

print(sum(map(len, data)))
