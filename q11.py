with open("input/q11.txt") as f:
    INPUT = f.read()

print(
    (lambda state: sum(w == "#" for w in state.values()))(
        (find_steady := lambda updater, vals:
            new_vals if (new_vals := updater(vals)) == vals else find_steady(updater, new_vals)
        )(
            lambda prev: {
                (j, i): "#L"[v == "#"]
                    if v == "Lxxxx#####"[sum(prev.get((j + q, i + p), 0) == "#" for q in [-1, 0, 1] for p in [-1, 0, 1])]
                    else v
                for (j, i), v in prev.items()
            },
            {(j, i): x for j, row in enumerate(INPUT.splitlines()) for i, x in enumerate(row)}
        )
    )
)
print(
    (lambda state: sum(w == "#" for w in state.values()))(
        (find_steady := lambda updater, vals:
            new_vals if (new_vals := updater(vals)) == vals else find_steady(updater, new_vals)
        )(
            (lambda look: (
                lambda prev: {
                    (j, i): "#L"[v == "#"]
                        if v == "Lxxxx#####"[sum(look(prev, i, j, p, q) for q in [-1, 0, 1] for p in [-1, 0, 1])]
                        else v
                    for (j, i), v in prev.items()
                }
            ))(_look := lambda vals, x, y, dx, dy:
                not (dx == 0 and dy == 0) and (
                    (v := vals.get((y + dy, x + dx), 0)) == "#"
                    or (v == "." and _look(vals, x + dx, y + dy, dx, dy))
                )
            ),
            {(j, i): x for j, row in enumerate(INPUT.splitlines()) for i, x in enumerate(row)}
        )
    )
)
