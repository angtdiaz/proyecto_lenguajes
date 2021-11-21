import ply.yacc as yacc
from AnalizadorLexico import tokens, lex


# Regla padre
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


# moises coronel---->>>
def p_clase(p):
    '''clase : CLASS CONSTANT END'''

def p_operadores(p):
    '''operadores : PLUS
                  | MINUS
                  | TIMES
                  | DIVIDE'''

def p_operaciones(p):
    '''operaciones : comparacion
                   | valor operadores valor
                   | valor operadores operaciones'''

def p_variable(p):
    '''variable : VARIABLE EQUALS valor
                | VARIABLE EQUALS operaciones'''

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

def p_asig_valor(p):
    '''asig_valor : STRING EQUALS GREATER valor
                  | INTEGER EQUALS GREATER valor'''

def p_valores_hash(p):
    '''valores_hash : asig_valor
                    | valores_hash COMMA asig_valor'''

def p_valor(p):
    '''valor : booleano
             | comparable'''

def p_imprimir(p):
    '''imprimir : PUTS valor'''
    print(p[2])
# <<<<<------ moises coronel

# Mario Chalén --->>
def p_booleano(p):
    '''booleano : comparacion
                | multibool
                | negacion
                | BOOLEAN'''


def p_negacion(p):
    '''negacion : NOT booleano
                | NOT VARIABLE'''


def p_comparable(p):
    '''comparable : INTEGER
                  | FLOATINGPOINT
                  | STRING
                  | VARIABLE'''


def p_comparador(p):
    '''comparador : ISEQUAL
                  | GREATER
                  | LESS'''


def p_comparacion(p):
    '''comparacion : comparable comparador comparable'''


def p_union(p):
    '''union : AND
             | OR'''


def p_multibool(p):
    '''multibool : VARIABLE union VARIABLE
                 | booleano union VARIABLE
                 | VARIABLE union booleano
                 | booleano union booleano'''

# <<--- Mario Chalén


def p_error(p):
    print("error syntaxis")


parser = yacc.yacc()
while True:
    try:
        s = input('calc> ')
    except EOFError:
        break
    if not s:
        continue
    result = parser.parse(s)
    print(result)
