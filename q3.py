from aocd import data
INPUT = data.splitlines()

PART2 = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]

print(sum(1 for i, x in enumerate(INPUT) if x[(3 * i) % len(x)] == "#"))
print(eval("*".join(str(sum(1 for i, x in enumerate(INPUT[::v_v]) if x[(v_h * i) % len(x)] == "#")) for v_h, v_v in PART2)))
