# Assembly Program with Macro Definition
alp = [
    "MACRO",
    "INCR &A,&B",
    "LOAD &A",
    "ADD &B",
    "STORE &A",
    "MEND",
    "START",
    "INCR X,Y",
    "MOV A,B",
    "INCR P,Q",
    "END"
]

# Tables
mnt = {}      # Macro Name Table
mdt = []      # Macro Definition Table
ala = {}      # Argument List Array
exp1 = []     # Code without macro defs (for pass 2)

# --- PASS 1: Store Macro Info ---
i = 0
while i < len(alp):
    line = alp[i].strip()
    parts = line.split()

    if parts[0] == "MACRO":
        i += 1
        head = alp[i].strip().split()
        name = head[0]
        args = head[1].split(",")

        mnt[name] = len(mdt)
        ala[name] = args
        i += 1

        # Save macro body
        while alp[i].strip() != "MEND":
            body_line = alp[i]
            for idx, a in enumerate(args):
                body_line = body_line.replace(a, f"#{idx+1}")
            mdt.append(body_line)
            i += 1
        mdt.append("MEND")
    else:
        exp1.append(line)
    i += 1

# --- PASS 2: Expand Macros ---
final = []
for line in exp1:
    parts = line.strip().split()
    if not parts:
        continue

    name = parts[0]
    if name in mnt:
        args = parts[1].split(",")
        map_args = {f"#{i+1}": args[i] for i in range(len(args))}

        idx = mnt[name]
        while mdt[idx] != "MEND":
            l = mdt[idx]
            for k, v in map_args.items():
                l = l.replace(k, v)
            final.append(l)
            idx += 1
    else:
        final.append(line)

# --- OUTPUT ---
print("=== MNT ===")
for n, idx in mnt.items():
    print(f"{n} -> MDT {idx}")

print("\n=== MDT ===")
for i, l in enumerate(mdt):
    print(f"{i}: {l}")

print("\n=== ALA ===")
for n, args in ala.items():
    for i, a in enumerate(args):
        print(f"{n} : {a} -> #{i+1}")

print("\n=== Final Code ===")
for l in final:
    print(l)
