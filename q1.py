with open("input/q1.txt") as f:
    INPUT = f.read()

SAN = [int(x) for x in INPUT.splitlines()]  # could inline but meh...

print(next(a * b for a in SAN for b in SAN if a + b == 2020))
print(next(a * b * c for a in SAN for b in SAN for c in SAN if a + b + c == 2020))
