import re

fields = []

tickets = []

refield = re.compile(r"([a-z ]+): (\d+)-(\d+) or (\d+)-(\d+)")

try:
    l = input()
    while l:
        m = refield.match(l)
        fields.append(
            (int(m.group(2)), int(m.group(3)), int(m.group(4)), int(m.group(5)))
        )
        l = input()
    input()
    input()
    input()
    input()
    while True:
        tickets.append(tuple(map(int, input().split(","))))
except EOFError:
    pass

res = 0
for t in tickets:
    for v in t:
        if not any(
            (
                ((v >= f[0]) and (v <= f[1])) or ((v >= f[2]) and (v <= f[3]))
                for f in fields
            )
        ):
            res += v

print(res)
