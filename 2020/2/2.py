data = []

try:
    while True:
        data.append(input().split())
        data[-1][0] = list(map(int, data[-1][0].split("-")))
        data[-1][1] = data[-1][1][:-1]
except EOFError:
    pass

print(sum(((s[n[0] - 1] == p) ^ (s[n[1] - 1] == p) for n, p, s in data)))
