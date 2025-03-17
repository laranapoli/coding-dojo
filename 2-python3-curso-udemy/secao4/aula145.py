"""
Generator expression, Iterables e Iterators
"""
iterable = ['Eu', 'Tenho', '__iter__']
# iterator = iterable.__iter__()  # tem __iter__ e __next__
iterator = iter(iterable)  # tem __iter__ e __next__

# A única responsabilidade do ITERATOR é te entregar um valor por vez
# É uma classe que PRECISA ter o método __iter__ e o método __next__

print(next(iterator))
print(next(iterator))
print(next(iterator))
# print(next(iterator))
print()
print('-----------------------------')
print()
# Generators = Funções que sabem pausar
# Todo GENERATOR é um ITERATOR (o contrário não é verdadeiro)
import sys 

lista = [n for n in range(1000)]
generator = (n for n in range(1000))

print('Tamanho da lista em bytes:', sys.getsizeof(lista))
print('Tamanho do generator em bytes:', sys.getsizeof(generator))

# É uma maneira de não salvar a lista toda na memória
print()
print(next(generator))
print(next(generator))
print()
for n in generator:
    print(n)

# Generator não sabe o tamanho, nada