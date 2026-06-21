%{
#include <stdio.h>
%}

INTEGER [0-9]+

%%

{INTEGER}                 { printf("Integer: %s\n", yytext); }
[A-Za-z_][A-Za-z0-9_]*    { printf("Not Integer: %s\n", yytext); }
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

/* Input: 123 abc 456
Output:
Integer: 123
Not Integer: abc
Integer: 456
*/