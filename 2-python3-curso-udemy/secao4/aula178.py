"""
REDUCE
- Faz a redução de um iterável em um único valor
"""
from functools import reduce

produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 10},
    {'nome': 'Produto 3', 'preco': 10},
    {'nome': 'Produto 2', 'preco': 10},
    {'nome': 'Produto 4', 'preco': 10},
]

total = 0  # acumulador

for p in produtos:
    total += p['preco']

print(total)

# a função reduce precisa de um acumulador também
def funcao_do_reduce(  # Recebe 2 parâmetros
    acumulador,
    produto
):
    print(acumulador)
    print('produto', produto)
    print()
    return acumulador + produto['preco']

total = reduce(
    # funcao_do_reduce,
    lambda ac, p: ac + p['preco'],
    produtos,  # Iterável
    0          # Valor inicial - se nao passar, o acumulador será o primeiro produto e o produto será o segundo produto
)

print('Total é:', total)