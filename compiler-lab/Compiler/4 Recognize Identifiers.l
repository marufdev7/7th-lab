%{
#include <stdio.h>
%}

ID [A-Za-z_][A-Za-z0-9_]*

%%

{ID}              { printf("Identifier: %s\n", yytext); }
[0-9][A-Za-z0-9_]* { printf("Invalid Identifier: %s\n", yytext); }
[ \t\n]+          { }
.                 { printf("Invalid Symbol: %s\n", yytext); }

%%

int yywrap() {
    return 1;
}

int main() {
    yylex();
    return 0;
}
