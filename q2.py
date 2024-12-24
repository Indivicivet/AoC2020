from aocd import data
INPUT = data.splitlines()

print(sum(1 for x in INPUT if (lambda ab, c_colon, word: int(ab.split("-")[0]) <= sum(1 for c in word if c==c_colon[0]) <= int(ab.split("-")[1]))(*x.split(" "))))
print(sum(1 for x in INPUT if (lambda ab, c_colon, word: (word[int(ab.split("-")[0]) - 1] == c_colon[0]) != (word[int(ab.split("-")[1]) - 1] == c_colon[0]))(*x.split(" "))))
