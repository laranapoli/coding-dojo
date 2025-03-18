"""
DECORADORES

- Decorar = Adicionar / Remover / Restringir / Alterar
- Decoradores são usados para fazer o Python usar as funções decoradoras em outras funções
- Decoradores são syntax sugar
"""

def criar_funcao(func):
    def interna(*args, **kwargs):
        print('Vou te decorar!')
        for arg in args:
            is_string(arg)
        resultado = func(*args, **kwargs)
        print('Você foi decorada')
        return resultado
    return interna

@criar_funcao
def inverte_string(string):
    print(inverte_string.__name__)  # O Python troca a função para -> interna
    return string[::-1]

def is_string(param):
    if not isinstance(param, str):
        raise TypeError('Param should be a string')

# inverte_string_checando_parametro = criar_funcao(inverte_string)
# invertida = inverte_string_checando_parametro('123')

invertida = inverte_string('123')
print(invertida)