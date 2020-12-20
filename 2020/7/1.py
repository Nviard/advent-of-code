import re

r = re.compile("(.+) bags contain(.*)")
s = re.compile(" ([0-9]+) ([^,.]+) bags?[,.]")

data = {}

try:
    while True:
        line = input()
        m = r.match(line)
        for _, color in s.findall(m.group(2)):
            if color not in data:
                data[color] = set()
            data[color].add(m.group(1))
except EOFError:
    pass

res = set()
candidates = set(data["shiny gold"])

while candidates:
    c = candidates.pop()
    res.add(c)
    if c in data:
        candidates.update(data[c].difference(res))

print(len(res))
