data = []

try:
    while True:
        data.append(int(input()))
except EOFError:
    pass

res1 = 0
res2 = 0

for i in range(1, len(data)):
    if data[i] > data[i - 1]:
        res1 += 1

for i in range(3, len(data)):
    if data[i] > data[i - 3]:
        res2 += 1

print(res1)
print(res2)
