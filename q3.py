with open("input/q3.txt") as f:
    INPUT = f.read()

PART2 = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]

print(sum(1 for i, x in enumerate(INPUT.splitlines()) if x[(3 * i) % len(x)] == "#"))
print(eval("*".join(str(sum(1 for i, x in enumerate(INPUT.splitlines()[::v_v]) if x[(v_h * i) % len(x)] == "#")) for v_h, v_v in PART2)))
