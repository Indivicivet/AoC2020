from aocd import data
INPUT = data.splitlines()

print(
    (lambda ds: (sum(d == 1 for d in ds)) * (1 + sum(d == 3 for d in ds)))(
        (lambda srtd: [y - x for x, y in zip(srtd, srtd[1:])])(
            [0] + sorted(int(x) for x in INPUT)
        )
    )
)
print(
    (lambda s: 2 ** s.count("3113") * 4 ** s.count("31113") * 7 ** s.count("311113"))(
        (lambda srtd: 
            "3" + "".join(str(y - x) for x, y in zip(srtd, srtd[1:])).replace("3", "33") + "3"
        )([0] + sorted(int(x) for x in INPUT))
    )
)
