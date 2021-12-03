import ply.lex as lex
reglas = []
# moises coronel / modificación angie tuarez
tokens = ['VARIABLE', 'VARIABLE_GLOBAL', 'VARIABLE_INSTANCIA',
          'VARIABLE_CLASE', 'CONSTANT', "FLOATINGPOINT",
          "INTEGER", "BOOLEAN", "STRING", "PLUS", "MINUS",
          "TIMS", "DIVIDE", "AND", "OR", "NOT", "EQUALS", "LESS",
          "GREATER", "DOT", "LPAREN", "RPAREN", "COMMA", "ISEQUAL", "LBRACE", "RBRACE", "LBRACKET", "RBRACKET"]

# Palabras reservadas (moises coronel)
reserved = {
    'elsif': 'ELSIF',
    'else': 'ELSE',
    'if': 'IF',
    'def': 'DEF',
    'class': 'CLASS',
    'do': 'DO',
    'while': 'WHILE',
    'end': 'END',
    #'begin': 'BEGIN',
    'in': 'IN',
    'for': 'FOR',
    'return': 'RETURN',
    'puts': 'PUTS',
    'times': 'TIMES',
    'length': 'LENGTH',
    'key': 'KEY',
    'first': 'FIRST',
    'last': 'LAST'
}

tokens = tokens + list(reserved.values())


# TOKENS (Moises Coronel)

# t_VARIABLE = r'[a-z][A-Za-z0-9_]*'
t_VARIABLE_GLOBAL = r'\$[a-zA-Z_][A-Za-z0-9_]*'
t_VARIABLE_INSTANCIA = r'\@[a-zA-Z_][A-Za-z0-9_]*'
t_VARIABLE_CLASE = r'\@\@[a-zA-Z_][A-Za-z0-9_]*'
t_CONSTANT = r'[A-Z][a-z0-9_]*'
t_STRING = r'(\"|\')[a-zA-z0-9\s\.\?\¿\!\¡\,\;\:]*(\"|\')'
#t_COMMENT = r'(\#.*|\"\"\".*\"\"\")'

t_DOT = r'\.'
# ------------------------

# angie tuarez
t_PLUS = r"\+"
t_MINUS = r'\-'
t_TIMS = r"\*"
t_DIVIDE = r"\/"
t_AND = r"\&\&"
t_OR = r"\|\|"
t_NOT = r"\!"
t_ISEQUAL = r"\=\="
t_LESS = r"\<"
t_GREATER = r"\>"
t_LPAREN = r"\("
t_RPAREN = r"\)"
t_COMMA = r"\,"
# t_SEMICOLON = r"\;"
# t_QUOTE = r"\""
t_LBRACE = r"\{"
t_RBRACE = r"\}"
t_LBRACKET = r"\["
t_RBRACKET = r"\]"
# t_POUND = r"\#"
t_EQUALS = r"\="


def t_BOOLEAN(t):
    r"true|false"
    return t


# def t_LETTER(t):
#     r"\'.\'"
#     t.value = t.value.replace("", "")
#     return t

# moises coronel


def t_VARIABLE(t):
    r'[a-z][A-Za-z0-9_]*'
    t.type = reserved.get(t.value, 'VARIABLE')
    return t


def t_FLOATINGPOINT(t):
    r'\d+\.\d+'
    t.value = float(t.value)
    return t


def t_INTEGER(t):
    r'[0-9]+'
    t.value = int(t.value)
    return t


# IGNORE
t_ignore = " \t"


# moises coronel
def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")


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


'''
token = " "
while (token != 'x'):
    token = input('Token > ')
    inputLex(token)
'''


def aLexico(data):
    lexer.lineno = 0
    reglas.clear()  # limpio los errores
    lexer.input(data)
    resultados = ""
    while True:
        tok = lexer.token()
        if not tok:
            break
        resultado = str(tok) + "\n"
        resultados = resultados + resultado
    return resultados, reglas