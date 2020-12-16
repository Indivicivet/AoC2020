with open("input/q12.txt") as f:
    INPUT = f.read().splitlines()

print(
    sum(map(abs, (lambda pos: [
        (pos := (lambda x, y, dx, dy, m, a: {
            "N": (x, y + a, dx, dy), "S": (x, y - a, dx, dy), "E": (x + a, y, dx, dy), "W": (x - a, y, dx, dy),
            "F": (x + a * dx, y + a * dy, dx, dy),
            "R": (x, y, *{0: (dx, dy), 1: (dy, -dx), 2: (-dx, -dy), 3: (-dy, dx)}[a // 90]),
            "L": (x, y, *{0: (dx, dy), 3: (dy, -dx), 2: (-dx, -dy), 1: (-dy, dx)}[a // 90]),
        }[m])(*pos, m, a))
        for m, a in [(x[0], int(x[1:])) for x in INPUT]
    ])((0, 0, 1, 0))[-1][:2]))
)

print(
    sum(map(abs, (lambda pos: [
        (pos := (lambda x, y, dx, dy, m, a: {
            "N": (x, y, dx, dy + a), "S": (x, y, dx, dy - a), "E": (x, y, dx + a, dy), "W": (x, y, dx - a, dy),
            "F": (x + a * dx, y + a * dy, dx, dy),
            "R": (x, y, *{0: (dx, dy), 1: (dy, -dx), 2: (-dx, -dy), 3: (-dy, dx)}[a // 90]),
            "L": (x, y, *{0: (dx, dy), 3: (dy, -dx), 2: (-dx, -dy), 1: (-dy, dx)}[a // 90]),
        }[m])(*pos, m, a))
        for m, a in [(x[0], int(x[1:])) for x in INPUT]
    ])((0, 0, 10, 1))[-1][:2]))
)