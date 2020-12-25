card = int(input())
door = int(input())

subject = 7
modulo = 20201227

l = 0

ccard = 1
cdoor = 1

lcard = None
ldoor = None

while not lcard and not ldoor:
    l += 1
    if not lcard:
        ccard *= subject
        ccard %= modulo
        if ccard == card:
            lcard = l
    if not ldoor:
        cdoor *= subject
        cdoor %= modulo
        if cdoor == door:
            ldoor = l

if lcard:
    print(pow(door, lcard, modulo))
else:
    print(pow(card, ldoor, modulo))
