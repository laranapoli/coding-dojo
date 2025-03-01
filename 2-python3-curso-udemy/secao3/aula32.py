# Problema 1
numero_str = input("Digite um número inteiro: ")

if numero_str.isdigit():
    numero = int(numero_str)

    if (numero % 2) > 0:
        print("Número ímpar")
    else:
        print("Número par")
else:
    print('Você não digitou um número inteiro!')

# Problema 2
horas = input("Insira as horas: ")
hora = int(horas.split(':')[0])

if hora >= 18:
    print('Boa noite!')
elif hora >= 12:
    print('Boa tarde!')
else:
    print('Bom dia!')

# Problema 3
nome = input("Insira seu nome: ")
tamanho_nome = len(nome)

if tamanho_nome > 6:
    print("Seu nome é muito grande")
elif tamanho_nome >= 5:
    print("Seu nome é normal!")
else:
    print("Seu nome é curto.")