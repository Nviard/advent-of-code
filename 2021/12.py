data = {}

try:
    while True:
        x, y = input().split("-")
        if x not in data:
            data[x] = []
        if y not in data:
            data[y] = []
        data[x].append(y)
        data[y].append(x)
except EOFError:
    pass

res1 = set()
res2 = set()

current = set()
current.add(("start",))

while current:
    c = current.pop()
    for n in data[c[-1]]:
        if n == "end":
            if "twice" not in c:
                res1.add((*c, n))
            res2.add((*c, n))
        elif n.isupper() or n not in c:
            current.add((*c, n))
        elif n.islower() and n not in ("start", "end") and "twice" not in c:
            current.add((*c, "twice", n))

res1 = len(res1)
res2 = len(res2)

print(res1)
print(res2)
