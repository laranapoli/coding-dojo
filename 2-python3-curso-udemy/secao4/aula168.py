"""
ORDEM DOS DECORADORES
"""

def parametros_decorador(nome):
    def decorador(func):
        print('Decorador:', nome)

        def sua_nova_funcao(*args, **kwargs):
            res = func(*args, **kwargs)
            final = f'{res} {nome}'
            return final
        return sua_nova_funcao
    return decorador

@parametros_decorador(nome='ParametroQuatro')
@parametros_decorador(nome='ParametroTres')
@parametros_decorador(nome='ParametroDois')
@parametros_decorador(nome='ParametroUm')
def soma(x, y):
    return x + y

dez_mais_cinco = soma(10, 5)
print(dez_mais_cinco)