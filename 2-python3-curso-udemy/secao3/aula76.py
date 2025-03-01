"""
Faça um jogo para o usuário adivinhar qual a palavra secreta.
- Você vai propor uma palavra secreta qualquer e dar 
a possibilidade para o usuário digitar apenas uma letra.
- Quando o usuário digitar uma letra, você vai conferir se 
a letra digitada está na palavra secreta.
    - Se a letra digitada estiver na palavra secreta, exibe
    a letra;
    - Se a letra não estiver, exiba *.
- Faça a contagem de tentativas do seu usuário.
"""
import os

palavra_secreta = 'teste'

palavra_adivinhada = len(palavra_secreta) * '*'

lista_letras_palavra_adivinhada = list(palavra_adivinhada)

tentativas = 0

while '*' in palavra_adivinhada:
    letra_inserida = input('Insira a letra desejada: ')

    if len(letra_inserida) > 1:
        print('Digite apenas uma letra!')
        continue

    tentativas += 1

    if letra_inserida in palavra_secreta:
        for i in range(len(palavra_secreta)):
            if letra_inserida == palavra_secreta[i]:
                lista_letras_palavra_adivinhada[i] = palavra_secreta[i]
                palavra_adivinhada = ''.join(lista_letras_palavra_adivinhada)

    print(f'Atualmente a palavra divinhada é: {palavra_adivinhada}')

os.system('clear')
print(f'Você acertou a palavra com {tentativas} tentativas válidas (apenas 1 letra).')