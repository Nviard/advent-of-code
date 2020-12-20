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


def id(seat):
    return seat[0] * 8 + seat[1]


print(max((id(s) for s in data)))
