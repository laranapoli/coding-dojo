# Exercício - Sistema de perguntas e respostas

perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
]

acertos = 0

for pergunta in perguntas:
    print(f"Pergunta: {pergunta.get('Pergunta')}")

    opcoes = pergunta.get('Opções')
    for i, opcao in enumerate(opcoes):
        print(f'{i}) {opcao}')

    resposta = input('Escolha uma opção: ')

    resposta_int = None
    qtd_opcoes = len(opcoes)
    acertou = False

    if resposta.isdigit():
        resposta_int = int(resposta)

    if resposta_int is not None:
        if resposta_int >= 0 and resposta_int < qtd_opcoes:
            if opcoes[resposta_int] == pergunta['Resposta']:
                acertou = True
    
    if acertou:
        acertos += 1
        print('Acertou!')
    else:
        print('Errou!')

print(f'Você acertou {acertos} de {len(perguntas)} perguntas!')
