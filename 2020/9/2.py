import itertools

data = []

try:
    while True:
        data.append(int(input()))
except EOFError:
    pass

sums = [data[0]]

for i in range(len(data) - 1):
    sums.append(sums[-1] + data[i + 1])


for start, end in itertools.combinations(range(len(data)), 2):
    if (start == 0 and sums[end] == 731031916) or (
        start > 0 and (sums[end] - sums[start - 1]) == 731031916
    ):
        print(min(data[start : end + 1]) + max(data[start : end + 1]))
        break
