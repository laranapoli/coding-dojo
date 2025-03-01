"""
Continuação - Listas

+ - Concatena listas
"""

lista_a = [1, 2, 3]
lista_b = [4, 5, 6]
lista_c = lista_a + lista_b
lista_d = lista_a.extend(lista_b) # Não retorna nada! Está mexendo no obj lista_a

print(lista_c)
print(lista_d)
print(lista_a)