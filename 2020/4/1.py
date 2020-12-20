import itertools

data = [{}]

try:
    while True:
        line = input().split()
        if line:
            for kv in line:
                k, v = kv.split(":")
                data[-1][k] = v
        else:
            data.append({})
except EOFError:
    pass

global fields

fields = set(("byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"))


def isvalid(p):
    return fields.intersection(p.keys()) == fields


print(sum((isvalid(p) for p in data)))
