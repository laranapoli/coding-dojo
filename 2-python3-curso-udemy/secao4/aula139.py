"""
LIST COMPREHENSION COM MAIS DE UM FOR
"""

lista = [
    x 
    for x in range(3)
    for _ in range(3)
]

print(lista)

lista_dentro_lista = [
    [x for y in range(x)]
    for x in range(3)
]

print(lista_dentro_lista)