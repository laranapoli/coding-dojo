""" for loop 

- não é muito comum usar o while com coisas que sabemos quando termina
- o while é utilizado para quando não sabemos precisamente quantas repetições vão existir

"""

# senha_salva = '123456'
# senha_digitada = ''
# repeticoes = 0

# while senha_salva != senha_digitada:
#     senha_digitada = input(f'Sua senha ({repeticoes=}x): ')

#     repeticoes += 1

# print ('O laço acima pode ter repetições infinitas')
# print(repeticoes)

texto = 'Python'

novo_texto = ''

for letra in texto:
    print(letra)
    novo_texto += f'*{letra}'

print(novo_texto)