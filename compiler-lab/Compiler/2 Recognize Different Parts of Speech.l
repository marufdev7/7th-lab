%{
#include <stdio.h>
%}

VERB (is|am|are|were|go)
ADVERB (very|simply|quickly|gently)
PREP (to|from|behind|between)
CONJ (if|then)

%%

{VERB}      { printf("Verb: %s\n", yytext); }
{ADVERB}    { printf("Adverb: %s\n", yytext); }
{PREP}      { printf("Preposition: %s\n", yytext); }
{CONJ}      { printf("Conjunction: %s\n", yytext); }
[A-Za-z]+   { printf("Unknown: %s\n", yytext); }
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
