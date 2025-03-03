"""
EMPACOTAMENTO E DESEMPACOTAMENTO DE DICIONÁRIOS
kwargs - keyword arguments (argumentos nomeados)
"""

a, b = 1, 2
a, b = b, a

print(a, b)

pessoa = {
    'nome': 'Aline',
    'sobrenome': 'Souza'
}

a, b = pessoa
print(a, b)

a, b = pessoa.values()
print(a, b)

a, b = pessoa.items()
print(a, b)

(a1, a2), b = pessoa.items()
print(a1, a2, b)

print('---------------------------')

dados_pessoa = {
    'idade': 27,
    'altura': 1.67
}

pessoa_completa = {**pessoa, **dados_pessoa}

print(pessoa_completa)

print('---------------------------')

def mostro_argumentos_nomeados(*args, **kwargs):
    print(kwargs)

    for key, value in kwargs.items():
        print(key, value)

mostro_argumentos_nomeados(nome='Joana', sobrenome='Souza')
print('---------------------------')
mostro_argumentos_nomeados(**pessoa_completa)