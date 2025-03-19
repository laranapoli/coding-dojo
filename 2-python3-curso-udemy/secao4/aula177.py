"""
FILTER

- Com map, geralmente retorna o mesmo tamanho do iterável recebido
- Com filter retorna a mesma quantidade ou menos valores
"""
def print_iter(iterator):
    print(*list(iterator), sep='\n')
    print()

produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]


# Filtro = a direita
novos_produtos = [
    p for p in produtos
    if p['preco'] < 25
]

print_iter(novos_produtos)


# Filter (programação funcional)
novos_produtos = filter(
    lambda p: p['preco'] > 100,
    produtos
)
print_iter(novos_produtos)
