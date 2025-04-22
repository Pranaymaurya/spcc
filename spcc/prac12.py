import re

def const_propagation(code):
    consts, result = {}, []
    for line in code:
        if '=' in line:
            var, expr = map(str.strip, line.split('='))
            if re.fullmatch(r'-?\d+', expr):
                consts[var] = expr
            for k, v in consts.items():
                expr = expr.replace(k, v)
            result.append(f"{var} = {expr}")
        else:
            result.append(line)
    return result

def dead_code_elim(code):
    used, assigned = set(), {}
    for line in code:
        if '=' in line:
            var, expr = map(str.strip, line.split('='))
            assigned[var] = line
            used.update(re.findall(r'\b[a-zA-Z_]\w*\b', expr))
    return [assigned[v] for v in assigned if v in used]

# Sample code
code = [
    "x = 5", "y = 10", "z = x + y", "a = 0", "b = a + 1",
    "c = b + 2", "d = z + 3", "x = x + 5", "z = 100", "e = z + 50 ","a=b+2"
]

# Apply optimizations
after_cp = const_propagation(code)
final = dead_code_elim(after_cp)

print(code)
# Output
print("Optimized Code:")
for line in final:
    print(line)
