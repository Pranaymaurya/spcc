# from collections import defaultdict

# # Simple Grammar
# prods = [
#     "S -> A B",
#     "A -> a | e",
#     "B -> b"
# ]

# # Grammar dict
# g = defaultdict(list)
# for p in prods:
#     lhs, rhs = p.split("->")
#     lhs = lhs.strip()
#     for alt in rhs.strip().split("|"):
#         g[lhs].append(alt.strip())
# print(g)
# # FIRST sets
# first = defaultdict(set)

# def is_term(x):
#     return not x.isupper() and x != 'e'

# def get_first(x):
#     if is_term(x) or x == 'e':
#         return {x}
#     if first[x]:
#         return first[x]

#     for rule in g[x]:
#         parts = rule.split()
#         for sym in parts:
#             f = get_first(sym)
#             first[x].update(f - {'e'})
#             if 'e' not in f:
#                 break
#         else:
#             first[x].add('e')
#     return first[x]

# # Compute FIRST sets
# for nt in g:
#     get_first(nt)

# # Output
# print("=== FIRST Sets ===")
# for nt, f_set in first.items():
#     print(f"FIRST({nt}) = {{ {', '.join(sorted(f_set))} }}")
grammar = {'E': ['TA'], 'A': ['+TA', 'ε'], 'T': ['FB'], 'B': ['*FB', 'ε'], 'F': ['(E)', 'id'],"L":[]}
first = {}

def find_first(symbol):
    if symbol not in grammar:
        return [symbol]
    result = []
    for prod in grammar[symbol]:
        if prod[0].isupper():
            result += find_first(prod[0])
        else:
            result.append(prod[0])
    return list(set(result))

for nonterm in grammar:
    first[nonterm] = find_first(nonterm)

print("FIRST:", first)
