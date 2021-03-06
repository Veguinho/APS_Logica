# APS de uma linguagem de programação nova - Lógica da Computação - Insper 2020.1 - Rafael Vieira Rosenzvaig

## Linguagem de programação .vegs

### Compilação
1 - Crie um programa válido e salve com a extensão .vegs 

2 - Rode com python3 o arquivo main.py e passe como entrada o arquivo .vegs: ```python main.py entrada.vegs```

3 - Se passar na compilação, você verá o resultado de seu programa no terminal 

### Exemplo de código:
```
{
	int function f1(int x, int y, int z){
		int counter = 0;
		loop while(counter < z){
			counter = counter + 1;
		}
		if(x > y){
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
	int returnval = f1(a,b,c);
	print(returnval);
}

```
### Características:
- Linguagem para facilitar o aprendizado de programação:
	- É similar à sintaxe do C;
	- Possúi operações flexíveis como Python. Exemplo: print e operações entre tipos diferentes sem conversão;
	- Restringe o programador para seguir boas práticas. Exemplo: Não é permitido declarar 2 vezes a mesma variável no mesmo contexto;
	- Da liberdade de operação com tipos diferentes;
	- Fornece tipagem para funções;
	- Usa a label "loop" para destacar loops;
- Tipos disponíveis:
	- int
	- bool
	- string
	- void (funções)
- Operadores disponíveis:
	- "+"
	- "-"
	- "/"
	- "*"
	- ">"
	- "<"
	- "<="
	- ">="
	- "!="
	- "=="

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
