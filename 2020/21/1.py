import re
from collections import Counter

reing = re.compile(r"([a-z ]*) \(contains ([a-z ,]*)\)")

data = {}

ingredients = []

try:
    while True:
        m = reing.match(input())
        ings = set(m.group(1).split())
        for al in m.group(2).split(", "):
            if al not in data:
                data[al] = set(ings)
            else:
                data[al].intersection_update(ings)
        ingredients.extend(ings)
except EOFError:
    pass

res = Counter(ingredients)

for ings in data.values():
    for ing in ings:
        if ing in res:
            del res[ing]

print(sum(res.values()))
