with open("input/q16.txt") as f:
    INPUT = f.read().splitlines()

print(
    (lambda ranges: sum(
        int(x) for line in INPUT for x in line.split(",")
        if "," in line and not any(int(x) in r for r in ranges)
    ))([
        sum((
            list(range(int(y.split("-")[0]), int(y.split("-")[1]) + 1))
            for y in line.split(":")[1].split("or")
        ), []) for line in INPUT if "or" in line
    ])
)
print(
    (lambda mapping, my_ticket: eval("*".join(str(my_ticket[mapping[j]]) for j in range(6))))(
        (lambda fields: {y[0]: x for x, y in fields.items()})(
            (update := lambda cands: (
                cands if all(len(v) == 1 for v in cands.values())
                else update({
                    k: [x for x in v if [x] == v or [x] not in cands.values()] for k, v in cands.items()
                })
            ))(
                (lambda ranges:
                    (lambda good_tix: {
                        pos: [i for i, r in enumerate(ranges) if all(t[pos] in r for t in good_tix)]
                        for pos in range(len(good_tix[0]))
                    })([
                        t for t in [[int(x) for x in line.split(",")] for line in INPUT if "," in line]
                        if all(any(v in r for r in ranges) for v in t)
                    ])
                )([
                    sum((
                        list(range(int(y.split("-")[0]), int(y.split("-")[1]) + 1))
                        for y in line.split(": ")[1].split(" or ")
                    ), []) for line in INPUT if "or" in line
                ])
            )
        ),
        next([int(x) for x in line.split(",")] for line in INPUT if "," in line),
    )
)
