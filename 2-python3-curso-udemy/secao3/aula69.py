""" while/else 
Para executar o bloco de código quando sai do while
(Nos casos em que não há ocorrência de break)
"""

string = 'Valorqualquer'

i = 0

while i < len(string):
    letra = string[i]

    print(letra)

    i += 1

    if letra == ' ':
        print('Espaço em branco encontrado!')
        break
else:
    print('Espaço em branco não encontrado!')
