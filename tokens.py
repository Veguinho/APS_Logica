import ply.lex as lex
import ply.yacc as yacc
import sys
import os


tokens = [
    'ID',
    'NUMBER',
    'NORMSTRING',
    'PLUS',
    'MINUS',
    'DIVIDE',
    'MULTIPLY',
    'EQUALS',
    'COMPEQUALS',
    'LESSTHAN',
    'GREATERTHAN',
    'GREATERTHANOREQUALS',
    'LESSTHANOREQUALS',
    'NOTEQUALS',
    'NOT',
    'OPENPAR',
    'CLOSEPAR',
    'OPENBRACK',
    'CLOSEBRACK',
    'SEMICOL',
    'COMMA'
]

t_OPENPAR = r'\('
t_CLOSEPAR = r'\)'
t_OPENBRACK = r'\{'
t_CLOSEBRACK = r'\}'
t_SEMICOL = r'\;'
t_COMMA = r'\,'
t_PLUS = r'\+'
t_MINUS = r'\-'
t_MULTIPLY = r'\*'
t_DIVIDE = r'\/'
t_EQUALS = r'\='
t_COMPEQUALS = r'\=\='
t_LESSTHAN = r'\<'
t_GREATERTHAN = r'\>'
t_GREATERTHANOREQUALS = r'\>\='
t_LESSTHANOREQUALS = r'\<\='
t_NOTEQUALS = r'\!\='
t_NOT = r'\!'

reserved = {
    'if' : 'IF',
    'else' : 'ELSE',
    'while' : 'WHILE',
    'or' : 'OR',
    'and' : 'AND',
    'loop' : 'LOOP',
    'function' : 'FUNCTION',
    'return' : 'RETURN',
    'int' : 'INT',
    'bool' : 'BOOL',
    'print' : 'PRINT',
    'string' : 'STRING',
    'void' : 'VOID',
    'true' : 'TRUE',
    'false' : 'FALSE'
}

tokens += reserved.values()

t_ignore = r' '

t_ignore_COMMENT = r'\#.*'

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = 'ID'
    if t.value in reserved:
        t.type = reserved[t.value]
    return t

def t_NORMSTRING(t):
    r'\"([^\\\n]|(\\.))*?\"'
    t.value = str(t.value)
    return t

def t_skipline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_error(t):
    print("Invalid character")
    t.lexer.skip(1)

lexer = lex.lex()

def p_program(p):
    """
    program : commandLoop
    """
    p[0] = p[1]
    print(p[0])
    print("Parsing complete. Lexical and syntatic analysis succeeded!")

def p_commandLoop(p):
    """
    commandLoop : command commandLoop
                | empty
    """
    if len(p)>2:
        if p[2] != None:
            p[0] = (p[1],p[2])
        else:
            p[0] = p[1]

def p_block(p):
    '''
    block : OPENBRACK command CLOSEBRACK
          | OPENBRACK CLOSEBRACK
    '''
    if len(p) > 3:
        p[0] = p[2]

def p_command(p):
    '''
    command : function SEMICOL
            | RETURN relexpr SEMICOL
            | print SEMICOL
            | assignment SEMICOL
            | empty SEMICOL
            | block
            | while
            | if
            | INT FUNCTION function block
            | STRING FUNCTION function block
            | BOOL FUNCTION function block
            | VOID FUNCTION function block
    '''

    if len(p) > 4:
        p[0] = (p[3],p[4])
        
    elif p[1] == 'return':
        p[0] = (p[1],p[2])
    else:
        p[0] = p[1]   
    
def p_function(p):
    '''
    function : ID OPENPAR INT ID CLOSEPAR
             | ID OPENPAR INT ID moreArg CLOSEPAR
             | ID OPENPAR STRING ID CLOSEPAR
             | ID OPENPAR STRING ID moreArg CLOSEPAR
             | ID OPENPAR BOOL ID CLOSEPAR
             | ID OPENPAR BOOL ID moreArg CLOSEPAR
             | ID OPENPAR relexpr CLOSEPAR
             | ID OPENPAR relexpr moreArg CLOSEPAR
             | ID OPENPAR CLOSEPAR
    '''
    if len(p) == 7:
        p[0] = (p[1],p[4],p[5])
    elif len(p) == 6:
        if p[3] == 'int' or p[3] == 'string' or p[3] == 'bool':
            p[0] = (p[1],p[4])
        else:
            p[0] = (p[1],p[3],p[4])
    elif len(p) == 5:
        p[0] = (p[1],p[3])
    else:
        p[0] = p[1]

def p_moreArg(p):
    '''
    moreArg : COMMA relexpr
            | COMMA relexpr moreArg
            | COMMA INT ID
            | COMMA INT ID moreArg
            | COMMA STRING ID
            | COMMA STRING ID moreArg
            | COMMA BOOL ID
            | COMMA BOOL ID moreArg
    '''
    if len(p) == 5:
        p[0] = (p[3],p[4])
    elif len(p) == 4:
        if p[2] == 'int' or p[2] == 'string' or p[2] == 'bool':
            p[0] = p[3]
        else:
            p[0] = (p[2],p[3])
    else:
        p[0] = p[0] = p[2]

def p_assignment(p):
    '''
    assignment : ID EQUALS expression
               | INT ID EQUALS expression
               | STRING ID EQUALS expression
    '''
    if len(p) > 4:
        p[0] = (p[3], p[2], p[4])
    else:
        p[0] = (p[2], p[1], p[3])

def p_while(p):
    '''
    while : LOOP WHILE OPENPAR relexpr CLOSEPAR block
    '''
    p[0] = (p[2], p[4], p[6])

def p_if(p):
    '''
    if : IF OPENPAR relexpr CLOSEPAR block
       | IF OPENPAR relexpr CLOSEPAR block ELSE block
    '''
    if len(p) > 6:
        p[0] = (p[1],p[3],p[5],p[7])
    else:
        p[0] = (p[1],p[3],p[5])

def p_print(p):
    '''
    print : PRINT OPENPAR expression CLOSEPAR
    '''
    p[0] = (p[1],p[3])

def p_expression(p):
    '''
    expression : term
               | term OR term
               | term PLUS term
               | term MINUS term
    '''
    if len(p) > 2:
        p[0] = (p[2],p[1],p[3])
    else:
        p[0] = p[1]

def p_relexpr(p):
    '''
    relexpr : expression
            | expression COMPEQUALS expression
            | expression LESSTHAN expression
            | expression GREATERTHAN expression
            | expression GREATERTHANOREQUALS expression
            | expression LESSTHANOREQUALS expression
            | expression NOTEQUALS expression
    '''
    if len(p) > 2:
        p[0] = (p[2],p[1],p[3])
    else:
        p[0] = p[1]

def p_term(p):
    '''
    term : factor
         | factor MULTIPLY factor
         | factor DIVIDE factor
         | factor AND factor
    '''
    if len(p) > 2:
        p[0] = (p[2],p[1],p[3])
    else:
        p[0] = p[1]

def p_factor(p):
    '''
    factor : PLUS factor
            | MINUS factor
            | NOT factor
            | NUMBER 
            | TRUE
            | FALSE
            | OPENPAR relexpr CLOSEPAR
            | ID
            | NORMSTRING
            | function
    '''
    if len(p) == 3:
        p[0] = (p[1],p[2])
    elif len(p) == 2:
        if p[1] is int:
            p[0] = int(p[1])
        else:
            p[0] = p[1]
    else:
        p[0] = p[2]

def p_empty(p):
    '''
    empty : 
    '''
    p[0] = None

def p_error(p):
    print("Syntax Error!")

parser = yacc.yacc()

code_in = '''
int function sominha(int a, int b){
    return a+b;
} 
int a = 0;
int b = 5;   
int c = sominha(a,b);
if(c>10){
    print(a);
}
'''
#variable_list = SymbolTable()
#p.Evaluate(variable_list)

#def run(p):
    # if type(p) == tuple:

    # else:
    #     return p
    
file_name = sys.argv[1]
if os.path.splitext(file_name)[1] != ".vegs":
    raise Exception("Invalid file. You must use a .vegs file")
else:
    with open(file_name, "r") as input_file:
        parser.parse(input_file.read(), lexer=lexer)