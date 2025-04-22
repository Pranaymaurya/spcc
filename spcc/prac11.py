import re

def simplify(expr):
    expr = re.sub(r'(\w+) \* 1', r'\1', expr)
    expr = re.sub(r'(\w+) \+ 0', r'\1', expr)
    expr = re.sub(r'(\w+) - \1', '0', expr)
    expr = re.sub(r'\w+ \* 0', '0', expr)
    return expr

def eliminate_cse(lines):
    seen, result, count = {}, [], 1
    for line in lines:
        var, expr = map(str.strip, line.split('='))
        if expr in seen:
            result.append(f"{var} = {seen[expr]}")
        else:
            temp = f"t{count}"
            seen[expr] = temp
            result.append(f"{temp} = {expr}")
            count += 1
    return result

# Input code
code = [
    "x = a * b + a * b",
    "y = a * c + d",
    "z = a * b + a * b",
    "w = x + 0",
    "v = y * 1"
]

# Optimization pipeline
simplified = [simplify(line) for line in code]
optimized = eliminate_cse(simplified)

# Output
print("Optimized Code:")
for line in optimized:
    print(line)
