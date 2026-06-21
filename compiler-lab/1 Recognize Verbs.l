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

/* Input: I am going to school. 
Output:
Not Verb: I
Verb: am
Not Verb: going
Not Verb: to
Not Verb: school.
*/