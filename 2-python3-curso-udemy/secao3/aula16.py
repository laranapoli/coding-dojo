# OS CONDICIONAIS
# if / elif / else

# Strings com algum valor retornam true
print(bool('a'))
# Strings vazias retornam false
print(bool(''))

opcao = input('Você quer entrar ou sair? ')

if opcao == 'entrar':
    print('Você entrou!')
elif opcao == 'sair':
    print('Você saiu!')
else:
    print('Opção inválida!')
