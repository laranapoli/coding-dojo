"""
Introdução às funções (def) em Python
Funções são trechos de código usados para
replicar determinada ação ao longo do seu código.
Elas podem receber valores para parâmetros (argumentos)
e retornar um valor específico.
Por padrão, funções Python retornam None (nada).
"""

# None é quase um False

# Quando definimos a função com parâmetros, ao passar 
# valores para eles, são chamados de argumentos


def imprimir(a, b, c):
    print(a, b, c)

# imprimir() -> TypeError: imprimir() missing 3 required positional arguments: 'a', 'b', and 'c' 
# Erro informa que esquecemos de passar os VALORES para a função

imprimir(1, 2, 3)

imprimir(4, 5, 6)


def saudacao(nome='sem nome'):
    print(f'Olá, {nome}!')

saudacao('Lara')
saudacao()