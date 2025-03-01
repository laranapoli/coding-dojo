"""
Introdução ao desempacotamento

- Desempacotamento pode ser feito com qualquer iterável
- _ antes do nome da variável indica para o desenvolvedor que ñ será usada
"""

nomes = ['Maria', 'Helena', 'Luiz']

_, _, nome, *resto = nomes

print(nome, resto)