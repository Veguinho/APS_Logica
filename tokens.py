import ply.lex as lex
import ply.yacc as yacc
import sys

tokens = [
    'INT',
    'FLOAT',
    'ID',
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
    'OPENPAR',
    'CLOSEPAR',
    'OPENBRACK',
    'CLOSEBRACK',
    'SEMICOL'
]

t_OPENPAR = r'\('
t_CLOSEPAR = r'\)'
t_OPENBRACK = r'\{'
t_CLOSEBRACK = r'\}'
t_SEMICOL = r'\;'
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

reserved = {
    'if' : 'IF',
    'else' : 'ELSE',
    'while' : 'WHILE',
    'or' : 'OR',
    'and' : 'AND',
    'loop' : 'LOOP',
    'function' : 'FUNCTION'
}

tokens += reserved.values()

t_ignore = r' '

def t_INT(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_FLOAT(t):
    r'\d+\.\d+'
    t.value = float(t.value)
    return t

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = 'ID'
    if t.value in reserved:
        t.type = reserved[t.value]
    return t

def t_error(t):
    print("Invalid character")
    t.lexer.skip(1)

lexer = lex.lex()

precedence = (
    ('left', 'PLUS', 'MINUS'),
    ('left', 'MULTIPLY', 'DIVIDE')
)

def p_operation(p):
    '''
    operation : expression
              | assignment
              | empty
    '''
    print(run(p[1]))

def p_assignment(p):
    '''
    assignment : ID EQUALS expression
    '''
    p[0] = ('=', p[1], p[3])

def p_expression(p):
    '''
    expression : expression MULTIPLY expression
               | expression DIVIDE expression
               | expression PLUS expression
               | expression MINUS expression
    '''
    p[0] = (p[2], p[1], p[3])

def p_expression_int_float(p):
    '''
    expression : INT
               | FLOAT
    '''
    p[0] = p[1]

def p_expression_var(p):
    '''
    expression : ID
    '''
    p[0] = ('var', p[1])

def p_empty(p):
    '''
    empty : 
    '''
    p[0] = None

def p_error(p):
    print("Syntax Error!")

parser = yacc.yacc()

def run(p):
    if type(p) == tuple:
        if p[0] == '+':
            return run(p[1]) + run(p[2])
        elif p[0] == '-':
            return run(p[1]) - run(p[2])
        elif p[0] == '*':
            return run(p[1]) * run(p[2])
        elif p[0] == '/':
            return run(p[1]) / run(p[2])
    else:
        return p

while True:
    try:
        s = input('')
    except EOFError:
        break
    parser.parse(s)
    