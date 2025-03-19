"""
MAP - MAPEAR DADOS
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

def adjust_price(valor, porcentagem):
    return round(valor * porcentagem, 2)

############################
from functools import partial

aumentar_dez_porcento = partial(
    adjust_price,
    porcentagem=1.1
)
############################

novos_produtos = [
    {**p, 'preco': aumentar_dez_porcento(p['preco'])}
    for p in produtos
]

print_iter(produtos)
print_iter(novos_produtos)

#################################################
# mudando para map
def muda_preco(produto):
    return {
        **produto,
        'preco': aumentar_dez_porcento(produto['preco'])
    }


novos_produtos = map(
    muda_preco,
    produtos
)

print_iter(novos_produtos)

print(novos_produtos)
print(hasattr(novos_produtos, '__iter__'))  # Se tem iter é um iterável
print(hasattr(novos_produtos, '__next__'))  # Se tem next é um iterator

# Todo generator é um iterator, mas nem todo iterator é um generator
from types import GeneratorType
print(isinstance(novos_produtos, GeneratorType))  # map não é um generator

# O iterator é esgotável. A partir do momento que foi todo percorrido, retorna lista vazia
# Para reutilizar, converte em lista junto ao map!