"""
FUNÇÃO LAMBDA 
É uma função como qualquer outra, porém
são funções anônimas que contém apenas uma linha.
Ou seja, tudo deve ser contido dentro de uma 
única expressão.
"""
lista = [
    {'nome': 'Luiz', 'sobrenome': 'miranda'},
    {'nome': 'Maria', 'sobrenome': 'Oliveira'},
    {'nome': 'Daniel', 'sobrenome': 'Silva'},
    {'nome': 'Eduardo', 'sobrenome': 'Moreira'},
    {'nome': 'Aline', 'sobrenome': 'Souza'},
]

def ordena(item):
    return item['nome']

lista.sort(key=lambda item: item['nome'])

# A opção abaixo faz uma shallow copy da lista original!
l1 = sorted(lista, key=lambda item: item['nome'])
l2 = sorted(lista, key=lambda item: item['sobrenome'])

for item in lista:
    print(item)

# Obs.: O Python usa tabela unicode para fazer ordenação alfabética