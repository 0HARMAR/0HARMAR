%{
#include "calculate.tab.h"
%}

%%
[0-9]+  { yylval = atoi(yytext); return NUMBER; }
[ \t]   ;
\n      return '\n';
.       return yytext[0];
%%

int yywrap(void) {
    return 1;
}
