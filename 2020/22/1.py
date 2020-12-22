from collections import deque

data = (deque(), deque())

try:
    input()
    while l := input():
        data[0].append(int(l))
    input()
    while True:
        data[1].append(int(input()))
except EOFError:
    pass

while data[0] and data[1]:
    p0 = data[0].popleft()
    p1 = data[1].popleft()
    if p0 > p1:
        data[0].append(p0)
        data[0].append(p1)
    else:
        data[1].append(p1)
        data[1].append(p0)

print(sum((x * (i + 1) for i, x in enumerate(list(data[0] or data[1])[::-1]))))
