import re

reing = re.compile(r"([a-z ]*) \(contains ([a-z ,]*)\)")

data = {}

try:
    while True:
        m = reing.match(input())
        ings = set(m.group(1).split())
        for al in m.group(2).split(", "):
            if al not in data:
                data[al] = set(ings)
            else:
                data[al].intersection_update(ings)
except EOFError:
    pass

ingredients = {}

while len(ingredients) < len(data):
    for k, v in data.items():
        v.difference_update(ingredients)
        if len(v) == 1:
            ingredients[v.pop()] = k

res = list(ingredients)
res.sort(key=lambda x: ingredients[x])

print(",".join(res))
