from aocd import data
INPUT = data.splitlines()

print(
    (lambda prog:
        (result := (lambda pos, acc, visited:
            acc if pos in visited else result(
                *(lambda p, a, instr, val: {
                    "nop": (p + 1, a), "acc": (p + 1, a + val), "jmp": (p + val, a),
                }[instr])(pos, acc, *prog[pos]),
                visited + [pos]
            )
        ))(0, 0, [])
    )(
        [(x, int(n)) for line in INPUT for (x, n) in [line.split(" ")]]
    )
)
print(
    next(filter(None,
        (lambda prog_orig: (
            (lambda prog:
                (result := (lambda pos, acc, visited:
                    None if pos in visited else acc if pos >= len(prog) else result(
                        *(lambda p, a, instr, val: {
                            "nop": (p + 1, a), "acc": (p + 1, a + val), "jmp": (p + val, a),
                        }[instr])(pos, acc, *prog[pos]),
                        visited + [pos]
                    )
                ))(0, 0, [])
            )([
                ({(i, "jmp"): "nop", (i, "nop"): "jmp"}.get((j, instr), instr), val)
                for j, (instr, val) in enumerate(prog_orig)
            ])
            for i in range(len(prog_orig))
        ))(
            [(x, int(n)) for line in INPUT for (x, n) in [line.split(" ")]]
        )
    ))
)
