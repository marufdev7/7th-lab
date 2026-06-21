%{
#include <stdio.h>
%}

%%

[0-9]      { printf("Digit: %s\n", yytext); }
[A-Za-z]   { printf("Not Digit: %s\n", yytext); }
[ \t\n]+   { }
.          { printf("Not Digit: %s\n", yytext); }

%%

int yywrap() {
    return 1;
}

int main() {
    yylex();
    return 0;
}
