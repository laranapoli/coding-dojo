"""
Valores padrão para parâmetros
Ao definir uma função, os parâmetros podem
ter valores padrão. Caso o valor não seja
enviado para o parâmetro, o valor padrão será
usado.
Refator: Editar o seu código.
"""

def soma(x, y, z=None): # E todo o parâmetro que vier depois de um parâmetro com valor padrão, precisa ter valor padrão
    if z is not None:
        print(x + y + z)
    else:
        print(x + y)


soma(1, 2, 3)
soma(4, 5)