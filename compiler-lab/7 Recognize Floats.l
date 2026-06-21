%{
#include <stdio.h>
%}

FLOAT [+-]?(([0-9]+\.[0-9]*)|(\.[0-9]+))

%%

{FLOAT}                   { printf("Float: %s\n", yytext); }
[+-]?[0-9]+               { printf("Not Float: %s\n", yytext); }
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

/* Input: 3.14 7 -0.01 2
Output:
Float: 3.14
Float: 7
Float: -0.01
Not Float: 2
*/