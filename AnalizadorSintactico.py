import ply.yacc
import ply.lex as lex
import ply.yacc as yacc
from AnalizadorLexico import tokens, lexer
reglas = []
sucess = True

# Regla padre

#
def p_programa(p):
   '''programa : clase
    | metodo
    | clase programa
    | metodo programa
    | lista_codigo programa
    | expresion
    | expresion programa
    '''
def p_identificador(p):
    ''' identificador : VARIABLE
    | CONSTANT
    | VARIABLE_GLOBAL
    | VARIABLE_CLASE
    | VARIABLE_INSTANCIA'''

def p_number(p):
    '''number : INTEGER
    | FLOATINGPOINT'''


def p_expresion(p):
    '''expresion : identificador
    | STRING
    | number
    | BOOLEAN
    | expresion_condicion
    | expresion_matematica
    | llamar_funcion
    | asignacion
    | arreglo
    | hash
    | puts
    | valorArr
    | times
    '''


def p_arreglo(p):
    '''
    arreglo : identificador EQUALS LBRACKET elementos RBRACKET
    valorArr : identificador LBRACKET valores_mat RBRACKET
    '''



def p_elementos(p):
    '''
    elementos : expresion
    | expresion COMMA elementos
    '''


def p_hash(p):
    '''
    hash : identificador EQUALS LBRACE elementos_hash RBRACE
    '''


def p_elementos_hash(p):
    '''
    elementos_hash : expresion EQUALS GREATER expresion
    | expresion EQUALS GREATER expresion COMMA elementos_hash
    '''


def p_puts(p):
    '''puts : PUTS expresion
    | PUTS expresion_matematica
    | PUTS LPAREN expresion RPAREN
    | PUTS LPAREN expresion_matematica RPAREN'''
# definicion de clase


def p_clase(p):
    '''
    clase : CLASS CONSTANT varias_exp varios_met END
    | CLASS CONSTANT varias_exp END
    | CLASS CONSTANT varios_met END
    varias_exp : expresion
    | expresion varias_exp
    varios_met : metodo
    | metodo varios_met
    '''
# definicion metodo


def p_metodo(p):
    '''
    metodo : DEF VARIABLE puts END
    | DEF VARIABLE LPAREN parametro RPAREN lista_codigo END
    parametro : VARIABLE
    | VARIABLE COMMA parametro
    lista_codigo : lista_codigo codigo
    | vacio
    codigo : asignacion
    | expresion
    | condicional_if
    | iteracion
    '''


def p_condicional_if(p):
    '''
<<<<<<< HEAD
    condicional_if : IF identificador lista_codigo END
    | IF identificador lista_codigo else END
    | IF identificador lista_codigo elsif END
    | IF identificador lista_codigo else elsif END
    | IF identificador lista_codigo elsif else END

    | IF expresion_condicion lista_codigo END
    | IF expresion_condicion lista_codigo else END
    | IF expresion_condicion lista_codigo elsif END
    | IF expresion_condicion lista_codigo else elsif END
    | IF expresion_condicion lista_codigo elsif else END
    else : ELSE expresion_condicion
    | ELSE identificador else
    | ELSE lista_codigo else
=======
    condicional_if : IF content_if lista_codigo END
    | IF content_if lista_codigo else END
    | IF content_if lista_codigo elsif END
    | IF LPAREN content_if RPAREN lista_codigo END
    | IF LPAREN content_if RPAREN lista_codigo else END
    | IF LPAREN content_if RPAREN lista_codigo elsif END
>>>>>>> ba0faaa7399a72b1835c76f81a2dd0f99a3f5e42

    content_if : identificador
    | expresion_condicion

    else : ELSE lista_codigo
    | ELSE lista_codigo elsif
    elsif : ELSIF expresion_condicion lista_codigo
    | ELSIF expresion_condicion lista_codigo elsif
    | ELSIF expresion_condicion lista_codigo else
    | ELSIF LPAREN expresion_condicion RPAREN lista_codigo
    | ELSIF LPAREN expresion_condicion RPAREN lista_codigo elsif
    | ELSIF LPAREN expresion_condicion RPAREN lista_codigo else

    '''
# regla semantica de condicion restringe el uso de booleanos, no se puede comparar con números
def p_expresion_condicion(p):
    '''expresion_condicion : valores_cond opNum valores_cond
   | identificador opIgual  BOOLEAN
    | BOOLEAN opIgual identificador
    | identificador opIgual valores_cond
    | valores_cond opIgual identificador

    '''

def p_valores_cond(p):
    '''valores_cond : valores_mat
    | STRING
     '''
def p_operador_condicion(p):
    ''' operador_condicion : opNum
    | opIgual
      opNum : LESS
        | LESS EQUALS
        | GREATER
        | GREATER EQUALS
    opIgual : ISEQUAL
        | NOT EQUALS

    '''

def p_iteracion(p):
    ''' iteracion : WHILE content_if lista_codigo END
    | WHILE LPAREN content_if RPAREN lista_codigo END
    | FOR expresion IN expresion lista_codigo END
    | FOR expresion IN rango lista_codigo END
    | FOR LPAREN expresion RPAREN IN expresion lista_codigo END
    | FOR LPAREN expresion RPAREN IN rango lista_codigo END

    rango : LPAREN valorR DOT DOT valorR RPAREN

    valorR : expresion_matematica
    | valores_mat
    '''


def p_times(p):
    ''' times : INTEGER DOT TIMES LBRACE expresion RBRACE
    | identificador DOT TIMES LBRACE expresion RBRACE
    | INTEGER DOT TIMES DO expresion END
    | identificador DOT TIMES DO expresion END
    '''



# regla semántica : iperaciones_,matemáticas  solo se puede hacerentre numero o variables pero no puede hacerse con valores booleanos

def p_expresion_matematica(p):
    """
    expresion_matematica : valores_mat operador valores_mat
    | valores_mat operador expresion_matematica
    """
def p_valores_mat(p):
    ''' valores_mat : number
    | identificador '''
def p_operador(p):
    '''operador : PLUS
    | MINUS
    | TIMS
    | DIVIDE '''
def p_asignacion(p):
    '''asignacion : identificador EQUALS expresion'''


def p_llamar_funcion(p):
    '''llamar_funcion : VARIABLE DOT LENGTH
    | VARIABLE DOT KEY
    | VARIABLE DOT FIRST
    | VARIABLE DOT LAST'''


def p_vacio(p):
    '''vacio : '''


def p_error(p):
    if p:
        texto = "Syntax error near '%s', line '%s', '%s'" % (
            p.value, p.lineno - 1, p.type)
        print(texto)
        reglas.append(texto)


parser = yacc.yacc()
''''
while True:
    try:
        s = input('calc> ')
    except EOFError:
        break
    if not s:
        continue
    result = parser.parse(s)
    print(result)
'''


def aSintactico(s):
    lexer.lineno = 1
    reglas.clear()  # limpio los errores
    result = str(parser.parse(s))
    print(result)
    prueba = []
    for regla in reglas:
        prueba.append(regla + " \n")
    return prueba
