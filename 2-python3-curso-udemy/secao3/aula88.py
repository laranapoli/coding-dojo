"""
Tupla = Lista imutável
- Tupla é um pouco mais eficiente que a lista
"""

# Podemos criar não passando os parênteses
nomes = 'Maria', 'Helena', 'Luiz'
print(nomes)
print(nomes[-1])

# Para ser muito específico, passar entre parênteses
nomes = ('Maria', 'Helena', 'Luiz')

# Outra maneira:
nomes = ['Maria', 'Helena', 'Luiz']
nomes = tuple(nomes)