"""
Operação ternária (condicional de uma linha)
<valor> if <condicao> else <outro valor>
"""

print('Valor' if True else 'Outro valor')
print('Valor' if False else 'Outro valor')

digito = 8

novo_digito = digito if digito <= 9 else 0
print(novo_digito)

print('Valor' if False else 'Outro valor' if True else 'Fim')