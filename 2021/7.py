import statistics

data = list(map(int, input().split(",")))

res1 = 0
res2 = 0

res1 = statistics.median(data)

res1 = int(sum(abs(res1 - x) for x in data))

res2 = int(statistics.mean(data) + 0.5)

best = 99999999999999999

for j in range(res2 - 10, res2 + 10):
    best = min(best, sum(abs(x - j) * (abs(x - j) + 1) / 2 for x in data))

res2 = int(best)

print(res1)
print(res2)
