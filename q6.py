with open("input/q6.txt") as f:
    INPUT = f.read()

print(sum(len(set(x.replace("\n", ""))) for x in INPUT.split("\n\n")))
print(sum(1 for x in INPUT.split("\n\n") for y in "abcdefghijklmnopqrstuvwxyz" if all(y in p for p in x.split("\n"))))
