%{
    #include <stdio.h>
    #include <string.h>
    
    int isKeyword(char *word) {
        char *keywords[] = { "int", "float", "char", "if", "else", "while", "for", "return", "void" };
        for (int i = 0; i < 9; i++) {
            if (strcmp(word, keywords[i]) == 0) {
                return 1;
            }
        }
        return 0;
    }
    %}
    
    %%
    
    [ \t\n]+               ; // Ignore whitespace
    
    "=="|"!="|"<="|">="|"="|"+"|"-"|"*"|"/"    { printf("Operator: %s\n", yytext); }
    
    "(" | ")" | ";" | "," | "{" | "}"         { printf("Delimiter: %s\n", yytext); }
    
    [0-9]+(\.[0-9]+)?      { printf("Number: %s\n", yytext); }
    
    [a-zA-Z_][a-zA-Z0-9_]* {
                            if (isKeyword(yytext))
                                printf("Keyword: %s\n", yytext);
                            else
                                printf("Identifier: %s\n", yytext);
                          }
    
    .                      { printf("Unknown symbol: %s\n", yytext); }
    
    %%
    
    int main(int argc, char **argv) {
        printf("LEXICAL ANALYSIS STARTED\n");
        yylex();
        printf("LEXICAL ANALYSIS COMPLETED\n");
        return 0;
    }
    
    int yywrap() {
        return 1;
    }
    