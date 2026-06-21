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
