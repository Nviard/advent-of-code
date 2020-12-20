departure = int(input())

buses = tuple(map(int, filter(lambda x: x != "x", input().split(","))))

bus = min(buses, key=lambda bus: -departure % bus)

print(bus * (-departure % bus))
