"""
Imprecisão de números de ponto flutuante
"""

numero_1 = 0.1
numero_2 = 0.7
numero_3 = numero_1 + numero_2

print(numero_3)

# Maneira 1 de resolver: Formatar o resultado final
print(f'{numero_3:.2f}')

# Maneira 2:
print(round(numero_3, 3))

# Maneira 3: Usado para quando temos um número com muitas 
# casas decimais e o programa depende dessa precisão

import decimal

numero_1 = decimal.Decimal('0.1') # É necessário passar como string pq se não o Python salva em memória como float
numero_2 = decimal.Decimal('0.7')
numero_3 = numero_1 + numero_2
print(numero_3)