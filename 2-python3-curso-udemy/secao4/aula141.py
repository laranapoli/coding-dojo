"""
DICTIONARY E SET COMPREHENSION
"""

produto = {
    'nome': 'Caneta Azul',
    'preco': 2.5,
    'categoria': 'Escritório',
}

new_dict = {
    chave: valor.upper()
    if isinstance(valor, str) else valor
    for chave, valor
    in produto.items()
    if chave != 'categoria'
}

print(new_dict)

s1 = {i for i in range(10)}
print(s1)