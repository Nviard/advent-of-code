import bisect
import itertools

data = []


def find(a, x):
    i = bisect.bisect_left(a, x)
    if i != len(a) and a[i] == x:
        return True
    return False


try:
    while True:
        data.append(int(input()))
except EOFError:
    pass
for i, d in enumerate(data[25:]):
    prev = data[i : i + 25]
    prev.sort()
    ok = False
    for p in prev:
        if d != p and find(prev, d - p):
            ok = True
            break
    if not ok:
        print(d)
        break
