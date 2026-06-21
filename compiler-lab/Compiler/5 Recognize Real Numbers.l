%{
#include <stdio.h>
%}

REAL [+-]?((([0-9]+\.[0-9]+)|([0-9]+\.)|(\.[0-9]+))([eE][+-]?[0-9]+)?|([0-9]+[eE][+-]?[0-9]+))

%%

{REAL}                    { printf("Real Number: %s\n", yytext); }
[+-]?[0-9]+               { printf("Not Real Number: %s\n", yytext); }
[A-Za-z_][A-Za-z0-9_]*    { printf("Invalid: %s\n", yytext); }
[ \t\n]+                  { }
.                         { }

%%

int yywrap() {
    return 1;
}

int main() {
    yylex();
    return 0;
}
