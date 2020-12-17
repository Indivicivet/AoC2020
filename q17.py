with open("input/q17.txt") as f:
    INPUT = f.read().splitlines()

print(
    (lambda state: sum(w == "#" for w in state.values()))(
        (do_six := lambda updater, vals:
            updater(updater(updater(updater(updater(updater(vals))))))
        )(
            lambda prev: {
                (k, j, i): ("#" if ((
                        neighbours := sum(prev.get((k + r, j + q, i + p), 0) == "#"
                        for r in [-1, 0, 1] for q in [-1, 0, 1] for p in [-1, 0, 1])
                    ) in [3, 4] and v == "#") or (neighbours == 3 and v == ".")
                    else ".")
                for (k, j, i), v in prev.items()
            },
            {
                **{(k, j, i): "." for k in range(-6, 7) for j in range(-6, 6 + len(INPUT)) for i in range(-6, 6 + len(INPUT[0]))},
                **{(0, j, i): x for j, row in enumerate(INPUT) for i, x in enumerate(row)},
            }
        )
    )
)
print(
    (lambda state: sum(w == "#" for w in state.values()))(
        (do_six := lambda updater, vals:
            updater(updater(updater(updater(updater(updater(vals))))))
        )(
            lambda prev: {
                (m, k, j, i): ("#" if ((
                        neighbours := sum(prev.get((m + s, k + r, j + q, i + p), 0) == "#"
                        for s in [-1, 0, 1] for r in [-1, 0, 1] for q in [-1, 0, 1] for p in [-1, 0, 1])
                    ) in [3, 4] and v == "#") or (neighbours == 3 and v == ".")
                    else ".")
                for (m, k, j, i), v in prev.items()
            },
            {
                **{(m, k, j, i): "." for m in range(-6, 7) for k in range(-6, 7) for j in range(-6, 6 + len(INPUT)) for i in range(-6, 6 + len(INPUT[0]))},
                **{(0, 0, j, i): x for j, row in enumerate(INPUT) for i, x in enumerate(row)},
            }
        )
    )
)
