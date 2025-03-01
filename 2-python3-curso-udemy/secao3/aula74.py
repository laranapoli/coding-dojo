"""
Como o for funciona por baixo dos panos

iterável -> elemento que pode te entregar 1 coisa por vez
    - método que tem um (__iter__)

Iterador -> quem sabe entregar um valor por vez

next -> me entregue o próximo valor

iter -> me entregue seu iterador
"""

iterador = iter('Luiz')  # __iter__() - é o entregador

# print(texto.__next__())
# print(next(texto))
# print(texto.__next__())
# print(texto.__next__())
# print(texto.__next__())

while True:
    try:
        letra = next(iterador)
        print(letra)
    except StopIteration:
        break