import re

rmask = re.compile(r"mask = ([X01]+)")
rmem = re.compile(r"mem\[(\d+)\] = (\d+)")

data = {}

try:
    while True:
        line = input()
        if m := rmask.match(line):
            mask = m.group(1)
            mask0 = int(mask.replace("X", "1"), 2)
            mask1 = int(mask.replace("X", "0"), 2)
        elif m := rmem.match(line):
            address = int(m.group(1))
            val = int(m.group(2))
            val &= mask0
            val |= mask1
            data[address] = val
except EOFError:
    pass

print(sum(data.values()))
