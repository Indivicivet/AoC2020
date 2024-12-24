from aocd import data
INPUT = data.splitlines()

print((lambda ints: next(a * b for a in ints for b in ints if a + b == 2020))([int(x) for x in INPUT]))
print((lambda ints: next(a * b * c for a in ints for b in ints for c in ints if a + b + c == 2020))([int(x) for x in INPUT]))
