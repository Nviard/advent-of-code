import re

rules = {}
ruleslist = {}
rulespipe = {}

resimple = re.compile(r'(\d+): "(.+)"')
relist = re.compile(r"(\d+): ([\d ]+)$")
repipe = re.compile(r"(\d+): ([\d ]+) \| ([\d ]+)")
data = []

try:
    while l := input():
        if m := repipe.match(l):
            rulespipe[m.group(1)] = (m.group(2).split(), m.group(3).split())
        elif m := relist.match(l):
            ruleslist[m.group(1)] = m.group(2).split()
        elif m := resimple.match(l):
            rules[m.group(1)] = m.group(2)
    while True:
        data.append(input())
except EOFError:
    pass


def getrule(rules, ruleslist, rulespipe, key):
    if key not in rules:
        if key in ruleslist:
            rules[key] = "".join(
                (getrule(rules, ruleslist, rulespipe, k) for k in ruleslist[key])
            )
        elif key in rulespipe:
            rules[
                key
            ] = f"({''.join((getrule(rules, ruleslist, rulespipe, k) for k in rulespipe[key][0]))}|{''.join((getrule(rules, ruleslist, rulespipe, k) for k in rulespipe[key][1]))})"
    return rules[key]


rule0 = re.compile(getrule(rules, ruleslist, rulespipe, "0"))

print(sum((1 for d in data if rule0.fullmatch(d))))
