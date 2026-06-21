%{
#include <stdio.h>
%}

%%

"++"|"--" {
    printf("Increment/Decrement Operator: %s\n", yytext);
}

"=="|"!="|"<="|">="|"<"|">" {
    printf("Relational Operator: %s\n", yytext);
}

"&&"|"||"|"!" {
    printf("Logical Operator: %s\n", yytext);
}

"="|"+="|"-="|"*="|"/="|"%=" {
    printf("Assignment Operator: %s\n", yytext);
}

"<<"|">>"|"&"|"|"|"^"|"~" {
    printf("Bitwise Operator: %s\n", yytext);
}

"+"|"-"|"*"|"/"|"%" {
    printf("Arithmetic Operator: %s\n", yytext);
}

[A-Za-z_][A-Za-z0-9_]* { printf("Not Operator: %s\n", yytext); }
[ \t\n]+    { }
.           { printf("Not Operator: %s\n", yytext); }

%%

int yywrap() {
    return 1;
}

int main() {
    yylex();
    return 0;
}

/* Input: a++ b-- c == d && e || f !g = h += i
Output:
Increment/Decrement Operator: ++
Increment/Decrement Operator: --
Relational Operator: ==
Logical Operator: &&
Logical Operator: ||
Logical Operator: !
Assignment Operator: =
Assignment Operator: +=
*/