"""
FUNÇÕES DECORADORAS

- Decorar = Adicionar / Remover / Restringir / Alterar
- Funções decoradoras são funções que decoram outras funções
"""
# A função decoradora é 'criar_funcao' 
# O trabalho dela é receber uma função, criar 
# uma função interna para que eu tenha uma closure dentro. 
# A função interna não será executada, será retornada 
# para a pessoa que estiver chamando ela possa finalmente 
# executar a função que está sendo decorada
def criar_funcao(func):
    def interna(*args, **kwargs):
        print('Vou te decorar!')
        for arg in args:
            is_string(arg)
        resultado = func(*args, **kwargs)
        print('Você foi decorada')
        return resultado
    return interna

def inverte_string(string):
    return string[::-1]

def is_string(param):
    if not isinstance(param, str):
        raise TypeError('Param should be a string')

inverte_string_checando_parametro = criar_funcao(inverte_string)
invertida = inverte_string_checando_parametro('123')
print(invertida)