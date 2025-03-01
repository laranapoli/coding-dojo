"""
FORMATAÇÃO BÁSICA DE STRINGS

Conversion flags
!r - __repr__
!s - __str__
!a -
"""

# padding: preenchimento a esquerda ou direita
variavel = 'ABC'
print(f'{variavel:0>10}.')
print(f'{variavel:0<10}.')
print(f'{variavel:0^10}.')

# Conversion flags
print(f'{variavel!r}')

# Separação do milhar com vírgula e aparecer sinal
number = -1000.7864378
print(f'{number:+,.1f}')

# Hexadecimal
print(f'O hexadecimal de 1500 é {1500:08x}')
print(f'O hexadecimal de 1500 é {1500:08X}')