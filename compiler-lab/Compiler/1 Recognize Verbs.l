%{
#include <stdio.h>
%}

VERB (is|am|are|were|was|be|being|been|do|does|did|will|would|should|can|could|has|have|had|go)

%%

{VERB}      { printf("Verb: %s\n", yytext); }
[A-Za-z]+   { printf("Not Verb: %s\n", yytext); }
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
