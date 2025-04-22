import re

# Define token patterns
keywords = {'if', 'else', 'while', 'for', 'return', 'int', 'float', 'char'}
regex = rf"({'|'.join(keywords)})|([a-zA-Z_]\w*)|([+\-*/=(){{}}\[\];,])"

# Lexical analyzer function
def lexical_analyzer(code):
    tokens = []
    for match in re.finditer(regex, code):
        kind = 'Keyword' if match.group(1) else 'Identifier' if match.group(2) else 'Symbol'
        tokens.append((kind, match.group(0)))
    return tokens

# Sample code
code = '''
int main() {
    int a = 10;
    float b = 20.5;
    if (a > b) {
        return a;
    }
    while (a < b) {
        a = a + 1;
    }
}
'''

# Run analyzer
for t in lexical_analyzer(code):
    print(f"Type: {t[0]}, Value: {t[1]}")
