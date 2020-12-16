with open("input/q13.txt") as f:
    INPUT = f.read().splitlines()

print(
    (lambda min_time, buses: 
        (lambda time, x: (time - min_time) * x)(*min(((min_time // x + 1) * x, x) for x in buses))
    )(int(INPUT[0]), [int(x) for x in INPUT[1].split(",") if x != "x"])
)
print(
    (lambda binary_op: (reduced := lambda x, y=None, *rest:
        x if y is None else reduced(binary_op(*x, *y), *rest)
    ))(
        lambda a, A, b, B: next((i * A + a, A * B) for i in range(B) if (i * A + a - b) % B == 0)
    )(*((-j, int(x)) for j, x in enumerate(INPUT[1].split(",")) if x != "x"))[0]
)
