"""
Assim como no else, também podemos usar continue, break e else no for loop
"""

for i in range(10):
    if i == 2:
        print('i é 2, pulando...')
        continue

    # if i == 8:
    #     print('i é 8, seu else não executará')
    #     break

    for j in range(1, 3):
        print(i, j)
else: # só executa se nada quebrar a execução no meio do caminho!
    print('For completo com sucesso!')