import itertools
import re

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
    valid = fields.intersection(p.keys()) == fields
    if valid:
        byr = int(p["byr"])
        valid = valid and (1920 <= byr <= 2002)
        iyr = int(p["iyr"])
        valid = valid and (2010 <= iyr <= 2020)
        eyr = int(p["eyr"])
        valid = valid and (2020 <= eyr <= 2030)
        hgt = p["hgt"][:-2] and int(p["hgt"][:-2])
        hgtu = p["hgt"][-2:]
        valid = valid and (
            (hgtu == "cm" and (150 <= hgt <= 193))
            or (hgtu == "in" and (59 <= hgt <= 76))
        )
        hcl = p["hcl"]
        valid = valid and (re.fullmatch("#[0-9a-z]{6}", hcl) is not None)
        ecl = p["ecl"]
        valid = valid and (ecl in ("amb", "blu", "brn", "gry", "grn", "hzl", "oth"))
        pid = p["pid"]
        valid = valid and (re.fullmatch("[0-9]{9}", pid) is not None)
    return valid


print(sum((isvalid(p) for p in data)))
