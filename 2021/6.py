data = list(map(int, input().split(",")))

res1 = 0
res2 = 0

lf = [0] * 9
for d in data:
    lf[d] += 1

for _ in range(80):
    p = lf.pop(0)
    lf[-2] += p
    lf.append(p)


res1 = sum(lf)

for _ in range(256 - 80):
    p = lf.pop(0)
    lf[-2] += p
    lf.append(p)

res2 = sum(lf)

print(res1)
print(res2)
