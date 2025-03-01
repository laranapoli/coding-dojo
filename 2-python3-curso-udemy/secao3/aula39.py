"""Iterando strings com while"""

nome = 'Lara Nápoli'
nova_string = ''
tamanho_nome = len(nome)
contador = 0

while contador < tamanho_nome:
    nova_string += f'*{nome[contador]}'

    contador += 1

    print(nova_string)