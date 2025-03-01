frase = 'O Python é uma linguagem de programação '\
    'multiparadigma. '\
    'Python foi criado por Guido van Rossum.'
    
i = 0
caractere_mais_comum = ''
qtd_caractere_mais_comum = 0

while i < len(frase):
    letra_atual = frase[i]

    if letra_atual == ' ':
        i += 1
        continue

    qtd_letra_atual = frase.count(letra_atual)

    if qtd_letra_atual > qtd_caractere_mais_comum:
        qtd_caractere_mais_comum = qtd_letra_atual
        caractere_mais_comum = letra_atual

    print(f'A letra atual "{letra_atual}" aparece {qtd_letra_atual} veze(s).')

    i += 1

print(
    f'A letra mais comum na frase é "{caractere_mais_comum}", '
    f'pois aparece {qtd_caractere_mais_comum} vezes.'
)