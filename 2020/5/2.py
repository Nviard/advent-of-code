import itertools

data = []

try:
    while True:
        line = input()
        data.append(
            (
                int(line[:7].replace("F", "0").replace("B", "1"), 2),
                int(line[7:].replace("L", "0").replace("R", "1"), 2),
            )
        )
except EOFError:
    pass

data = set(data)


def id(seat):
    return seat[0] * 8 + seat[1]


for seat in itertools.product(
    range(min((s[0] for s in data)), max((s[0] for s in data))), range(0, 8)
):
    if seat not in data:
        print(id(seat))
        break
