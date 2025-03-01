"""
CONTINUAÇÃO - CÁLCULO DO PRIMEIRO DÍGITO DO CPF
- Solução utilizando lib 're' para tratar entrada!
"""
import numpy as np
import re
import sys


cpf_entrada = '144.881.257-78'
cpf_fmt = re.sub(
    r'[^0-9]',
    '',
    cpf_entrada
)

if len(set(cpf_fmt)) == 1:
    print('Você enviou dados sequenciais')
    sys.exit()

list_digitos_cpf = list(map(int, list(cpf_fmt)))

# primeiro dígito
cont_regressiva = np.array([i for i in range(10,1,-1)])

nove_digitos = list_digitos_cpf[0:9]

array_cpf_9 = np.array(nove_digitos)

primeiro_digito = (sum(array_cpf_9*cont_regressiva) * 10) % 11

primeiro_digito = 0 if primeiro_digito > 9 else primeiro_digito

# segundo dígito
cont_regressiva = np.array([i for i in range(11,1,-1)])

array_cpf_10 = np.array(list_digitos_cpf[0:9] + [primeiro_digito])

segundo_digito = (sum(array_cpf_10 * cont_regressiva) * 10) % 11

segundo_digito = 0 if segundo_digito > 9 else segundo_digito

nove_dig_str = ''.join(map(str,nove_digitos))

cpf_gerado = f'{nove_dig_str}{primeiro_digito}{segundo_digito}'


if cpf_fmt == cpf_gerado:
    print(f'{cpf_entrada=} é valido')