%{
#include <stdio.h>
%}

PFLOAT \+?(([0-9]+\.[0-9]*)|(\.[0-9]+))
NFLOAT -(([0-9]+\.[0-9]*)|(\.[0-9]+))
PINT \+?[0-9]+
NINT -[0-9]+

%%

{NFLOAT}    { printf("Negative Float: %s\n", yytext); }
{PFLOAT}    { printf("Positive Float: %s\n", yytext); }
{NINT}      { printf("Negative Integer: %s\n", yytext); }
{PINT}      { printf("Positive Integer: %s\n", yytext); }
[A-Za-z_][A-Za-z0-9_]* { printf("Invalid: %s\n", yytext); }
[ \t\n]+    { }
.           { }

%%

int yywrap() {
    return 1;
}

int main() {
    yylex();
    return 0;
}

/* Input: 3.14 -0.001 2 .5 -7
Output:
Positive Float: 3.14
Negative Float: -0.001
Positive Integer: 2
Positive Float: .5
Negative Integer: -7
*/