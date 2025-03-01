nome = input("Digite seu nome: ")
idade_str = input("Digite sua idade: ")

if len(nome) == 0 or len(idade_str) == 0:
    print("Desculpe, você deixou campos vazios.")
else:
    idade_int = int(idade_str)

    print(f'Seu nome é {nome}')
    print(f'Seu nome invertido é {nome[::-1]}')
    
    if ' ' in nome:
        print('Seu nome contém whitespaces.')
    else:
        print('Seu nome não contém whitespaces.')

    print(f'Seu nome tem {len(nome)} letras')
    print(f'A primeira letra do seu nome é {nome[0]}')
    print(f'A última letra do seu nome é {nome[-1]}')
