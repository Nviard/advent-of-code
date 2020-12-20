import numpy as np
from collections import Counter
from operator import mul
from functools import reduce

data = {}

try:
    while True:
        _, n = input().split()
        n = int(n[:-1])
        data[n] = np.array([list(input()) for _ in range(10)])
        input()
except EOFError:
    pass


def get_edge_id(list_):
    c = "".join(list_)
    return min(c, c[::-1])


def get_edge(list_):
    return "".join(list_)


edges = {}
for n, x in data.items():
    for c in (x[0, :], x[9, :], x[:, 0], x[:, 9]):
        c = get_edge_id(c)
        if c not in edges:
            edges[c] = []
        edges[c].append(n)

corners = Counter()
for e in edges.values():
    if len(e) == 1:
        corners.update(e)

corners = tuple((x for x, _ in corners.most_common(4)))

image = data.pop(corners[0])
while (len(edges[get_edge_id(image[0, :])]) != 1) or (
    len(edges[get_edge_id(image[:, 0])]) != 1
):
    image = np.rot90(image)

for col in range(1, 12):
    c = get_edge_id(image[:, -1])
    co = get_edge(image[:, -1])
    piece = data.pop(next((p for p in edges[c] if p in data)))
    while get_edge_id(piece[:, 0]) != c:
        piece = np.rot90(piece)
    if co != get_edge(piece[:, 0]):
        piece = np.flipud(piece)
    image = np.concatenate((image, piece[:, 1:]), 1)

for row in range(1, 12):
    c = get_edge_id(image[-1, :10])
    co = get_edge(image[-1, :10])
    line = data.pop(next((p for p in edges[c] if p in data)))
    while get_edge_id(line[0, :]) != c:
        line = np.rot90(line)
    if co != get_edge(line[0, :]):
        line = np.fliplr(line)
    for col in range(1, 12):
        c = get_edge_id(line[:, -1])
        co = get_edge(line[:, -1])
        piece = data.pop(next((p for p in edges[c] if p in data)))
        while get_edge_id(piece[:, 0]) != c:
            piece = np.rot90(piece)
        if co != get_edge(piece[:, 0]):
            piece = np.flipud(piece)
        line = np.concatenate((line, piece[:, 1:]), 1)
    image = np.concatenate((image, line[1:, :]), 0)


image = np.delete(np.delete(image, range(0, 109, 9), axis=0), range(0, 109, 9), axis=1)


monster = np.array(
    [
        list("                  # "),
        list("#    ##    ##    ###"),
        list(" #  #  #  #  #  #   "),
    ]
)

res = 0
for _ in range(4):
    image = np.rot90(image)
    for _ in range(2):
        image = np.flipud(image)
        for _ in range(2):
            image = np.fliplr(image)
            res = max(
                res,
                sum(
                    (
                        np.all(
                            np.logical_or(
                                monster != "#", monster == image[r : r + 3, c : c + 20]
                            )
                        )
                        for c in range(0, 96 - 20)
                        for r in range(0, 96 - 3)
                    )
                ),
            )

print(sum(sum(image == "#")) - sum(sum(monster == "#")) * 43)
