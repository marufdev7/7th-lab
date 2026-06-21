%{
#include <stdio.h>
%}

KEYWORD (auto|break|case|char|const|continue|default|do|double|else|enum|extern|float|for|goto|if|int|long|register|return|short|signed|sizeof|static|struct|switch|typedef|union|unsigned|void|volatile|while)

%%

{KEYWORD}                 { printf("Keyword: %s\n", yytext); }
[A-Za-z_][A-Za-z0-9_]*    { printf("Identifier: %s\n", yytext); }
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
