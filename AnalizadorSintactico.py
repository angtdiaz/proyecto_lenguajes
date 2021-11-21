import ply.yacc as yacc
from AnalizadorLexico import tokens,lex

def p_prueba(p):
    '''prueba : variable
    | variable_global
    | variable_instancia
    | constant
    | variable_clase
    | imprimir
    | clase
    | operaciones
    | arreglos
    | hash'''
def p_clase(p):
    '''clase : CLASS CONSTANT END'''
#moises coronel---->>>
def p_operadores(p):
    '''operadores : PLUS
    | MINUS
    | TIMES
    | DIVIDE'''
#moisescoronel
def p_operaciones(p):
    '''operaciones : valor operadores valor
    | valor operadores operaciones'''
#moisesCoronel
def p_variable(p):
    '''variable : VARIABLE EQUALS valor'''
# moisesCoronel ---->>>>>>
def p_variable_global(p):
    '''variable_global : VARIABLE_GLOBAL EQUALS valor'''
def p_variable_instancia(p):
    '''variable_instancia : VARIABLE_INSTANCIA EQUALS valor'''
def p_constant(p):
    '''constant : CONSTANT  EQUALS  valor'''
def p_variable_clase(p):
    '''variable_clase : VARIABLE_CLASE EQUALS valor'''
def p_arreglos(p):
    '''arreglos : VARIABLE EQUALS LBRACKET valor_arreglo RBRACKET'''
def p_valor_arreglo(p):
    '''valor_arreglo : valor
    | valor_arreglo COMMA valor'''
def p_hash(p):
    '''hash : VARIABLE EQUALS LBRACE valores_hash RBRACE '''

def p_asig_Valor(p):
    '''asig_valor : STRING EQUALS GREATER valor
    | INTEGER EQUALS GREATER valor'''

def p_valores_hash(p):
    '''valores_hash : asig_valor
    | valores_hash COMMA asig_valor'''
def p_valor(p):
    '''valor : STRING
    | INTEGER
    | FLOATINGPOINT
    | BOOLEAN'''
def p_imprimir(p):
    '''imprimir : PUTS valor'''
    print(p[2])
<<<<<------ moises coronel
def p_error(p):
    print("error syntaxis")

parser = yacc.yacc()
while True:
    try:
        s = input('calc> ')
    except EOFError:
        break
    if not s: continue
    result = parser.parse(s)
    print(result)



