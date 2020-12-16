with open("input/q4.txt") as f:
    INPUT = f.read()

print(sum(
    1 for x in INPUT.split("\n\n")
    if all(f"{w}:" in x for w in ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"])
))
print(sum(
    1 for passport in INPUT.split("\n\n")
    if all(f"{w}:" in passport for w in ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"])
    and all(
        {
            "byr": lambda x: 1920 <= int(x) <= 2002,
            "iyr": lambda x: 2010 <= int(x) <= 2020,
            "eyr": lambda x: 2020 <= int(x) <= 2030,
            "hgt": lambda x:
                (x[-2:] == "cm" and 150 <= int(x[:-2]) <= 193)
                or (x[-2:] == "in" and 59 <= int(x[:-2]) <= 76),
            "hcl": lambda x:
                x[0] == "#" and len(x) == 7 and all(c in "0123456789abcdef" for c in x[1:]),
            "ecl": lambda x: x in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"],
            "pid": lambda x: len(x) == 9 and all(c in "0123456789" for c in x),
            "cid": lambda x: True,
        }[tag](value)
        for entry in passport.split()
        for tag, value in [entry.strip().split(":")]
    )
))
