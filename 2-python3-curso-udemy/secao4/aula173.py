"""
COUNT É UM ITERADOR SEM FIM
- Muito similar ao range, mas o range finaliza
- Está no módulo itertools
"""
from itertools import count

c1 = count(16, 8)  # Possível passar início e step
r1 = range(16, 100, 8)

print('c1 - iter', hasattr(c1, '__iter__'))  # Se tem o método iter, garante que é um iterável
print('c1 - next', hasattr(c1, '__next__'))  # É um iterator pq tem o método next

print('r1 - iter', hasattr(r1, '__iter__'))  # Se tem o método iter, garante que é um iterável
print('r1 - next', hasattr(r1, '__next__'))  # É um iterável, mas não um iterator (pq ñ tem next)

print('count')
for i in c1:
    if i > 99:
        break
    print(i)

print()
print('range')
for i in r1:
    print(i)