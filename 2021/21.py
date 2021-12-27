from collections import Counter

data = []

data.append(int(input().split(":")[1]) - 1)
data.append(int(input().split(":")[1]) - 1)


def deterministic_dice():
    current = 0
    while True:
        yield current + 1
        current += 1
        current %= 100


res1 = 0
res2 = 0

scores = [0, 0]
rolls = 0
pos = data.copy()
player = 0
dice = deterministic_dice()

while max(scores) < 1000:
    for _ in range(3):
        pos[player] += next(dice)
    pos[player] %= 10
    scores[player] += pos[player] + 1
    rolls += 3
    player = 1 - player


res1 = min(scores) * rolls

games = {(*data, 0, 0, 0): 1}
wins = [0, 0]

dice = tuple(
    Counter(
        (i + j + k for i in range(1, 4) for j in range(1, 4) for k in range(1, 4))
    ).items()
)

while games:
    k = list(games.keys())[0]
    g = games.pop(k)
    for d, n in dice:
        c = list(k)
        w = g * n
        c[c[-1]] += d
        c[c[-1]] %= 10
        c[2 + c[-1]] += c[c[-1]] + 1
        if c[2 + c[-1]] > 20:
            wins[c[-1]] += w
        else:
            c[-1] = 1 - c[-1]
            c = tuple(c)
            if c in games:
                games[c] += w
            else:
                games[c] = w

res2 = max(wins)

print(res1)
print(res2)
