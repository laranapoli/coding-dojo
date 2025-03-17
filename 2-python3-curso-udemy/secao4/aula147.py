"""
INTRODUÇÃO ÀS GENERATOR FUNCTIONS EM PYTHON
- Toda função que tem o "yield" é uma generator function
- O "return" da função com yield funciona como um raise
stop iteration
"""

def generator(n=0):
    yield 1 # Pausar
    print('Continuando...')
    yield 2 # Pausar
    print('Mais uma vez...')
    yield 3 # Pausar
    print('Vou terminar!!')
    return 'ACABOU'

gen = generator(n=0)
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
for n in gen:
    print(n)


def another_generator(n=0, maximum=10):
    while True:
        yield n
        n += 1
        
        if n>= maximum:
            return
        
genn = another_generator()
for n in genn:
    print(n)

print()
print()
print('----------------------------')
print()
print()

# Yield from
def gen1():
    yield 1
    yield 2
    yield 3

def gen2():
    yield from gen1()
    yield 4
    yield 5
    yield 6


g = gen2()
for numero in g:
    print(numero)