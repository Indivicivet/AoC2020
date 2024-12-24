from aocd import data as INPUT

print(sum(len(set(x.replace("\n", ""))) for x in INPUT.split("\n\n")))
print(sum(1 for x in INPUT.split("\n\n") for y in "abcdefghijklmnopqrstuvwxyz" if all(y in p for p in x.split("\n"))))
