"""
HIGHER ORDER FUNCTIONS: Funções que podem receber e/ou retornar outras funções
    Esse conceito depende da existência de first-class functions

First Class Functions: Funções que são tratadas como outros tipos de dados comuns

Quer dizer que as funções em python podem ser 
tratadas como qualquer outro tipo de dado
"""

def saudacao(msg, nome): # First-class function
    return f'{msg}, {nome}!'

saudacao_2 = saudacao

# msg = saudacao_2('Bom dia')
# print(msg)


def executa(funcao, *args): # HOF
    return funcao(*args)


print(executa(saudacao, 'Bom dia', 'Lara'),)