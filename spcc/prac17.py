import re
symtab = {}
littab = []
loc = 0
inst = ['START', 'END', 'DS', 'DC', 'MOVER', 'MOVEM', 'ADD', 'SUB', 'JMP']

def pass1(code):
    global loc
    for line in code:
        parts = line.strip().split()
        if not parts: continue

        if parts[0] == 'START':
            loc = int(parts[1])
            continue

        label = None
        if parts[0] not in inst:
            label = parts[0]
            parts = parts[1:]

        op = parts[0]
        if len(parts) > 2 and "='" in parts[2]:
            lit = parts[2]
            if lit not in littab:
                littab.append(lit)

        if label:
            symtab[label] = loc

        loc += int(parts[1]) if op == 'DS' else 1

def show():
    print("SYMBOL TABLE:")
    for s, a in symtab.items():
        print(f"{s:<8} {a}")
    print("\nLITERAL TABLE:")
    for i, l in enumerate(littab):
        print(f"{l:<8} {loc + i}")  # Assuming literals are assigned addresses after the last LOC

# Sample input
code = [
    "START 100",
    "MOVER AREG, ='5'",
    "ADD BREG, ONE",
    "ONE DS 1",
    "LOOP SUB AREG, ='1'",
    "     JMP LOOP",
    "     END"
]

pass1(code)
show()
