import sys
import re
import os
from pydoc import locate

class Token:
    def __init__(self, token_type, value):
        self.token_type = token_type
        self.value = value

class Tokenizer:
    def __init__(self, origin):
        self.origin = origin
        self.position = 0
        self.actual = Token(int, 0)
        self.selectNext()

    def selectNext(self):
        key_words = ['print', 'if', 'else','while', 'or', 'and', 'return', 'function', 'int', 'string', 'void', 'bool', 'loop']
        num = ''
        string = ''
        while self.position < len(self.origin) and self.origin[self.position] == ' ':
            self.position += 1
        if self.position == len(self.origin):
            self.actual = Token(type(''), 'eof')
        elif self.origin[self.position] == '+':
            self.actual = Token(type('+'), 'plus')
            self.position += 1
        elif self.origin[self.position] == '-':
            self.actual = Token(type('-'), 'minus')
            self.position += 1
        elif self.origin[self.position] == '*':
            self.actual = Token(type('*'), 'mult')
            self.position += 1
        elif self.origin[self.position] == '/':
            self.actual = Token(type('/'), 'div')
            self.position += 1
        elif self.origin[self.position] == '(':
            self.actual = Token(type(')'), 'open_p')
            self.position += 1
        elif self.origin[self.position] == ')':
            self.actual = Token(type('('), 'close_p')
            self.position += 1
        elif self.origin[self.position] == '{':
            self.actual = Token(type('{'), 'open_b')
            self.position += 1
        elif self.origin[self.position] == '}':
            self.actual = Token(type('}'), 'close_b')
            self.position += 1
        elif self.origin[self.position] == ';':
            self.actual = Token(type(';'), 'semi_c')
            self.position += 1
        elif self.origin[self.position] == ',':
            self.actual = Token(type(','), 'comma')
            self.position += 1
        elif self.origin[self.position] == '>':
            if self.position < len(self.origin)-1 and self.origin[self.position+1] == '=':
                self.actual = Token(type('>='), 'gteq_compare')
                self.position += 1
            else:
                self.actual = Token(type('>'), 'gt_compare')
            self.position += 1
        elif self.origin[self.position] == '<':
            if self.position < len(self.origin)-1 and self.origin[self.position+1] == '=':
                self.actual = Token(type('<='), 'lteq_compare')
                self.position += 1
            else:
                self.actual = Token(type('<'), 'lt_compare')
            self.position += 1
        elif self.origin[self.position] == '!':
            if self.position < len(self.origin)-1 and self.origin[self.position+1] == '=':
                self.actual = Token(type('!='), 'noteq_compare')
                self.position += 1
            else:
                self.actual = Token(type('!'), 'not')
            self.position += 1
        elif self.origin[self.position] == '=':
            if self.position < len(self.origin)-1 and self.origin[self.position+1] == '=':
                self.actual = Token(type('=='), 'eq_compare')
                self.position += 1
            else:
                self.actual = Token(type('='), 'equal')
            self.position += 1
        elif self.origin[self.position] == '"':
            self.position += 1
            while self.position < len(self.origin) and self.origin[self.position] != '"':
                string += self.origin[self.position]
                self.position += 1
            self.actual = Token('string', string)
            self.position += 1
        elif self.origin[self.position].isalpha(): #Checks for key words
            while self.position < len(self.origin) and (self.origin[self.position].isalpha() or self.origin[self.position].isnumeric() or self.origin[self.position] == '_'):
                string += self.origin[self.position]
                self.position += 1
            string = string.lower()
            if string == 'true' or string == 'false':
                self.actual = Token(bool, string)
            elif string in key_words:
                self.actual = Token('key_word', string)
            else:
                if self.origin[self.position] == '(':
                    self.actual = Token('func_name', string)
                else:
                    self.actual = Token('variable', string)
        elif self.origin[self.position].isnumeric(): #Checks for numbers
            while self.position < len(self.origin) and self.origin[self.position].isnumeric():
                num += self.origin[self.position]
                self.position += 1
            self.actual = Token(int,int(num))
        else:
            raise Exception("Invalid input. Couldn't get next character")

class Parser:
    tokens = None

    @staticmethod
    def parseBlock():
        if Parser.tokens.actual.value == 'open_b':
            Parser.tokens.selectNext()
            commands = []
            while Parser.tokens.actual.value != 'close_b':
                commands.append(Parser.parseCommand())
            Parser.tokens.selectNext()
            return Commands(commands)
        else:
            raise Exception("Invalid input. Was expecting { ")

    @staticmethod        
    def parseCommand():
        node = None
        if Parser.tokens.actual.token_type == 'variable':
            iden = Parser.tokens.actual.value
            Parser.tokens.selectNext()
            if Parser.tokens.actual.value == 'equal':
                Parser.tokens.selectNext()
                node = UpdateVar(iden, [Variable(iden), Parser.parseRelexpr()])
        elif Parser.tokens.actual.value == 'string' or Parser.tokens.actual.value == 'int' or Parser.tokens.actual.value == 'bool' or Parser.tokens.actual.value == 'void':
            var_type = Parser.tokens.actual.value
            Parser.tokens.selectNext()
            if Parser.tokens.actual.token_type == 'variable' and var_type != 'void':
                iden = Parser.tokens.actual.value
                Parser.tokens.selectNext()
                if Parser.tokens.actual.value == 'equal':
                    Parser.tokens.selectNext()
                    node = Assignment(var_type, iden, [Variable(iden), Parser.parseRelexpr()])
            elif Parser.tokens.actual.value == 'function':
                Parser.tokens.selectNext()
                func_name = Parser.tokens.actual.value
                list_of_args = []
                if Parser.tokens.actual.token_type == 'func_name':
                    Parser.tokens.selectNext()
                    if Parser.tokens.actual.value == 'open_p':
                        while Parser.tokens.actual.value != 'close_p':
                            Parser.tokens.selectNext()
                            if Parser.tokens.actual.value == 'string' or Parser.tokens.actual.value == 'int' or Parser.tokens.actual.value == 'bool':
                                if Parser.tokens.actual.value == 'string':
                                    arg_type = str
                                elif Parser.tokens.actual.value == 'int':
                                    arg_type = int
                                elif Parser.tokens.actual.value == 'bool':
                                    arg_type = bool
                                Parser.tokens.selectNext()
                                if Parser.tokens.actual.token_type == 'variable':
                                    list_of_args.append([Parser.tokens.actual.value,arg_type])
                                    Parser.tokens.selectNext()
                                # else:
                                #     raise Exception("Invalid input. Was expecting a variable at function call")
                                if Parser.tokens.actual.value != 'comma' and Parser.tokens.actual.value != 'close_p':
                                    raise Exception("Invalid input. Was expecting , or )")
                        Parser.tokens.selectNext()
                        node = FuncDec(var_type, func_name, list_of_args, Parser.parseBlock())
                        return node
                    else:
                        raise Exception("Invalid input. Was expecting (")
                else:
                    raise Exception("Invalid input. Was expecting function name")
        elif Parser.tokens.actual.token_type == 'func_name':
            func_name = Parser.tokens.actual.value
            Parser.tokens.selectNext()
            list_of_args = []
            if Parser.tokens.actual.value == 'open_p':
                Parser.tokens.selectNext()
                while Parser.tokens.actual.value != 'close_p':
                    #Parser.tokens.selectNext()
                    list_of_args.append(Parser.parseRelexpr())
                    #Parser.tokens.selectNext()
                    # if Parser.tokens.actual.value != 'comma' and Parser.tokens.actual.value != 'close_p':
                    #     raise Exception("Invalid input. Was expecting , or )")
                node = FuncCall(func_name, list_of_args)
                Parser.tokens.selectNext()
            else:
                raise Exception("Invalid input. Was expecting (")
        elif Parser.tokens.actual.value == 'print':
            Parser.tokens.selectNext()
            node = EchoOp(Parser.parseRelexpr())
        elif Parser.tokens.actual.value == 'return':
            Parser.tokens.selectNext()
            node = ReturnNode(Parser.parseRelexpr())
        elif Parser.tokens.actual.value == 'loop':
            Parser.tokens.selectNext()
            if Parser.tokens.actual.value == 'while':
                Parser.tokens.selectNext()
                if Parser.tokens.actual.value == 'open_p':
                    Parser.tokens.selectNext()
                    condition = Parser.parseRelexpr()
                    if Parser.tokens.actual.value == 'close_p':
                        Parser.tokens.selectNext()
                        node = WhileNode([condition, Parser.parseCommand()])
                        return node                
                    else:
                        raise Exception("Invalid input. Expected )")               
                else:
                    raise Exception("Invalid input. Expected (")
            else:
                raise Exception("Invalid input. Expected a loop function (while)")
        elif Parser.tokens.actual.value == 'if':
            Parser.tokens.selectNext()
            if Parser.tokens.actual.value == 'open_p':
                Parser.tokens.selectNext()
                condition = Parser.parseRelexpr()
                if Parser.tokens.actual.value == 'close_p':
                    Parser.tokens.selectNext()
                    command = Parser.parseCommand()
                    if Parser.tokens.actual.value == 'else':
                        Parser.tokens.selectNext()
                        node = IfNode([condition, command, Parser.parseCommand()])
                        return node 
                    else:
                        node = IfNode([condition, command])
                        return node                  
                else:
                    raise Exception("Invalid input. Expected )")               
            else:
                raise Exception("Invalid input. Expected (")
        else:
            node = Parser.parseBlock()
            return node
        if Parser.tokens.actual.value == 'semi_c':
            Parser.tokens.selectNext()
            return node
        else:
            raise Exception("Invalid input. Expected ;")
    
    @staticmethod
    def parseRelexpr():
        node = Parser.parseExpression()
        while Parser.tokens.actual.value == 'lt_compare' or Parser.tokens.actual.value == 'gt_compare' or Parser.tokens.actual.value == 'eq_compare' or Parser.tokens.actual.value == 'noteq_compare' or Parser.tokens.actual.value == 'lteq_compare' or Parser.tokens.actual.value == 'gteq_compare':
            if Parser.tokens.actual.value == 'lt_compare':
                Parser.tokens.selectNext()
                node = BinOp('<',[node,Parser.parseExpression()])
            if Parser.tokens.actual.value == 'gt_compare':
                Parser.tokens.selectNext()
                node = BinOp('>',[node,Parser.parseExpression()])
            if Parser.tokens.actual.value == 'eq_compare':
                Parser.tokens.selectNext()
                node = BinOp('==',[node,Parser.parseExpression()])
            if Parser.tokens.actual.value == 'noteq_compare':
                Parser.tokens.selectNext()
                node = BinOp('!=',[node,Parser.parseExpression()])
            if Parser.tokens.actual.value == 'lteq_compare':
                Parser.tokens.selectNext()
                node = BinOp('<=',[node,Parser.parseExpression()])
            if Parser.tokens.actual.value == 'gteq_compare':
                Parser.tokens.selectNext()
                node = BinOp('>=',[node,Parser.parseExpression()])
        return node

    @staticmethod
    def parseExpression():
        node = Parser.parseTerm()
        while Parser.tokens.actual.value == 'plus' or Parser.tokens.actual.value == 'minus' or Parser.tokens.actual.value == 'or' or Parser.tokens.actual.value == 'concat':
            if Parser.tokens.actual.value == 'plus':
                Parser.tokens.selectNext()
                node = BinOp('+',[node,Parser.parseTerm()])
            if Parser.tokens.actual.value == 'minus':
                Parser.tokens.selectNext()
                node = BinOp('-',[node,Parser.parseTerm()])
            if Parser.tokens.actual.value == 'or':
                Parser.tokens.selectNext()
                node = BinOp('or',[node,Parser.parseFactor()])
            if Parser.tokens.actual.value == 'concat':
                Parser.tokens.selectNext()
                node = BinOp('.',[node,Parser.parseFactor()])
        return node

    @staticmethod
    def parseTerm():
        node = Parser.parseFactor()
        while Parser.tokens.actual.value == 'mult' or Parser.tokens.actual.value == 'div' or Parser.tokens.actual.value == 'and':
            if Parser.tokens.actual.value == 'mult':
                Parser.tokens.selectNext()
                node = BinOp('*',[node,Parser.parseFactor()])
            if Parser.tokens.actual.value == 'div':
                Parser.tokens.selectNext()
                node = BinOp('/',[node,Parser.parseFactor()])
            if Parser.tokens.actual.value == 'and':
                Parser.tokens.selectNext()
                node = BinOp('and',[node,Parser.parseFactor()])
        return node

    @staticmethod
    def parseFactor():
        node = IntVal(Parser.tokens.actual.value)
        if Parser.tokens.actual.value == 'comma':
            Parser.tokens.selectNext()
        if Parser.tokens.actual.token_type is int:
            node = IntVal(Parser.tokens.actual.value)
            Parser.tokens.selectNext()
            return node
        elif Parser.tokens.actual.token_type is bool:
            if Parser.tokens.actual.value == 'true':
                node = BoolVal(True)
                Parser.tokens.selectNext()
            elif Parser.tokens.actual.value == 'false':
                node = BoolVal(False)
                Parser.tokens.selectNext()
            else:
                raise Exception("Invalid input. Bool type error) ")
            return node
        elif Parser.tokens.actual.token_type == 'string':
            node = StringVal(Parser.tokens.actual.value)
            Parser.tokens.selectNext()
            return node
        elif Parser.tokens.actual.value == 'plus':
            Parser.tokens.selectNext()
            node = UnOp('+',[Parser.parseFactor()])
            return node
        elif Parser.tokens.actual.value == 'minus':
            Parser.tokens.selectNext()
            node = UnOp('-',[Parser.parseFactor()])
            return node
        elif Parser.tokens.actual.value == 'not':
            Parser.tokens.selectNext()
            node = UnOp('!',[Parser.parseFactor()])
            return node 
        elif Parser.tokens.actual.value == 'open_p':
            Parser.tokens.selectNext()
            node = Parser.parseRelexpr()
            if Parser.tokens.actual.value != 'close_p':
                raise Exception("Invalid input. Was expecting ) ")
            Parser.tokens.selectNext()
            return node
        elif Parser.tokens.actual.token_type == 'variable':
            node = Variable(Parser.tokens.actual.value)
            Parser.tokens.selectNext()
            return node
        elif Parser.tokens.actual.token_type == 'func_name':
            func_name = Parser.tokens.actual.value
            Parser.tokens.selectNext()
            list_of_args = []
            if Parser.tokens.actual.value == 'open_p':
                Parser.tokens.selectNext()
                while Parser.tokens.actual.value != 'close_p':
                    list_of_args.append(Parser.parseRelexpr())
                    if Parser.tokens.actual.value != 'comma' and Parser.tokens.actual.value != 'close_p':
                        raise Exception("Invalid input. Was expecting , or )")
                node = FuncCall(func_name, list_of_args)
                Parser.tokens.selectNext()
                return node
            else:
                raise Exception("Invalid input. Was expecting (")
        else:
            raise Exception("Invalid input. Was expecting number, +, -, ( or function call")
        
    @staticmethod
    def run(code):
        preprocessing = PrePro.filter(code)
        Parser.tokens = Tokenizer(preprocessing)
        node_final = Parser.parseBlock()
        if Parser.tokens.actual.value != 'eof':
            raise Exception("Invalid input. Did not reach EOF")
        variable_list = SymbolTable()
        node_final.Evaluate(variable_list)

class PrePro:
    @staticmethod
    def filter(code):
        filteredCode = re.sub(re.compile("/\*.*?\*/",re.DOTALL ) ,"" ,code)
        filteredCode = re.sub("\n","", filteredCode)
        return filteredCode

class Node:
    value = None
    children = []
    def Evaluate(self):
        pass

class BinOp(Node):
    def __init__(self, value, children):
        self.value = value
        self.children = children

    def Evaluate(self, variable_list):
        if self.value == '+':
            c0 = self.children[0].Evaluate(variable_list)
            c1 = self.children[1].Evaluate(variable_list)
            if c0[1] != str and c1[1] != str:
                return (c0[0] + c1[0], int)
            else:
                raise Exception("Invalid input. Invalid types for + operation")
        elif self.value == '-':
            c0 = self.children[0].Evaluate(variable_list)
            c1 = self.children[1].Evaluate(variable_list)
            if c0[1] != str and c1[1] != str:
                return (c0[0] - c1[0], int)
            else:
                raise Exception("Invalid input. Invalid types for - operation")
        elif self.value == '/':
            c0 = self.children[0].Evaluate(variable_list)
            c1 = self.children[1].Evaluate(variable_list)
            if c0[1] != str and c1[1] != str:
                return (c0[0] // c1[0], int)
            else:
                raise Exception("Invalid input. Invalid types for / operation")
        elif self.value == '*':
            c0 = self.children[0].Evaluate(variable_list)
            c1 = self.children[1].Evaluate(variable_list)
            if c0[1] != str and c1[1] != str:
                return (c0[0] * c1[0], int)
            else:
                raise Exception("Invalid input. Invalid types for * operation")
        elif self.value == 'and':
            c0 = self.children[0].Evaluate(variable_list)
            c1 = self.children[1].Evaluate(variable_list)
            if c0[1] != str and c1[1] != str:
                return (bool(c0[0]) and bool(c1[0]), bool)
            else:
                raise Exception("Invalid input. Invalid types for AND operation")
        elif self.value == 'or':
            c0 = self.children[0].Evaluate(variable_list)
            c1 = self.children[1].Evaluate(variable_list)
            if c0[1] != str and c1[1] != str:
                return (bool(c0[0]) or bool(c1[0]), bool)
            else:
                raise Exception("Invalid input. Invalid types for OR operation")
        elif self.value == '<':
            c0 = self.children[0].Evaluate(variable_list)
            c1 = self.children[1].Evaluate(variable_list)
            if c0[1] != str and c1[1] != str:
                return (int(c0[0]) < int(c1[0]), bool)
            else:
                raise Exception("Invalid input. Invalid types for < operation")
        elif self.value == '>':
            c0 = self.children[0].Evaluate(variable_list)
            c1 = self.children[1].Evaluate(variable_list)
            if c0[1] != str and c1[1] != str:
                return (int(c0[0]) > int(c1[0]), bool)
            else:
                raise Exception("Invalid input. Invalid types for > operation")
        elif self.value == '>=':
            c0 = self.children[0].Evaluate(variable_list)
            c1 = self.children[1].Evaluate(variable_list)
            if c0[1] != str and c1[1] != str:
                return (int(c0[0]) >= int(c1[0]), bool)
            else:
                raise Exception("Invalid input. Invalid types for >= operation")
        elif self.value == '<=':
            c0 = self.children[0].Evaluate(variable_list)
            c1 = self.children[1].Evaluate(variable_list)
            if c0[1] != str and c1[1] != str:
                return (int(c0[0]) <= int(c1[0]), bool)
            else:
                raise Exception("Invalid input. Invalid types for <= operation")
        elif self.value == '!=':
            c0 = self.children[0].Evaluate(variable_list)
            c1 = self.children[1].Evaluate(variable_list)
            if c0[1] == c1[1]:
                return (c0[0] != c1[0], bool)
            elif c0[1] == str or c1[1] == str:
                  raise Exception("Invalid input. Invalid types for != operation")
            else: 
                return (int(c0[0]) != int(c1[0]), bool)
        elif self.value == '==':
            c0 = self.children[0].Evaluate(variable_list)
            c1 = self.children[1].Evaluate(variable_list)
            if c0[1] == c1[1]:
                return (c0[0] == c1[0], bool)
            elif c0[1] == str or c1[1] == str:
                  raise Exception("Invalid input. Invalid types for == operation")
            else: 
                return (int(c0[0]) == int(c1[0]), bool)
        
class Assignment(Node):
    def __init__(self, var_type, name, children):
        self.name = name
        if var_type == 'string':
            self.var_type = str
        elif var_type == 'int':
            self.var_type = int
        elif var_type == 'bool':
            self.var_type = bool
        else:
            raise Exception("Variable cannot be of unknow type or void")
        self.children = children

    def Evaluate(self, variable_list):
        if self.name not in variable_list.id:
            c1 = self.children[1].Evaluate(variable_list)
            if c1[1] != self.var_type:
                raise Exception("Variable can only be assigned with values from its type")
            variable_list.set(self.name, c1[0], c1[1])
        else:
            raise Exception("Cannot re-declare a variable in the same context")

class UpdateVar(Node):
    def __init__(self, name, children):
        self.name = name
        self.children = children

    def Evaluate(self, variable_list):    
        if self.name in variable_list.id:
            c1 = self.children[1].Evaluate(variable_list)
            variable_list.set(self.name, c1[0], c1[1])
        else:
            raise Exception("Variable has not been declared")

class UnOp(Node):
    def __init__(self, value, children):
        self.value = value
        self.children = children

    def Evaluate(self, variable_list):
        if self.value == '+':
            return (+self.children[0].Evaluate(variable_list)[0], int)
        elif self.value == '-':
            return (-self.children[0].Evaluate(variable_list)[0], int) 
        elif self.value == '!':
            return (not self.children[0].Evaluate(variable_list)[0], bool)  

class EchoOp(Node):
    def __init__(self, child):
        self.child = child

    def Evaluate(self, variable_list):
        return print(self.child.Evaluate(variable_list)[0])

class ReadlineOp(Node):
    def __init__(self):
        self.value = 0

    def Evaluate(self, variable_list):
        self.value = input()
        return (int(self.value), int)

class IfNode(Node):
    def __init__(self, children):
        self.children = children
    
    def Evaluate(self, variable_list):
        if(self.children[0].Evaluate(variable_list)[0]):
            return self.children[1].Evaluate(variable_list)
        elif len(self.children)>2:
            return self.children[2].Evaluate(variable_list)

class WhileNode(Node):
    def __init__(self, children):
        self.children = children
    
    def Evaluate(self, variable_list):
        while(self.children[0].Evaluate(variable_list)[0]):
            self.children[1].Evaluate(variable_list)

class ReturnNode(Node):
    def __init__(self, child):
        self.child = child
    
    def Evaluate(self, variable_list):
        c0 = self.child.Evaluate(variable_list)
        variable_list.set("return_val", c0[0], c0[1])
        
class Variable(Node):
    def __init__(self, name):
        self.name = name

    def Evaluate(self, variable_list):
        return variable_list.get(self.name) 

class Commands(Node):
    def __init__(self, children):
        self.children = children

    def Evaluate(self, variable_list):
        for n in self.children:
            n.Evaluate(variable_list)
            if "return_val" in variable_list.id:
                break

class IntVal(Node):
    def __init__(self, value):
        self.value = value

    def Evaluate(self, variable_list):
        return (self.value, int)

class StringVal(Node):
    def __init__(self, value):
        self.value = value

    def Evaluate(self, variable_list):
        return (self.value, str)

class BoolVal(Node):
    def __init__(self, value):
        self.value = value

    def Evaluate(self, variable_list):
        return (self.value, bool)

class NoOp(Node):
    def __init__(self):
        pass

    def Evaluate(self, variable_list):
        pass

class FuncDec:
    def __init__(self, func_type, name, args, commands):
        self.name = name
        self.args = args
        self.commands = commands
        if func_type == 'string':
            self.func_type = str
        elif func_type == 'int':
            self.func_type = int
        else:
            self.func_type = None

    def Evaluate(self, variable_list):
        SymbolTable.defineFunc(self.name, self)

class FuncCall:
    def __init__(self, name, args):
        self.name = name
        self.args = args

    def Evaluate(self, variable_list):
        func_variable_list = SymbolTable()
        target_func = SymbolTable.getFunc(self.name)
        if len(target_func.args) != len(self.args):
            raise Exception("Wrong of number of arguments for function")
        for i in range(len(target_func.args)):
            c0 = self.args[i].Evaluate(variable_list)
            if c0[1] == target_func.args[i][1]:
                func_variable_list.set(target_func.args[i][0], c0[0], c0[1])
            else:
                raise Exception("Function expected another argument type")
        target_func.commands.Evaluate(func_variable_list)
        if "return_val" in func_variable_list.id and target_func.func_type == None:
            raise Exception("Function is void, but has return statement")
        elif "return_val" not in func_variable_list.id and target_func.func_type == None:
            return None
        else:
            if target_func.func_type != None:
                ret_val = func_variable_list.get("return_val")
                if ret_val[1] == target_func.func_type:
                    return ret_val
                else:
                    raise Exception("Function expected another return type")

class SymbolTable:
    funcs = {}

    def __init__(self):
        self.id = {}

    def get(self, name):
        return self.id[name] 
    
    def set(self, name, value, tipo):
        self.id[name] = (value, tipo)

    @staticmethod
    def getFunc(name):
        return SymbolTable.funcs[name] 
    
    @staticmethod
    def defineFunc(name, node):
        if name not in SymbolTable.funcs:
            SymbolTable.funcs[name] = node
        else:
            raise Exception("Function error. Cannot declare same function named {} more than once".format(name))

def main():
    file_name = sys.argv[1]
    if os.path.splitext(file_name)[1] != ".vegs":
        raise Exception("Invalid file. You must use a .vegs file")
    else:
        with open(file_name, "r") as input:
            Parser.run(input.read())
if __name__ == '__main__':
  main()