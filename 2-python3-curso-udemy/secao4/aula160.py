# copy, sorted, produtos.sort
# Exercícios
# Aumente os preços dos produtos a seguir em 10%
# Gere novos_produtos por deep copy (cópia profunda)
produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]

from copy import deepcopy

novos_produtos = deepcopy(produtos)

novos_produtos = [
    {
        key: value*1.1
        if isinstance(value, float) else value
        for key, value
        in item.items()
    }
    for item in novos_produtos
]

print(*novos_produtos, sep='\n')

# Ordene os produtos por nome decrescente (do maior para menor)
# Gere produtos_ordenados_por_nome por deep copy (cópia profunda)
produtos_ordenados_por_nome = deepcopy(produtos)

produtos_ordenados_por_nome = [
    item['nome'] for item in produtos_ordenados_por_nome
]

produtos_ordenados_por_nome.sort()
print(produtos_ordenados_por_nome)

# Ordene os produtos por preco crescente (do menor para maior)
# Gere produtos_ordenados_por_preco por deep copy (cópia profunda)

produtos_ordenados_por_preco = deepcopy(produtos)
produtos_ordenados_por_preco = [
    item['preco'] for item in produtos_ordenados_por_preco
]

produtos_ordenados_por_preco.sort()
print(produtos_ordenados_por_preco)


############### SOLUÇÃO DO PROFESSOR
# 1)
novos_produtos = [
    {
        **item, 'preco': round(item['preco']*1.1, 2)
    }
    for item in deepcopy(produtos)
]
print()
print(*novos_produtos, sep='\n')
  
# 2) 
produtos_ordenados_por_preco = sorted(
    deepcopy(produtos),
    key=lambda p: p['nome'],
    reverse=True
)

# 3)
produtos_ordenados_por_preco = sorted(
    deepcopy(produtos),
    key=lambda p: p['preco']
)
