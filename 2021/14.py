from collections import Counter

template = input()

input()

pairs = {}

try:
    while l := input():
        c, v = l.split(" -> ")
        pairs[c] = v
except EOFError:
    pass

res1 = Counter()
res2 = Counter()

data = Counter([template[i : i + 2] for i in range(len(template) - 1)])

for _ in range(10):
    current = Counter()
    for k, v in data.items():
        n = pairs[k]
        current[k[0] + n] += v
        current[n + k[1]] += v
    data = current

for k, v in data.items():
    res1[k[0]] += v
    res1[k[1]] += v

res1[template[0]] += 1
res1[template[-1]] += 1

res1 = res1.most_common()
res1 = res1[0][1] - res1[-1][1]
res1 /= 2

print(res1)

for _ in range(30):
    current = Counter()
    for k, v in data.items():
        n = pairs[k]
        current[k[0] + n] += v
        current[n + k[1]] += v
    data = current

for k, v in data.items():
    res2[k[0]] += v
    res2[k[1]] += v

res2[template[0]] += 1
res2[template[-1]] += 1

res2 = res2.most_common()
res2 = res2[0][1] - res2[-1][1]
res2 /= 2

print(res2)
