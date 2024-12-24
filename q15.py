from aocd import data
INPUT = [int(x) for x in data.split(",")]

print(
    (lambda turns, said_times:
        max(enumerate(
            (
                turns.__iadd__([len(turns) - said_times.get(turns[-1], len(turns))]),
                said_times.update({turns[-2]: len(turns) - 1}),
            )
            for _ in range(len(turns), 2020)
        ))[1][0][-1]
    )(INPUT, {v: i + 1 for i, v in enumerate(INPUT)})
)
print(
    (lambda turns, said_times:
        max(enumerate(
            (
                turns.__iadd__([len(turns) - said_times.get(turns[-1], len(turns))]),
                said_times.update({turns[-2]: len(turns) - 1}),
            )
            for _ in range(len(turns), 30000000)  # otherwise identical
        ))[1][0][-1]
    )(INPUT, {v: i + 1 for i, v in enumerate(INPUT)})
)
