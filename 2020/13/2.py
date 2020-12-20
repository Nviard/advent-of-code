from operator import mul
from functools import reduce

# from math import gcd

input()

buses = {int(x): i for i, x in enumerate(input().split(",")) if x != "x"}

step = max(buses.keys())
i = step - buses[step]

ok = set((step,))

while len(ok) + len(
    t := tuple((k for k, v in buses.items() if (k not in ok) and ((i + v) % k) == 0))
) < len(buses):
    if t:
        ok.update(t)
        step = reduce(mul, ok)  # // reduce(gcd, ok)
    i += step

print(i)
