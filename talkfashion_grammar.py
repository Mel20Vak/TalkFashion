from textx import metamodel_from_str

talkfashion_grammar = """
Model:
    statements*=Statement
;

Statement:
    VariableDeclaration |
    InputStatement |
    SuggestStatement |
    PrintStatement |
    IfStatement |
    FunctionDeclaration |
    FunctionCall |
    ReturnStatement |
    Block
;

VariableDeclaration:
    'var' name=ID ':' type=Type ('=' expression=Expression)? ';'
;

Type:
    'String' | 'Bool' | 'List<String>' | 'Outfit'
;

InputStatement:
    name=ID '=' 'input' '(' prompt=STRING ')' ';'
;

SuggestStatement:
    'suggest' 'outfit' expression=Expression ('for' event=ID)?;
;

PrintStatement:
    'print' '(' expression=Expression ')' ';'
;

IfStatement:
    'if' '(' condition=Expression ')' thenBlock=Block
    ('else' elseBlock=Block)?
;

Block:
    '{' statements*=Statement '}'
;

FunctionDeclaration:
    'func' name=ID '(' params*=Parameter[','] ')' ('->' returnType=Type)? body=Block
;

Parameter:
    name=ID ':' type=Type
;

FunctionCall:
    name=ID '(' args*=Expression[','] ')'
;

ReturnStatement:
    'return' expression=Expression ';'
;

Expression:
    Literal | ID | FunctionCall | BinaryOperation | TemplateString | OutfitConcat
;

OutfitConcat:
    left=Expression '+' right=Expression
;

Literal:
    IntLiteral | StringLiteral | BoolLiteral
;

IntLiteral:
    value=INT
;

StringLiteral:
    value=STRING
;

BoolLiteral:
    value=BOOL
;

BinaryOperation:
    left=Expression operator=Operator right=Expression
;

Operator:
    '==' | '!=' | '<' | '>' | '<=' | '>=' | '+' | '-' | '*' | '/' | '&&' | '||'
;

TemplateString:
    '${' expression=Expression '}'
;

Comment:
    /\/\/.*$/
;

BOOL:
    "true" | "false"
;
"""

# Create the metamodel from the grammar
talkfashion_metamodel = metamodel_from_str(talkfashion_grammar)
