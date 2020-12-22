with open("input/q22.txt") as f:
    INPUT = f.read()

print(
    (lambda result: sum((i + 1) * v for i, v in enumerate(reversed(sum(result, [])))))(
        (take_turn := lambda decks: (
            decks if [] in (
                decks := (lambda p1, p2:
                    (p1[1:] + [p1[0], p2[0]], p2[1:]) if p1[0] > p2[0] else (p1[1:], p2[1:] + [p2[0], p1[0]])
                )(*decks)
            ) else take_turn(decks)
        ))([[int(x) for x in p.split("\n")[1:]] for p in INPUT.strip().split("\n\n")])
    )
)
print(
    (lambda result: sum((i + 1) * v for i, v in enumerate(reversed(sum(result, [])))))(
        (play_game := (lambda next_round:
            (lambda gamestate: next(
                gamestate[:2] for _ in range(10 ** 100) if [] in (gamestate := next_round(*gamestate))
            ))
        )(
            lambda p1, p2, prev_rounds: (p1, [], None) if (p1, p2) in prev_rounds else (
                (p1[1:] + [p1[0], p2[0]], p2[1:])
                if (
                    play_game((p1[1:1 + p1[0]], p2[1:1 + p2[0]], [[]]))[0]
                    if (len(p1) > p1[0] and len(p2) > p2[0])
                    else p1[0] > p2[0]
                ) else (p1[1:], p2[1:] + [p2[0], p1[0]])
            ) + (prev_rounds.__iadd__([(p1.copy(), p2.copy())]), )
        ))([[int(x) for x in p.split("\n")[1:]] for p in INPUT.strip().split("\n\n")] + [[]])
    )
)
