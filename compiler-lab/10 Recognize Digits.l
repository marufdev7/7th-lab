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

/* Input: 1a 7 c3 4
Output:
Digit: 1
Not Digit: a
Digit: 7
Not Digit: c
Digit: 3
Digit: 4
*/