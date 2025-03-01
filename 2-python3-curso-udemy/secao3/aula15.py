# A FUNÇÃO INPUT
nome = input('Qual o seu nome? ')

# passar o nome da variável + '=' mostra o nome da variável e o valor dela
print(f'O seu nome é {nome=}.')

idade = int(input(f'Qual a sua idade, {nome}? '))

print(f'{nome} tem {idade=} anos.')
print(type(idade))

# A função input sempre retorna uma string!
