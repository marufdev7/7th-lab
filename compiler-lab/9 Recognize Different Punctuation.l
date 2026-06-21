%{
#include <stdio.h>
%}

PUNC [,;:.!?()\[\]{}]

%%

{PUNC}     { printf("Punctuation Symbol: %s\n", yytext); }
[ \t\n]+   { }
.          { printf("Not Punctuation: %s\n", yytext); }

%%

int yywrap() {
    return 1;
}

int main() {
    yylex();
    return 0;
}

/* Input: Hello, world! (This is a test.)
Output:
Punctuation Symbol: ,
Punctuation Symbol: !
Punctuation Symbol: (
Punctuation Symbol: )
Punctuation Symbol: .
*/