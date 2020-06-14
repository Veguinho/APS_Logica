# APS de uma linguagem de programação nova - Lógica da Computação - Insper 2020.1 - Rafael Vieira Rosenzvaig

## Linguagem de programação .vegs

### EXEMPLO:
```
{
	int function f1(int x, int y, int z){
		int counter = 0;
		loop while(counter < z){
			counter = counter + 1;
		}
		if((x > y) and (x > x+y) or (x > y-x)){
			print(x);
			return x;
		}
		else{
			print(y);
			return y;
		}
	}
	int a = 5;
	int b = 6;
	int c = 7;
	int return_val = f1(a,b,c);
	print(return_val);
}

```
### Características:
- Linguagem para facilitar o aprendizado de programação:
	- Similar à sintaxe do C;
	- Operações flexíveis como Python. Exemplo: print e operações entre tipos diferentes sem conversão;
	- Restringe o programador para seguir boas práticas. Exemplo: Declarar 2 vezes a mesma variável no mesmo contexto;
	- Da liberdade de operação com tipos diferentes;
	- Tipagem para funções;
	- Label "loop" para destacar loops;
- Tipos disponíveis:
	- int
	- bool
	- string
	- void (funções)
- Operadores disponíveis:
	- +
	- -
	- /
	- *
	- >
	- <
	- <=
	- >=
	- !=
	- ==

### Regras:
- Não se pode declarar a mesma variável mais de uma vez no mesmo contexto;
- Todo programa deve estar envolto em {};
- É possível realizar operações entre int e bool, e bool será convertido para int;
- Se uma função não retorna nada, nenhuma variável pode ser atribuída por ela;
- Não existe tipo nulo;

### EBNF linguagem VEGS (.vegs)
```
BLOCK = "{", {COMMAND}, "}";

COMMAND = ( λ | ASSIGNMENT | PRINT | ("return", RELEXPR) | FUNCTION), ";" | BLOCK | WHILE | IF | ( (FUNC_TYPE, "function")+, FUNCTION, BLOCK);

FUNCTION = IDENTIFIER, "(", ( (RELEXPR, {",", RELEXPR})+ )?, ")";

WHILE = "loop", "while", "(", RELEXPR, ")", BLOCK;

IF = "if", "(", RELEXPR, ")", BLOCK, ("else", BLOCK)?;

ASSIGNMENT = VAR_TYPE+, IDENTIFIER, "=", EXPRESSION;

PRINT = "print", "(", EXPRESSION, ")";

EXPRESSION = TERM, {("+" | "-" | "or"), TERM};

RELEXPR = EXPRESSION, {("==" | ">" | "<" | ">=" | "<=" | "!="), EXPRESSION};

TERM = FACTOR, { ("*" | "/" | "and"), FACTOR };

FACTOR = ("+" | "-" | "!"), FACTOR | NUMBER | "(", RELEXPR, ")" | IDENTIFIER | FUNCTION | STRING | BOOLEAN;

IDENTIFIER = LETTER, {LETTER | DIGIT | "_"};

NUMBER = DIGIT, {DIGIT};

STRING = """, (LETTER | DIGIT), {LETTER | DIGIT}, """;

BOOLEAN = "true" | "false";

LETTER = ( a | ... | z | A | ... | Z );

DIGIT = ( 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 0 );

FUNC_TYPE = "int", "string", "bool", "void";

VAR_TYPE = "int", "string", "bool";

NUMBER = DIGIT, {DIGIT};
```