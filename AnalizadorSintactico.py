import ply.yacc
import ply.lex as lex
import ply.yacc as yacc
from AnalizadorLexico import tokens, lexer
reglas = []
sucess = True

# Regla padre


def p_programa(p):
    '''programa : clase
    | metodo
    | clase programa
    | metodo programa
    | lista_codigo programa
    | expresion
    | expresion programa
    |

    '''


def p_identificador(p):
    ''' identificador : VARIABLE
    | CONSTANT
    | VARIABLE_GLOBAL
    | VARIABLE_CLASE
    | VARIABLE_INSTANCIA'''


def p_asignacion(p):
    '''asignacion : identificador EQUALS number'
    | identificador EQUALS llamar_funcion
    '''


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
    | times
    '''


def p_arreglo(p):
    '''
    arreglo : identificador EQUALS LBRACKET elementos RBRACKET
    '''
    print("arreglo")


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
    | PUTS LPAREN expresion RPAREN'''
    print(p[2])
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
    metodo : DEF VARIABLE lista_codigo END
    | DEF VARIABLE LPAREN parametro RPAREN lista_codigo END
    | DEF VARIABLE LPAREN parametro RPAREN lista_codigo RETURN expresion END
    parametro : VARIABLE
    | VARIABLE COMMA parametro
    lista_codigo : codigo
    | vacio
    | codigo lista_codigo
    codigo : asignacion
    | expresion
    | condicional_if
    | iteracion
    | puts



    '''


def p_condicional_if(p):
    '''
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
    else : ELSE varias_exp
    | ELSE identificador else
    | ELSE lista_codigo else

    elsif : ELSIF expresion_condicion lista_codigo
    | ELSIF expresion_condicion lista_codigo elsif
    | ELSIF identificador lista_codigo
    | ELSIF identificador lista_codigo elsif
    '''


def p_expresion_condicion(p):
    '''expresion_condicion : expresion EQUALS EQUALS expresion
    | expresion ISEQUAL expresion
    | expresion NOT EQUALS expresion
    | expresion LESS expresion
    | expresion LESS EQUALS expresion
    | expresion GREATER expresion
    | expresion GREATER EQUALS expresion
    | expresion AND expresion
    | expresion OR expresion
    | NOT expresion'''


def p_iteracion(p):
    ''' iteracion : WHILE expresion lista_codigo END
    | FOR expresion IN expresion lista_codigo END
    | FOR expresion IN rango lista_codigo END

    rango : LPAREN INTEGER DOT DOT INTEGER RPAREN
    '''


def p_times(p):
    ''' times : INTEGER DOT TIMES LBRACE expresion RBRACE
    | identificador DOT TIMES LBRACE expresion RBRACE
    | INTEGER DOT TIMES DO expresion END
    | identificador DOT TIMES DO expresion END
    '''


def p_expresion_matematica(p):
    """
    expresion_matematica : expresion PLUS expresion
                    | expresion MINUS expresion
                    | expresion TIMS expresion
                    | expresion DIVIDE expresion
    """


def p_asignacion(p):
    """asignacion : identificador EQUALS expresion
                | identificador PLUS EQUALS expresion
                | identificador MINUS EQUALS expresion"""


def p_llamar_funcion(p):
    '''llamar_funcion : VARIABLE
    | VARIABLE LPAREN parametro RPAREN
    | VARIABLE DOT VARIABLE
    | identificador DOT VARIABLE'''


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
