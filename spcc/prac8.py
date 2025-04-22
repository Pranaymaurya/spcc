# from collections import defaultdict

# # Grammar
# prods = [
#     "S -> A B",
#     "A -> a | e",
#     "B -> b"
# ]

# # Parse grammar
# g = defaultdict(list)
# NT = set()
# for p in prods:
#     lhs, rhs = p.split("->")
#     lhs = lhs.strip()
#     NT.add(lhs)
#     for alt in rhs.strip().split("|"):
#         g[lhs].append(alt.strip())

# # Helpers
# first = defaultdict(set)
# follow = defaultdict(set)
# def is_term(x): return not x.isupper() and x != 'e'

# # FIRST computation
# def get_first(x):
#     if is_term(x): return {x}
#     if x == 'e': return {'e'}
#     if first[x]: return first[x]

#     for rule in g[x]:
#         for sym in rule.split():
#             f = get_first(sym)
#             first[x].update(f - {'e'})
#             if 'e' not in f: break
#         else:
#             first[x].add('e')
#     return first[x]

# # FIRST of string
# def first_of_str(symbols):
#     out = set()
#     for sym in symbols:
#         f = get_first(sym)
#         out.update(f - {'e'})
#         if 'e' not in f: break
#     else:
#         out.add('e')
#     return out

# # FOLLOW computation
# def compute_follow():
#     start = list(g.keys())[0]
#     follow[start].add('$')
#     changed = True
#     while changed:
#         changed = False
#         for head in g:
#             for rule in g[head]:
#                 symbols = rule.split()
#                 for i, sym in enumerate(symbols):
#                     if sym in NT:
#                         tail = symbols[i+1:]
#                         f = first_of_str(tail)
#                         before = len(follow[sym])
#                         follow[sym].update(f - {'e'})
#                         if 'e' in f or not tail:
#                             follow[sym].update(follow[head])
#                         if len(follow[sym]) > before:
#                             changed = True

# # Compute sets
# for nt in g: get_first(nt)
# compute_follow()

# # Output
# print("=== FOLLOW Sets ===")
# for nt in NT:
#     print(f"FOLLOW({nt}) = {{ {', '.join(sorted(follow[nt]))} }}")
grammar = {'S': ['AB'], 'A': ['a', 'ε'], 'B': ['b']}
first = {'A': ['a', 'ε'], 'B': ['b'], 'S': ['a', 'b']}
follow = {'S': ['$'], 'A': [], 'B': []}

for lhs in grammar:
    for rule in grammar[lhs]:
        for i in range(len(rule)-1):
            if rule[i] in grammar:
                follow[rule[i]].append(rule[i+1])
        if rule[-1] in grammar:
            follow[rule[-1]] += follow[lhs]

print("FOLLOW:", follow)
