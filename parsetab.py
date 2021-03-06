
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'AND BOOL CLOSEBRACK CLOSEPAR COMMA COMPEQUALS DIVIDE ELSE EQUALS FALSE FUNCTION GREATERTHAN GREATERTHANOREQUALS ID IF INT LESSTHAN LESSTHANOREQUALS LOOP MINUS MULTIPLY NORMSTRING NOT NOTEQUALS NUMBER OPENBRACK OPENPAR OR PLUS PRINT RETURN SEMICOL STRING TRUE VOID WHILE\n    program : commandLoop\n    \n    commandLoop : command commandLoop\n                | empty\n    \n    block : OPENBRACK command CLOSEBRACK\n          | OPENBRACK CLOSEBRACK\n    \n    command : function SEMICOL\n            | RETURN relexpr SEMICOL\n            | print SEMICOL\n            | assignment SEMICOL\n            | empty SEMICOL\n            | block\n            | while\n            | if\n            | INT FUNCTION function block\n            | STRING FUNCTION function block\n            | BOOL FUNCTION function block\n            | VOID FUNCTION function block\n    \n    function : ID OPENPAR INT ID CLOSEPAR\n             | ID OPENPAR INT ID moreArg CLOSEPAR\n             | ID OPENPAR STRING ID CLOSEPAR\n             | ID OPENPAR STRING ID moreArg CLOSEPAR\n             | ID OPENPAR BOOL ID CLOSEPAR\n             | ID OPENPAR BOOL ID moreArg CLOSEPAR\n             | ID OPENPAR relexpr CLOSEPAR\n             | ID OPENPAR relexpr moreArg CLOSEPAR\n             | ID OPENPAR CLOSEPAR\n    \n    moreArg : COMMA relexpr\n            | COMMA relexpr moreArg\n            | COMMA INT ID\n            | COMMA INT ID moreArg\n            | COMMA STRING ID\n            | COMMA STRING ID moreArg\n            | COMMA BOOL ID\n            | COMMA BOOL ID moreArg\n    \n    assignment : ID EQUALS expression\n               | INT ID EQUALS expression\n               | STRING ID EQUALS expression\n    \n    while : LOOP WHILE OPENPAR relexpr CLOSEPAR block\n    \n    if : IF OPENPAR relexpr CLOSEPAR block\n       | IF OPENPAR relexpr CLOSEPAR block ELSE block\n    \n    print : PRINT OPENPAR expression CLOSEPAR\n    \n    expression : term\n               | term OR term\n               | term PLUS term\n               | term MINUS term\n    \n    relexpr : expression\n            | expression COMPEQUALS expression\n            | expression LESSTHAN expression\n            | expression GREATERTHAN expression\n            | expression GREATERTHANOREQUALS expression\n            | expression LESSTHANOREQUALS expression\n            | expression NOTEQUALS expression\n    \n    term : factor\n         | factor MULTIPLY factor\n         | factor DIVIDE factor\n         | factor AND factor\n    \n    factor : PLUS factor\n            | MINUS factor\n            | NOT factor\n            | NUMBER \n            | TRUE\n            | FALSE\n            | OPENPAR relexpr CLOSEPAR\n            | ID\n            | NORMSTRING\n            | function\n    \n    empty : \n    '
    
_lr_action_items = {'RETURN':([0,3,9,10,11,18,22,23,38,39,50,54,85,101,103,105,106,128,136,141,],[6,6,-11,-12,-13,6,-10,-6,-8,-9,-5,-7,-4,-14,-15,-16,-17,-39,-38,-40,]),'INT':([0,3,9,10,11,18,22,23,38,39,46,50,54,85,101,103,105,106,112,128,136,141,],[12,12,-11,-12,-13,12,-10,-6,-8,-9,78,-5,-7,-4,-14,-15,-16,-17,124,-39,-38,-40,]),'STRING':([0,3,9,10,11,18,22,23,38,39,46,50,54,85,101,103,105,106,112,128,136,141,],[13,13,-11,-12,-13,13,-10,-6,-8,-9,80,-5,-7,-4,-14,-15,-16,-17,125,-39,-38,-40,]),'BOOL':([0,3,9,10,11,18,22,23,38,39,46,50,54,85,101,103,105,106,112,128,136,141,],[14,14,-11,-12,-13,14,-10,-6,-8,-9,81,-5,-7,-4,-14,-15,-16,-17,126,-39,-38,-40,]),'VOID':([0,3,9,10,11,18,22,23,38,39,50,54,85,101,103,105,106,128,136,141,],[15,15,-11,-12,-13,15,-10,-6,-8,-9,-5,-7,-4,-14,-15,-16,-17,-39,-38,-40,]),'SEMICOL':([0,3,4,5,7,8,9,10,11,18,22,23,24,25,26,29,31,32,33,35,36,37,38,39,50,51,54,64,65,69,79,83,85,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,110,113,116,118,120,122,128,129,130,131,136,141,],[-67,-67,22,23,38,39,-11,-12,-13,-67,-10,-6,54,-46,-42,-53,-60,-61,-62,-64,-65,-66,-8,-9,-5,22,-7,-57,-58,-59,-26,-35,-4,-47,-48,-49,-50,-51,-52,-43,-44,-45,-54,-55,-56,-63,-14,-36,-15,-37,-16,-17,-24,-41,-18,-20,-22,-25,-39,-19,-21,-23,-38,-40,]),'$end':([0,1,2,3,4,9,10,11,21,22,23,38,39,50,54,85,101,103,105,106,128,136,141,],[-67,0,-1,-67,-3,-11,-12,-13,-2,-10,-6,-8,-9,-5,-7,-4,-14,-15,-16,-17,-39,-38,-40,]),'ID':([0,3,6,9,10,11,12,13,18,22,23,27,28,30,34,38,39,40,42,44,45,46,47,48,50,53,54,55,56,57,58,59,60,61,62,63,66,67,68,73,75,78,80,81,85,86,101,103,105,106,112,124,125,126,128,136,141,],[16,16,35,-11,-12,-13,41,43,16,-10,-6,35,35,35,35,-8,-9,72,72,72,72,35,35,35,-5,35,-7,35,35,35,35,35,35,35,35,35,35,35,35,35,35,107,108,109,-4,35,-14,-15,-16,-17,35,133,134,135,-39,-38,-40,]),'PRINT':([0,3,9,10,11,18,22,23,38,39,50,54,85,101,103,105,106,128,136,141,],[17,17,-11,-12,-13,17,-10,-6,-8,-9,-5,-7,-4,-14,-15,-16,-17,-39,-38,-40,]),'OPENBRACK':([0,3,9,10,11,18,22,23,38,39,50,54,71,74,76,77,79,85,101,103,105,106,110,115,116,118,120,122,127,128,129,130,131,136,137,141,],[18,18,-11,-12,-13,18,-10,-6,-8,-9,-5,-7,18,18,18,18,-26,-4,-14,-15,-16,-17,-24,18,-18,-20,-22,-25,18,-39,-19,-21,-23,-38,18,-40,]),'LOOP':([0,3,9,10,11,18,22,23,38,39,50,54,85,101,103,105,106,128,136,141,],[19,19,-11,-12,-13,19,-10,-6,-8,-9,-5,-7,-4,-14,-15,-16,-17,-39,-38,-40,]),'IF':([0,3,9,10,11,18,22,23,38,39,50,54,85,101,103,105,106,128,136,141,],[20,20,-11,-12,-13,20,-10,-6,-8,-9,-5,-7,-4,-14,-15,-16,-17,-39,-38,-40,]),'PLUS':([6,26,27,28,29,30,31,32,33,34,35,36,37,46,47,48,53,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,73,75,79,86,97,98,99,100,110,112,116,118,120,122,129,130,131,],[27,62,27,27,-53,27,-60,-61,-62,27,-64,-65,-66,27,27,27,27,27,27,27,27,27,27,27,27,27,-57,-58,27,27,27,-59,27,27,-26,27,-54,-55,-56,-63,-24,27,-18,-20,-22,-25,-19,-21,-23,]),'MINUS':([6,26,27,28,29,30,31,32,33,34,35,36,37,46,47,48,53,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,73,75,79,86,97,98,99,100,110,112,116,118,120,122,129,130,131,],[28,63,28,28,-53,28,-60,-61,-62,28,-64,-65,-66,28,28,28,28,28,28,28,28,28,28,28,28,28,-57,-58,28,28,28,-59,28,28,-26,28,-54,-55,-56,-63,-24,28,-18,-20,-22,-25,-19,-21,-23,]),'NOT':([6,27,28,30,34,46,47,48,53,55,56,57,58,59,60,61,62,63,66,67,68,73,75,86,112,],[30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,]),'NUMBER':([6,27,28,30,34,46,47,48,53,55,56,57,58,59,60,61,62,63,66,67,68,73,75,86,112,],[31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,]),'TRUE':([6,27,28,30,34,46,47,48,53,55,56,57,58,59,60,61,62,63,66,67,68,73,75,86,112,],[32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,]),'FALSE':([6,27,28,30,34,46,47,48,53,55,56,57,58,59,60,61,62,63,66,67,68,73,75,86,112,],[33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,]),'OPENPAR':([6,16,17,20,27,28,30,34,35,46,47,48,52,53,55,56,57,58,59,60,61,62,63,66,67,68,72,73,75,86,112,],[34,46,48,53,34,34,34,34,46,34,34,34,86,34,34,34,34,34,34,34,34,34,34,34,34,34,46,34,34,34,34,]),'NORMSTRING':([6,27,28,30,34,46,47,48,53,55,56,57,58,59,60,61,62,63,66,67,68,73,75,86,112,],[36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,]),'CLOSEBRACK':([9,10,11,18,22,23,38,39,49,50,54,85,101,103,105,106,128,136,141,],[-11,-12,-13,50,-10,-6,-8,-9,85,-5,-7,-4,-14,-15,-16,-17,-39,-38,-40,]),'FUNCTION':([12,13,14,15,],[40,42,44,45,]),'EQUALS':([16,41,43,],[47,73,75,]),'WHILE':([19,],[52,]),'CLOSEPAR':([25,26,29,31,32,33,35,36,37,46,64,65,69,70,79,82,84,87,88,89,90,91,92,93,94,95,96,97,98,99,100,107,108,109,110,111,114,116,117,118,119,120,121,122,123,129,130,131,132,133,134,135,138,139,140,],[-46,-42,-53,-60,-61,-62,-64,-65,-66,79,-57,-58,-59,100,-26,110,113,115,-47,-48,-49,-50,-51,-52,-43,-44,-45,-54,-55,-56,-63,116,118,120,-24,122,127,-18,129,-20,130,-22,131,-25,-27,-19,-21,-23,-28,-29,-31,-33,-30,-32,-34,]),'COMMA':([25,26,29,31,32,33,35,36,37,64,65,69,79,82,88,89,90,91,92,93,94,95,96,97,98,99,100,107,108,109,110,116,118,120,122,123,129,130,131,133,134,135,],[-46,-42,-53,-60,-61,-62,-64,-65,-66,-57,-58,-59,-26,112,-47,-48,-49,-50,-51,-52,-43,-44,-45,-54,-55,-56,-63,112,112,112,-24,-18,-20,-22,-25,112,-19,-21,-23,112,112,112,]),'COMPEQUALS':([25,26,29,31,32,33,35,36,37,64,65,69,79,94,95,96,97,98,99,100,110,116,118,120,122,129,130,131,],[55,-42,-53,-60,-61,-62,-64,-65,-66,-57,-58,-59,-26,-43,-44,-45,-54,-55,-56,-63,-24,-18,-20,-22,-25,-19,-21,-23,]),'LESSTHAN':([25,26,29,31,32,33,35,36,37,64,65,69,79,94,95,96,97,98,99,100,110,116,118,120,122,129,130,131,],[56,-42,-53,-60,-61,-62,-64,-65,-66,-57,-58,-59,-26,-43,-44,-45,-54,-55,-56,-63,-24,-18,-20,-22,-25,-19,-21,-23,]),'GREATERTHAN':([25,26,29,31,32,33,35,36,37,64,65,69,79,94,95,96,97,98,99,100,110,116,118,120,122,129,130,131,],[57,-42,-53,-60,-61,-62,-64,-65,-66,-57,-58,-59,-26,-43,-44,-45,-54,-55,-56,-63,-24,-18,-20,-22,-25,-19,-21,-23,]),'GREATERTHANOREQUALS':([25,26,29,31,32,33,35,36,37,64,65,69,79,94,95,96,97,98,99,100,110,116,118,120,122,129,130,131,],[58,-42,-53,-60,-61,-62,-64,-65,-66,-57,-58,-59,-26,-43,-44,-45,-54,-55,-56,-63,-24,-18,-20,-22,-25,-19,-21,-23,]),'LESSTHANOREQUALS':([25,26,29,31,32,33,35,36,37,64,65,69,79,94,95,96,97,98,99,100,110,116,118,120,122,129,130,131,],[59,-42,-53,-60,-61,-62,-64,-65,-66,-57,-58,-59,-26,-43,-44,-45,-54,-55,-56,-63,-24,-18,-20,-22,-25,-19,-21,-23,]),'NOTEQUALS':([25,26,29,31,32,33,35,36,37,64,65,69,79,94,95,96,97,98,99,100,110,116,118,120,122,129,130,131,],[60,-42,-53,-60,-61,-62,-64,-65,-66,-57,-58,-59,-26,-43,-44,-45,-54,-55,-56,-63,-24,-18,-20,-22,-25,-19,-21,-23,]),'OR':([26,29,31,32,33,35,36,37,64,65,69,79,97,98,99,100,110,116,118,120,122,129,130,131,],[61,-53,-60,-61,-62,-64,-65,-66,-57,-58,-59,-26,-54,-55,-56,-63,-24,-18,-20,-22,-25,-19,-21,-23,]),'MULTIPLY':([29,31,32,33,35,36,37,64,65,69,79,100,110,116,118,120,122,129,130,131,],[66,-60,-61,-62,-64,-65,-66,-57,-58,-59,-26,-63,-24,-18,-20,-22,-25,-19,-21,-23,]),'DIVIDE':([29,31,32,33,35,36,37,64,65,69,79,100,110,116,118,120,122,129,130,131,],[67,-60,-61,-62,-64,-65,-66,-57,-58,-59,-26,-63,-24,-18,-20,-22,-25,-19,-21,-23,]),'AND':([29,31,32,33,35,36,37,64,65,69,79,100,110,116,118,120,122,129,130,131,],[68,-60,-61,-62,-64,-65,-66,-57,-58,-59,-26,-63,-24,-18,-20,-22,-25,-19,-21,-23,]),'ELSE':([50,85,128,],[-5,-4,137,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'program':([0,],[1,]),'commandLoop':([0,3,],[2,21,]),'command':([0,3,18,],[3,3,49,]),'empty':([0,3,18,],[4,4,51,]),'function':([0,3,6,18,27,28,30,34,40,42,44,45,46,47,48,53,55,56,57,58,59,60,61,62,63,66,67,68,73,75,86,112,],[5,5,37,5,37,37,37,37,71,74,76,77,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,]),'print':([0,3,18,],[7,7,7,]),'assignment':([0,3,18,],[8,8,8,]),'block':([0,3,18,71,74,76,77,115,127,137,],[9,9,9,101,103,105,106,128,136,141,]),'while':([0,3,18,],[10,10,10,]),'if':([0,3,18,],[11,11,11,]),'relexpr':([6,34,46,53,86,112,],[24,70,82,87,114,123,]),'expression':([6,34,46,47,48,53,55,56,57,58,59,60,73,75,86,112,],[25,25,25,83,84,25,88,89,90,91,92,93,102,104,25,25,]),'term':([6,34,46,47,48,53,55,56,57,58,59,60,61,62,63,73,75,86,112,],[26,26,26,26,26,26,26,26,26,26,26,26,94,95,96,26,26,26,26,]),'factor':([6,27,28,30,34,46,47,48,53,55,56,57,58,59,60,61,62,63,66,67,68,73,75,86,112,],[29,64,65,69,29,29,29,29,29,29,29,29,29,29,29,29,29,29,97,98,99,29,29,29,29,]),'moreArg':([82,107,108,109,123,133,134,135,],[111,117,119,121,132,138,139,140,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('program -> commandLoop','program',1,'p_program','tokens.py',101),
  ('commandLoop -> command commandLoop','commandLoop',2,'p_commandLoop','tokens.py',109),
  ('commandLoop -> empty','commandLoop',1,'p_commandLoop','tokens.py',110),
  ('block -> OPENBRACK command CLOSEBRACK','block',3,'p_block','tokens.py',120),
  ('block -> OPENBRACK CLOSEBRACK','block',2,'p_block','tokens.py',121),
  ('command -> function SEMICOL','command',2,'p_command','tokens.py',128),
  ('command -> RETURN relexpr SEMICOL','command',3,'p_command','tokens.py',129),
  ('command -> print SEMICOL','command',2,'p_command','tokens.py',130),
  ('command -> assignment SEMICOL','command',2,'p_command','tokens.py',131),
  ('command -> empty SEMICOL','command',2,'p_command','tokens.py',132),
  ('command -> block','command',1,'p_command','tokens.py',133),
  ('command -> while','command',1,'p_command','tokens.py',134),
  ('command -> if','command',1,'p_command','tokens.py',135),
  ('command -> INT FUNCTION function block','command',4,'p_command','tokens.py',136),
  ('command -> STRING FUNCTION function block','command',4,'p_command','tokens.py',137),
  ('command -> BOOL FUNCTION function block','command',4,'p_command','tokens.py',138),
  ('command -> VOID FUNCTION function block','command',4,'p_command','tokens.py',139),
  ('function -> ID OPENPAR INT ID CLOSEPAR','function',5,'p_function','tokens.py',152),
  ('function -> ID OPENPAR INT ID moreArg CLOSEPAR','function',6,'p_function','tokens.py',153),
  ('function -> ID OPENPAR STRING ID CLOSEPAR','function',5,'p_function','tokens.py',154),
  ('function -> ID OPENPAR STRING ID moreArg CLOSEPAR','function',6,'p_function','tokens.py',155),
  ('function -> ID OPENPAR BOOL ID CLOSEPAR','function',5,'p_function','tokens.py',156),
  ('function -> ID OPENPAR BOOL ID moreArg CLOSEPAR','function',6,'p_function','tokens.py',157),
  ('function -> ID OPENPAR relexpr CLOSEPAR','function',4,'p_function','tokens.py',158),
  ('function -> ID OPENPAR relexpr moreArg CLOSEPAR','function',5,'p_function','tokens.py',159),
  ('function -> ID OPENPAR CLOSEPAR','function',3,'p_function','tokens.py',160),
  ('moreArg -> COMMA relexpr','moreArg',2,'p_moreArg','tokens.py',176),
  ('moreArg -> COMMA relexpr moreArg','moreArg',3,'p_moreArg','tokens.py',177),
  ('moreArg -> COMMA INT ID','moreArg',3,'p_moreArg','tokens.py',178),
  ('moreArg -> COMMA INT ID moreArg','moreArg',4,'p_moreArg','tokens.py',179),
  ('moreArg -> COMMA STRING ID','moreArg',3,'p_moreArg','tokens.py',180),
  ('moreArg -> COMMA STRING ID moreArg','moreArg',4,'p_moreArg','tokens.py',181),
  ('moreArg -> COMMA BOOL ID','moreArg',3,'p_moreArg','tokens.py',182),
  ('moreArg -> COMMA BOOL ID moreArg','moreArg',4,'p_moreArg','tokens.py',183),
  ('assignment -> ID EQUALS expression','assignment',3,'p_assignment','tokens.py',197),
  ('assignment -> INT ID EQUALS expression','assignment',4,'p_assignment','tokens.py',198),
  ('assignment -> STRING ID EQUALS expression','assignment',4,'p_assignment','tokens.py',199),
  ('while -> LOOP WHILE OPENPAR relexpr CLOSEPAR block','while',6,'p_while','tokens.py',208),
  ('if -> IF OPENPAR relexpr CLOSEPAR block','if',5,'p_if','tokens.py',214),
  ('if -> IF OPENPAR relexpr CLOSEPAR block ELSE block','if',7,'p_if','tokens.py',215),
  ('print -> PRINT OPENPAR expression CLOSEPAR','print',4,'p_print','tokens.py',224),
  ('expression -> term','expression',1,'p_expression','tokens.py',230),
  ('expression -> term OR term','expression',3,'p_expression','tokens.py',231),
  ('expression -> term PLUS term','expression',3,'p_expression','tokens.py',232),
  ('expression -> term MINUS term','expression',3,'p_expression','tokens.py',233),
  ('relexpr -> expression','relexpr',1,'p_relexpr','tokens.py',242),
  ('relexpr -> expression COMPEQUALS expression','relexpr',3,'p_relexpr','tokens.py',243),
  ('relexpr -> expression LESSTHAN expression','relexpr',3,'p_relexpr','tokens.py',244),
  ('relexpr -> expression GREATERTHAN expression','relexpr',3,'p_relexpr','tokens.py',245),
  ('relexpr -> expression GREATERTHANOREQUALS expression','relexpr',3,'p_relexpr','tokens.py',246),
  ('relexpr -> expression LESSTHANOREQUALS expression','relexpr',3,'p_relexpr','tokens.py',247),
  ('relexpr -> expression NOTEQUALS expression','relexpr',3,'p_relexpr','tokens.py',248),
  ('term -> factor','term',1,'p_term','tokens.py',257),
  ('term -> factor MULTIPLY factor','term',3,'p_term','tokens.py',258),
  ('term -> factor DIVIDE factor','term',3,'p_term','tokens.py',259),
  ('term -> factor AND factor','term',3,'p_term','tokens.py',260),
  ('factor -> PLUS factor','factor',2,'p_factor','tokens.py',269),
  ('factor -> MINUS factor','factor',2,'p_factor','tokens.py',270),
  ('factor -> NOT factor','factor',2,'p_factor','tokens.py',271),
  ('factor -> NUMBER','factor',1,'p_factor','tokens.py',272),
  ('factor -> TRUE','factor',1,'p_factor','tokens.py',273),
  ('factor -> FALSE','factor',1,'p_factor','tokens.py',274),
  ('factor -> OPENPAR relexpr CLOSEPAR','factor',3,'p_factor','tokens.py',275),
  ('factor -> ID','factor',1,'p_factor','tokens.py',276),
  ('factor -> NORMSTRING','factor',1,'p_factor','tokens.py',277),
  ('factor -> function','factor',1,'p_factor','tokens.py',278),
  ('empty -> <empty>','empty',0,'p_empty','tokens.py',292),
]
