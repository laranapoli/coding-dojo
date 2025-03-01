"""
split e join com list e str
split - divide uma string
join - une uma string
"""

frase = 'Olha só, que coisa interessante'

lista_palavras = frase.split()

print(f'{lista_palavras=}')

lista_frases = frase.split(',')

print(f'{lista_frases=}')

lista_frases_fixed = []

for i, frase in enumerate(lista_frases):
    lista_frases_fixed.append(lista_frases[i].strip())

print(f'{lista_frases_fixed=}')

frases_unidas = ' '.join(lista_palavras)

print(frases_unidas)