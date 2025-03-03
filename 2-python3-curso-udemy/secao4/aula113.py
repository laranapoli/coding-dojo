"""
EXERCÍCIO COM FUNÇÕES

Crie uma função que multiplica todos os argumentos
não nomeados recebidos. 
Retorne o total para uma variável e mostre o valor 
da variável.

Crie uma função que fala se o número é par ou ímpar.
Retorne se o número é par ou ímpar.
"""
# Minha resolução:
def multiplicacao(*args):
    resultado = 1
    for arg in args:
        resultado *= arg

    return resultado

r_mult = multiplicacao(1, 2, 3, 4)
print(r_mult)
print(1*2*3*4)

def is_impar(numero):
    if numero % 2 == 0:
        return 'Par'
    return 'Ímpar'


print(is_impar(6))
print(is_impar(7))


# Resolução do professor
def multiplicar(*args):
    total = 1
    for numero in args:
        total *= numero
    return total

multiplicação = multiplicar(1, 2, 3, 4, 5)
print(multiplicação)


def par_impar(numero):
    multiplo_de_dois = numero % 2 == 0

    if multiplo_de_dois:
        return f'{numero} é par'
    return f'{numero} é ímpar'

print(par_impar(2))
print(par_impar(3))