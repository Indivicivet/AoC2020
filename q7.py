with open("input/q7.txt") as f:
    INPUT = f.read().splitlines()

print(
    (lambda tree: sum(
        1 for bag in tree
        if (above_gold := lambda _bag: ("shiny gold bag" in [b for _, b in tree[_bag]]) or any(above_gold(b) for _, b in tree[_bag]))(bag)
    ))
    ({
        bag: [b.split(" ", 1) for b in inside if b]
        for bag, inside in [
            [w.split(", ")[i and slice(None)] for i, w in enumerate(line.replace("bags", "bag").replace(".", "").replace("no other bag", "").split(" contain "))]
            for line in INPUT
        ]
    })
)
print(
    (lambda tree: (tote := lambda target: sum(int(n_str) * (1 + tote(inner)) for n_str, inner in tree[target]))("shiny gold bag"))
    ({
        bag: [b.split(" ", 1) for b in inside if b]
        for bag, inside in [
            [w.split(", ")[i and slice(None)] for i, w in enumerate(line.replace("bags", "bag").replace(".", "").replace("no other bag", "").split(" contain "))]
            for line in INPUT
        ]
    })
)
