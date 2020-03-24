# APS de uma linguagem de programação nova - Lógica da Computação - Insper 2020.1 - Rafael Vieira Rosenzvaig

## Linguagem de programação .vgs

### EXEMPLO:
```
function f1(receive int x, int y, float z, string a; return int;)
{
	float counter = 0.0;
	loop while(counter < z){
		counter = counter + 0.1;
	}
	loop for(t < 100; start int t=0; step t=t+2;){
		counter = counter - 0.1;
	}
	if(x > y and x > x+y or x > y-x){
		return x;
	}
	else{
		return y;
	}
}
```
Regras:
if(k){…} não é válido. Deveria ser if(k==1){…}, por exemplo;

### EBNF linguagem VEGS (.vgs)
```
FUNCTIONDEF = "function", id, '(', "receive", VAR_DECL, {',', VAR_DECL}, ';', "return", "void"|TYPE, ';', ')', '{', {STMT}, '}';

VAR_DECL = TYPE, EXPRESSION;

STMT = VAR_DECL | WHILE_EXP | IF_EXP | FOR_EXP | EXPRESSION | RETURN_EXP, ';';

WHILE_EXP = "loop", "while", '(', COMP_EXPRESSION , {"and" | "or", COMP_EXPRESSION},')', '{', STMT*, '}';

IF_EXP = "if", '(', COMP_EXPRESSION , {"and" | "or", COMP_EXPRESSION},')', '{', {STMT}, '}';

FOR_EXP = "loop", "for", '(', COMP_EXPRESSION, {"and" | "or", COMP_EXPRESSION}, ';', "start", VAR_DECL, ';', "step", EXPRESSION, ';', ')', '{', {STMT}, '}';

EXPRESSION = (id, {'=', EXPRESSION|COMP_EXPRESSION|OPERATION})| OPERATION ;

COMP_EXPRESSION = id, COMP_OPERATOR, EXPRESSION;

RETURN_EXP = return, {id|NUMBER};

OPERATION = id|NUMBER, OPERATOR, id|NUMBER, {OPERATION};

COMP_OPERATOR = '==' | '>=' | '<=' | '!=' | '<'| '>';

OPERATOR = '+' | '-' | '*' | '/';

NUMBER = DIGIT, {DIGIT};

TYPE = "int"|"float"|"string";

DIGIT = 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9;
