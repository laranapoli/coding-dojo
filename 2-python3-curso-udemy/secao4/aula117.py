"""
Exercício
Crie funções que duplicam, triplicam e quadruplicam
o número recebido como parâmetro
"""

def operacao(valor):
    def multiplicar(numero):
        return numero * valor
    return multiplicar

duplica = operacao(2)
triplica = operacao(3)
quadruplica = operacao(4)

print(duplica(4))
print(triplica(4))
print(quadruplica(4))