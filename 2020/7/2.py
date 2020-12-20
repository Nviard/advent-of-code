import re

r = re.compile("(.+) bags contain(.*)")
s = re.compile(" ([0-9]+) ([^,.]+) bags?[,.]")

data = {}

try:
    while True:
        line = input()
        m = r.match(line)
        data[m.group(1)] = {color: int(n) for n, color in s.findall(m.group(2))}
except EOFError:
    pass

res = 0

bags = data["shiny gold"]

while bags:
    color = tuple(bags.keys())[0]
    n = bags.pop(color)
    if data[color]:
        for k, v in data[color].items():
            if k not in bags:
                bags[k] = 0
            bags[k] += v * n
    res += n

print(res)
