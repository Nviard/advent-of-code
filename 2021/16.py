import math

data = input()

data = "".join(f"{int(x, 16):0>4b}" for x in data)

res1 = 0
res2 = 0


def read_packet(data, start):
    current = start
    V = int(data[current : current + 3], 2)
    current += 3

    T = int(data[current : current + 3], 2)
    current += 3

    if T != 4:
        X = []
        I = int(data[current], 2)
        current += 1
        if I == 0:
            L = int(data[current : current + 15], 2)
            current += 15
            L += current
            while current < L:
                v, c, x = read_packet(data, current)
                V += v
                X.append(x)
                current = c
        else:
            L = int(data[current : current + 11], 2)
            current += 11
            for _ in range(L):
                v, c, x = read_packet(data, current)
                V += v
                X.append(x)
                current = c
        if T == 0:
            X = sum(X)
        elif T == 1:
            X = math.prod(X)
        elif T == 2:
            X = min(X)
        elif T == 3:
            X = max(X)
        elif T == 5:
            X = int(X[0] > X[1])
        elif T == 6:
            X = int(X[0] < X[1])
        elif T == 7:
            X = int(X[0] == X[1])
    else:
        f = 1
        X = 0
        while f:
            X *= 16
            f = int(data[current], 2)
            current += 1
            X += int(data[current : current + 4], 2)
            current += 4

    return V, current, X


res1, end, res2 = read_packet(data, 0)


print(res1)
print(res2)
