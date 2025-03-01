"""
enumerate - enumera iteráveis (índices)

- É um iterator!
"""

lista = ['Maria', 'Helena', 'Luiz']
lista.append('João')

lista_enumerada = enumerate(lista)
print(lista_enumerada)
print(next(lista_enumerada))

for i,value in lista_enumerada:
    print(i, value) # Quando você faz um print, consome o iterator


for i,value in lista_enumerada:
    print(i, value) 
    
# É possível mudar de onde ele começa:
for i, value in enumerate(lista, start=10):
    print(i, value)

# Esse for equivale a um for dentro do outro!