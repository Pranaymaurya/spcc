# # Predefined Machine and Pseudo Opcode Tables
# MOT = {
#     "MOV": "01", "ADD": "02", "SUB": "03", "MUL": "04", "DIV": "05",
#     "JMP": "06", "CMP": "07", "LOAD": "08", "STORE": "09", "PRINT": "0A"
# }

# POT = ["START", "END", "DC", "DS", "ORG", "EQU"]

# # Sample ALP code (as a list of strings)
# alp_code = [
#     "START 100",
#     "LOOP MOV A, B",
#     "     ADD A, C",
#     "     SUB A, D",
#     "     PRINT A",
#     "     JMP LOOP",
#     "VALUE DC 5",
#     "SPACE DS 1",
#     "     END"
# ]

# location_counter = 0
# symbol_table = {}
# intermediate_code = []

# used_mot = set()
# used_pot = set()

# # -------- PASS 1 --------
# print("=== PASS 1 ===")
# for line in alp_code:
#     tokens = line.strip().split()

#     # Handle START
#     if tokens[0] == "START":
#         location_counter = int(tokens[1])
#         used_pot.add("START")
#         intermediate_code.append((location_counter, "START", tokens[1]))
#         continue

#     if tokens[0] == "END":
#         used_pot.add("END")
#         intermediate_code.append((location_counter, "END", ""))
#         break

#     label = ""
#     opcode = ""
#     operand = ""

#     if len(tokens) == 3:
#         label, opcode, operand = tokens
#         symbol_table[label] = location_counter
#     elif len(tokens) == 2:
#         opcode, operand = tokens
#     else:
#         opcode = tokens[0]

#     # Track MOT/POT usage
#     if opcode in MOT:
#         used_mot.add(opcode)
#     elif opcode in POT:
#         used_pot.add(opcode)

#     # Update location counter
#     if opcode == "DS":
#         location_counter += int(operand)
#     elif opcode == "DC":
#         location_counter += 1
#     else:
#         location_counter += 1

#     intermediate_code.append((location_counter - 1, opcode, operand))

# # -------- DISPLAY OUTPUTS --------

# print("\n=== MOT USED IN ALP ===")
# for op in used_mot:
#     print(f"{op} : {MOT[op]}")

# print("\n=== POT USED IN ALP ===")
# for op in used_pot:
#     print(op)

# print("\n=== SYMBOL TABLE ===")
# for sym, addr in symbol_table.items():
#     print(f"{sym} : {addr}")

# print("\n=== INTERMEDIATE CODE ===")
# for line in intermediate_code:
#     print(line)
# MOT = {"MOVER": "01", "ADD": "02", "STOP": "00"}
# POT = ["START", "END", "DS", "DC"]

# alp = ["START 100", "MOVER AREG, B", "ADD C", "STOP", "B DS 1", "C DC 5", "END"]
# for line in alp:
#     op = line.split()[0]
#     if op in MOT:
#         print(f"MOT: {op} -> {MOT[op]}")
#     elif op in POT:
#         print(f"POT: {op}")


alp_code = [
    "START 100",
    "MOVER AREG, =5",
    "ADD   BREG, X",
    "IF    A > B",
    "ENDIF",
    "PRINT A",
    "END"
]

mot = {"MOVER", "ADD", "SUB", "MOVEM", "MUL", "DIV"}
pot = {"START", "END", "IF", "ELSE", "ENDIF", "PRINT"}

mot_found = set()
pot_found = set()

# --- Pass 1 ---
for line in alp_code:
    parts = line.strip().split()
    for part in parts:
        if part in mot:
            mot_found.add(part)
        elif part in pot:
            pot_found.add(part)

# --- Output ---
print("MOT (Machine Opcodes) Found:")
for op in mot_found:
    print(op)

print("\nPOT (Pseudo Opcodes) Found:")
for op in pot_found:
    print(op)

