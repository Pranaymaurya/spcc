import re

# Define patterns
keywords = {'if', 'else', 'while', 'for', 'return', 'int', 'float', 'char'}
symbol_pattern = r"[+\-*/=(){}\[\];,<>]"
number_pattern = r"\b\d+(\.\d+)?\b"
preprocessor_pattern = r"#\w+"
identifier_pattern = r"\b[a-zA-Z_]\w*\b"

# Combined regex
combined_pattern = rf"({preprocessor_pattern})|({number_pattern})|({symbol_pattern})|({identifier_pattern})"

# Analyzer function
def lexical_analyzer(code):
    tokens = []
    for match in re.finditer(combined_pattern, code):
        # print(match)
        token = match.group(0)
        if re.fullmatch(preprocessor_pattern, token):
            kind = 'Preprocessor'
        elif token in keywords:
            kind = 'Keyword'
        elif re.fullmatch(number_pattern, token):
            kind = 'Number'
        elif re.fullmatch(symbol_pattern, token):
            kind = 'Symbol'
        else:
            kind = 'Identifier'
        tokens.append((kind, token))
    return tokens

# Sample code
code = '''
#include <stdio.h>
#define PI 3.14

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
    print(f"Type: {t[0]:<12} Value: {t[1]}")
