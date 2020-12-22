with open("input/q21.txt") as f:
    INPUT = f.read().splitlines()

print(
    (lambda data: (lambda mapping: sum((x not in mapping.values()) for xs, _ in data for x in xs))(
        (lambda allergens: [allergens := (lambda prev: next(
            {**{
                a2: ([x for x in xs2 if x != xs[0]] if a != a2 else xs) if isinstance(xs2, list) else xs2
                for a2, xs2 in prev.items() if a != a2
            }, a: xs[0]}
            for a, xs in prev.items() if len(xs) == 1
        ))(allergens) for _ in range(len(allergens))][-1])({
            a: [
                x for x in {x for xs, _ in data for x in xs}
                if all(x in xs for (xs, alz) in data if a in alz)
            ] for _, alz in data for a in alz
        })
    ))([(line.split(" (")[0].split(" "), line.split("contains ")[1][:-1].split(", ")) for line in INPUT])
)

print(
    (lambda data: (lambda mapping: ",".join(x for _, x in sorted(mapping.items())))(
        (lambda allergens: [allergens := (lambda prev: next(
            {**{
                a2: ([x for x in xs2 if x != xs[0]] if a != a2 else xs) if isinstance(xs2, list) else xs2
                for a2, xs2 in prev.items() if a != a2
            }, a: xs[0]}
            for a, xs in prev.items() if len(xs) == 1
        ))(allergens) for _ in range(len(allergens))][-1])({
            a: [
                x for x in {x for xs, _ in data for x in xs}
                if all(x in xs for (xs, alz) in data if a in alz)
            ] for _, alz in data for a in alz
        })
    ))([(line.split(" (")[0].split(" "), line.split("contains ")[1][:-1].split(", ")) for line in INPUT])
)
