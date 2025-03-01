"""
For + Range

range -> range(start, stop, step)

- o stop não é incluído!
"""

numeros = range(10, 0, -1)

# Aqui não pegamos o índice, mas sim o valor
for numero in numeros:
    print(numero)

# Quando chega na última posição, o iterador levanta um erro 
# de stop iteration!