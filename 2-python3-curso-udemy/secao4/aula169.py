# Exercício - Unir listas
# Crie uma função zipper (como o zipper de roupas)
# O trabalho dessa função será unir duas
# listas na ordem.
# Use todos os valores da menor lista.
# Ex.:
# ['Salvador', 'Ubatuba', 'Belo Horizonte']
# ['BA', 'SP', 'MG', 'RJ']
# Resultado
# [('Salvador', 'BA'), ('Ubatuba', 'SP'), ('Belo Horizonte', 'MG')]

lista_1 = ['Salvador', 'Ubatuba', 'Belo Horizonte']
lista_2 = ['BA', 'SP', 'MG', 'RJ']


def decoradora(func):
    def aninhada(*args, **kwargs):
        primeira = args[0]
        segunda = args[1]
        if len(primeira) < len(segunda):
            resultado = func(primeira, segunda)
        else:
            resultado = func(segunda, primeira)
        return resultado
    return aninhada

@decoradora
def une_listas(primeira_lista, segunda_lista):
    resultado = []
    for i in range(len(primeira_lista)):
        resultado.append((primeira_lista[i], segunda_lista[i]))
    
    return resultado

teste = une_listas(lista_2, lista_1)
# print(teste)

# SOLUÇÃO DO PROFESSOR
def zipper(lista1, lista2):
    max_interval = min(len(lista_1), len(lista2))
    resultado = []
    for i in range(max_interval):
        resultado.append((lista1[i], lista2[i]))

    return resultado

teste = une_listas(lista_2, lista_1)
# print(teste)


# USANDO ZIP:
# print(list(zip(lista_1, lista_2)))


# USANDO ZIP_LONGEST
from itertools import zip_longest
print(list(zip_longest(lista_1, lista_2)))