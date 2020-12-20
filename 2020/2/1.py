import re

data = []

try:
    while True:
        data.append(input().split())
except EOFError:
    pass

print(
    sum(
        (
            bool(
                re.search(
                    f"^[^{p[:-1]}]*({p[:-1]}[^{p[:-1]}]*){{{n.replace('-',',')}}}$", s
                )
            )
            for n, p, s in data
        )
    )
)
