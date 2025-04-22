# Macro Name Table
mnt = {"INCR": 0}

# Macro Definition Table
mdt = [
    "LOAD #1",
    "ADD #2",
    "STORE #1",
    "MEND"
]

# Assembly program
alp = [
    "START",
    "INCR A,B",
    "MOV C,D",
    "INCR X,Y",
    "END"
]

# Expanded code output
exp = []

# ----- PASS 2: Macro Expansion -----
for line in alp:
    tok = line.strip().split()
    if not tok:
        continue

    name = tok[0]
    args = tok[1].split(",") if len(tok) > 1 else []
    if name in mnt:
        index = mnt[name]
        ala = {f"#{i+1}": args[i] for i in range(len(args))}

        while mdt[index] != "MEND":
            l = mdt[index]
            for k, v in ala.items():
                l = l.replace(k, v)
            exp.append(l)
            index += 1
    else:
        exp.append(line)

# ----- Output -----
# print("=== MNT ===")
# for n, i in mnt.items():
#     print(f"{n} -> {i}")

# print("\n=== MDT ===")
# for i, l in enumerate(mdt):
#     print(f"{i} : {l}")

print("\n=== Expanded Code ===")
for l in exp:
    print(l)
