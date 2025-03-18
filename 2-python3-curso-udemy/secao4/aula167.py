"""
DECORADORES COM PARÂMETROS

- A função fabrica_de_funcoes é usada para criar funções: Fábrica de funções
- 
"""
def fabrica_de_decoradores(a, b, c):  # Parâmetros que podem ser usados para configurar o decorador
    def fabrica_de_funcoes(func):
        print('fabrica_de_funcoes 1')

        def aninhada(*args, **kwargs):  # inner function OU nested function
            print('Aninhada', a, b, c)
            res = func(*args, **kwargs)
            return res
        return aninhada
    return fabrica_de_funcoes


# def fabrica_de_decoradores(a, b, c):
#     return fabrica_de_funcoes


# Quando passa sem parênteses: Python executa a fabrica_de_funcoes
# Quando fecha parênteses: Tenta já executar a aninhada | TypeError: fabrica_de_funcoes() missing 1 required positional argument: 'func'
# @fabrica_de_funcoes
@fabrica_de_decoradores(1, 2, 3)
def soma(x, y):  # A função aninhada mais interna é a que vai substituir a minha função real
    return x + y


dez_mais_cinco = soma(10, 5)
print(dez_mais_cinco)