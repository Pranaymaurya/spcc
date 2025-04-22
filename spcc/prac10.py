import re

# Token patterns
regex_num = r'\b\d+(\.\d+)?\b'
regex_id = r'\b[a-zA-Z_]\w*\b'
regex_pre = r'^\s*#\s*(\w+)'

def lexical_analyzer(code):
    tokens = []
    for line in code.splitlines():
        if m := re.match(regex_pre, line):
            tokens.append(('Preprocessor', m.group(1)))
        tokens += [('Number', m.group()) for m in re.finditer(regex_num, line)]
        tokens += [('Identifier', m.group()) for m in re.finditer(regex_id, line)]
    return tokens

# Sample code
code = '''
#include <stdio.h>
#define MAX 100
int main() {
    int a = 10;
    float b = 20.5;
    a = a + 2;
    if (a > b) {
        return a;
    }
}
'''

# Analyze and print tokens
for t in lexical_analyzer(code):
    print(f"Type: {t[0]}, Value: {t[1]}")
