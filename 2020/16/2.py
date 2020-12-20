import re
from functools import reduce
from operator import mul

fields = {}

tickets = []

refield = re.compile(r"([a-z ]+): (\d+)-(\d+) or (\d+)-(\d+)")

try:
    l = input()
    while l:
        m = refield.match(l)
        fields[m.group(1)] = (
            int(m.group(2)),
            int(m.group(3)),
            int(m.group(4)),
            int(m.group(5)),
        )
        l = input()
    input()
    ticket = tuple(map(int, input().split(",")))
    # tickets.append(ticket)
    input()
    input()
    while True:
        tickets.append(tuple(map(int, input().split(","))))
except EOFError:
    pass

pos = [set((n for n in fields)) for v in ticket]
for t in tickets:
    candidates = [
        set(
            (
                n
                for n, f in fields.items()
                if ((v >= f[0]) and (v <= f[1])) or ((v >= f[2]) and (v <= f[3]))
            )
        )
        for v in t
    ]
    if min(map(len, candidates)) > 0:
        for i in range(len(ticket)):
            pos[i].intersection_update(candidates[i])

res = {}

while len(res) < len(ticket):
    for i, p in enumerate(pos):
        p.difference_update(res)
        if len(p) == 1:
            res[p.pop()] = i

print(reduce(mul, (ticket[v] for k, v in res.items() if k.startswith("departure"))))
