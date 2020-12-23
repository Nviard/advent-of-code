data = list(map(int, "389547612"))

for _ in range(100):
    d = data.pop(0)
    picked, data = data[:3], [*data[3:], d]
    d -= 1
    d %= 10
    while d not in data:
        d -= 1
        d %= 10
    i = data.index(d)
    data = [*data[: i + 1], *picked, *data[i + 1 :]]

i = data.index(1)
print("".join(map(str, [*data[i + 1 :], *data[:i]])))
