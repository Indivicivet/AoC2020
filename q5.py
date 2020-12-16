with open("input/q5.txt") as f:
    INPUT = f.read().splitlines()

print(max(int(s[:-3].replace("F", "0").replace("B", "1"), 2) * 8 + int(s[-3:].replace("L", "0").replace("R", "1"), 2) for s in INPUT))
print(next(
    8 * (col.find("xox") + 1) + idx
    for idx, col in enumerate(
        "".join(
            "x" if f"{i:07b}".replace("0", "F").replace("1", "B") + f"{j:03b}".replace("0", "L").replace("1", "R") in INPUT else "o"
            for i in range(128)
        )
        for j in range(8)
    )
    if col.find("xox") != -1
))
