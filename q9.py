with open("input/q9.txt") as f:
    INPUT = f.read().splitlines()

print(
    (lambda in_vals: next(
        x for i, x in enumerate(in_vals[25:])
        if not any(x == a + b and a != b for a in in_vals[i:i + 25] for b in in_vals[i:i + 25])
    ))([int(line) for line in INPUT])
)
print(
    (lambda in_vals: 
        (lambda target: next(
            max(seq) + min(seq)
            for delta in range(2, len(in_vals)) for i in range(len(in_vals))
            if sum(seq := in_vals[i:i + delta]) == target
        ))(next(
            x for i, x in enumerate(in_vals[25:])
            if not any(x == a + b and a != b for a in in_vals[i:i + 25] for b in in_vals[i:i + 25])
        ))
    )([int(line) for line in INPUT])
)
