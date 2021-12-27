data = []
try:
    while True:
        data.append(tuple(input().split()))
except EOFError:
    pass

res1 = 0
res2 = 0

# (d == e - 6)
# and (f == c - 6)
# and (h == g - 2)
# and (j == i - 1)
# and (l == k - 0)
# and (b == m - 8)
# and (a == n - 4)

a, b, c, d, e, f, g, h, i, j, k, l, m, n = [9] * 14

d = e - 6
f = c - 6
h = g - 2
j = i - 1
l = k
b = m - 8
a = n - 4


params = [a, b, c, d, e, f, g, h, i, j, k, l, m, n]
res1 = "".join(map(str, params))

print(res1)

a, b, c, d, e, f, g, h, i, j, k, l, m, n = [1] * 14

e = d + 6
c = f + 6
g = h + 2
i = j + 1
l = k
m = b + 8
n = a + 4


params = [a, b, c, d, e, f, g, h, i, j, k, l, m, n]
res2 = "".join(map(str, params))
print(res2)
