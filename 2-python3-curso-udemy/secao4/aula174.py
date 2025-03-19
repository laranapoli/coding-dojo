"""
COMBINATIONS, PERMUTATIONS E PRODUCT - ITERTOOLS
- Combinação: Ordem não importa - Iterável + Tamanho do grupo
- Permutação: Ordem importa
- Produto: Ordem importa e repete valores únicos
"""
from itertools import combinations, permutations, product

def print_iter(iterator):
    print(iterator.__class__)
    print(*list(iterator), sep='\n')
    print()


pessoas = [
    'João', 'Joana', 'Lara',
]

camisetas = [
    ['preta', 'branca'],
    ['p', 'm', 'g'],
    ['masculino', 'feminino'],
    ['algodão', 'poliester'],
]

# print_iter(combinations(pessoas, 2))
# print_iter(permutations(pessoas, 2))
print_iter(product(*camisetas))