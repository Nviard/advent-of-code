import re
import itertools

rmask = re.compile(r"mask = ([X01]+)")
rmem = re.compile(r"mem\[(\d+)\] = (\d+)")

data = {}

try:
    while True:
        line = input()
        if m := rmask.match(line):
            mask = m.group(1)
            mask0 = int(mask.replace("0", "1").replace("X", "0"), 2)
            mask1 = int(mask.replace("X", "0"), 2)
            floats = tuple(
                map(
                    sum,
                    itertools.product(
                        *(
                            (0, 2 ** (len(mask) - i - 1))
                            for i, x in enumerate(mask)
                            if x == "X"
                        )
                    ),
                )
            )
        elif m := rmem.match(line):
            address = int(m.group(1))
            val = int(m.group(2))
            address &= mask0
            address |= mask1
            for f in floats:
                data[address + f] = val
except EOFError:
    pass

print(sum(data.values()))
