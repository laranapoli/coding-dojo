"""
Introdução ao try except

try -> tentar executar o código
except -> ocorreu algum erro ao tentar executar

o if não evita erros

fail fast -> errar rápido
Não interrompe a execução do código (se não levantar um erro)
"""
numero_str = input('Insira um número: ')

try:
    print(f'STR: {numero_str}')
    numero_float = float(numero_str)
    print(f'FLOAT: {numero_float}')
except:
    print('Isso não é um número')


