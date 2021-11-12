import ply.lex as lex
## moises coronel =>
tokens = ['VARIABLE','VARIABLE_GLOBAL','VARIABLE_INSTANCIA','VARIABLE_CLASE','CONSTANTE','COMENTARIO','CADENA','ENTERO','FLOTANTE']


## Palabras reservadas (moises coronel)
reserved = {

    'elsif': 'ELSIF',
    'def': 'DEF',
    'class': 'CLASS',
    'and': 'AND',
    'or': 'OR',
    'do': 'DO',
    'else': 'ELSE',
    'while': 'WHILE',
    'unless': 'UNLESS',
    'end': 'END',
    'begin': 'BEGIN',
    'break': 'BREAK',
    'case': 'CASE',
    'in': 'IN',
    'raise': 'RAISE',
    'false': 'FALSE',
    'for': 'FOR',
    'if': 'IF',
    'nil': 'NIL',
    'redo': 'REDO',
    'true': 'TRUE',
    'return': 'RETURN',
    'not': 'NOT',
    'self': 'SELF',
    'retry': 'RETRY'
}

tokens = tokens + list(reserved.values())


# TOKENS (Moises Coronel)

#t_VARIABLE = r'[a-z][A-Za-z0-9_]*'
t_VARIABLE_GLOBAL= r'\$[a-zA-Z_][A-Za-z0-9_]*'
t_VARIABLE_INSTANCIA=r'\@[a-zA-Z_][A-Za-z0-9_]*'
t_VARIABLE_CLASE=r'\@\@[a-zA-Z_][A-Za-z0-9_]*'
t_CONSTANTE= r'[A-Z][a-z]*'
t_CADENA = r'(\"|\')[a-zA-z0-9\s]*(\"|\')'
t_COMENTARIO = r'(\#.*|\"\"\".*\"\"\")'
##------------------------
## moises coronel
def t_VARIABLE(t):
    r'[a-zA-Z_][A-Za-z0-9_]*'
    t.type = reserved.get(t.value,'VARIABLE')
    return t

 ## moises coronel
def t_FLOTANTE(t):
    r'-?\d+\.\d+'
    t.value = float(t.value)
    return t

 ## moises coronel
def t_ENTERO(t):
    r'-?[0-9]+'
    t.value = int(t.value)
    return t


# IGNORE
t_ignore = " \t"


## moises coronel
def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")

 ## moises coronel
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)


# BUILDER
lexer = lex.lex()


def inputLex(s):
    lexer.input(s)
    while True:
        tok = lexer.token()
        if not tok:
            break  # No more input
        print(tok)


token = " "
while (token != 'x'):
    token = input('Token > ')
    inputLex(token)
