from aocd import data
INPUT = data.splitlines()

print(sum(
    (lambda *mem_mask:
        [mem_mask := (lambda mem, mask, instr:
            (mem, instr[7:]) if instr[:4] == "mask" else (
                {**mem, int(instr.split("]")[0].split("[")[1]):
                    sum(2 ** i for i, v in enumerate(reversed(mask)) if v == "1")
                    | (int(instr.split(" = ")[1]) & sum(2**i for i, v in enumerate(reversed(mask)) if v == "X"))
                }, mask
            )
        )(*mem_mask, instr) for instr in INPUT][-1]
    )({}, "0" * 36)[0].values()
))  
print(sum(
    (lambda *mem_mask, subaddresses:
        [mem_mask := (lambda mem, mask, instr:
            (mem, instr[7:]) if instr[:4] == "mask" else (
                {**mem, **{int("".join(addr_bits), 2):
                    int(instr.split(" = ")[1]) for addr_bits in subaddresses([
                        "1" if v_mask == "1" else v_base
                        for v_mask, v_base in zip(mask, list(f'{int(instr.split("]")[0].split("[")[1]):036b}'))
                    ], mask)
                }}, mask
            )
        )(*mem_mask, instr) for instr in INPUT][-1]
    )({}, "0" * 36, subaddresses=(
        _subs := lambda base, mask: [base] if "X" not in mask else (
            lambda replace_at_x: sum((_subs(replace_at_x(base, c), replace_at_x(mask, "0")) for c in "01"), [])
        )(lambda orig, new_val: [new_val if i == mask.index("X") else v for i, v in enumerate(orig)])
    ))[0].values()
))
