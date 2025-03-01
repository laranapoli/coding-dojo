# Desempacotamento em chamadas 
# de métodos e funções
lista = ['Maria', 'Helena', 1, 2, 3, 'Eduarda']
tupla = 'Python', 'é', 'legal'

p, *_, u = lista
print(p, u)

print(*lista)

print(*tupla)