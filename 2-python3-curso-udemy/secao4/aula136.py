"""
LIST COMPREHENSION
Forma rápida para criar listas a partir de iteráveis
"""

print(list(range(10)))

print('---------------------------')

print([i for i in range(10)])

print('---------------------------')

print([
    i * 2 
    for i in range(10)
])

print('---------------------------')
# Mapeamento de dados em list comprehension
produtos = [
    {'nome': 'p1', 'preco': 20},
    {'nome': 'p2', 'preco': 10},
    {'nome': 'p3', 'preco': 30},
]

novos_produtos = [
    {**produto, 'preco': produto['preco'] * 1.05}
    for produto in produtos
]

print(*novos_produtos, sep='\n')

print('---------------------------')

novos_produtos = [
    {**produto, 'preco': produto['preco'] * 1.05}
    if produto['preco'] > 20 else {**produto}
    for produto in produtos
]

print(*novos_produtos, sep='\n')

print('---------------------------')
# FILTRO
# O Que vem na esquerda do for é MAPEAMENTO
# O que vem na direita do for é FILTRO!
import pprint
def p(v):
    pprint.pprint(v, sort_dicts=False, width=40)

# lista = [n for n in range(10) if n < 5]
# p(lista)

novos_produtos = [
    {**produto, 'preco': produto['preco'] * 1.05}
    for produto in produtos
    if produto['preco'] > 20
]

p(novos_produtos)