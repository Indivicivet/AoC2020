from aocd import data
INPUT = data.splitlines()

print(
    (lambda cls: sum(eval("".join(
        t if t in "()+" else "-" if t == "*" else f"{cls.__name__}({t})"
        for t in line.replace("(", "( ").replace(")", " )").split(" ")
    )) for line in INPUT))(
        cls := type("cls", (int,), {"__add__": lambda s, o: cls(int(s) + o), "__sub__": lambda s, o: cls(int(s) * o)})
    )
)
print(
    (lambda cls: sum(eval("".join(
        {"(": "(", ")": ")", "+": "*", "*": "+"}.get(t, f"{cls.__name__}({t})")
        for t in line.replace("(", "( ").replace(")", " )").split(" ")
    )) for line in INPUT))(
        cls := type("cls", (int,), {"__add__": lambda s, o: cls(int(s) * o), "__mul__": lambda s, o: cls(int(s) + o)})
    )
)
