"""CONTINUAÇÃO - CPF"""
"""
CONTINUAÇÃO - CÁLCULO DO PRIMEIRO DÍGITO DO CPF
- Solução utilizando lib 're' para tratar entrada!
"""
import numpy as np
import random
import sys


nove_digitos = ''

for i in range(9):
    nove_digitos += str(random.randint(0,9))

int_nove_digitos = list(map(int, nove_digitos))

# primeiro dígito
cont_regressiva = np.array([i for i in range(10,1,-1)])

array_cpf_9 = np.array(int_nove_digitos)

primeiro_digito = (sum(array_cpf_9*cont_regressiva) * 10) % 11

primeiro_digito = 0 if primeiro_digito > 9 else primeiro_digito

# segundo dígito
cont_regressiva = np.array([i for i in range(11,1,-1)])

array_cpf_10 = np.array(int_nove_digitos[0:9] + [primeiro_digito])

segundo_digito = (sum(array_cpf_10 * cont_regressiva) * 10) % 11

segundo_digito = 0 if segundo_digito > 9 else segundo_digito

nove_dig_str = ''.join(map(str,nove_digitos))

cpf_gerado = f'{nove_dig_str}{primeiro_digito}{segundo_digito}'

print(cpf_gerado)