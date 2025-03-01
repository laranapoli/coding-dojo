"""
CÁLCULO DO PRIMEIRO DÍGITO DO CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF
Multiplicando cada um dos valores por uma 
contagem regressiva começando de 10

Ex.: 746.824.890-70
   10  9  8  7  6  5  4  3  2
   7   4  6  8  2  4  8  9  0
   70  36 48 56 12 20 32 27 0

Somar todos os resultados:
70+36+48+56+12+20+32+27+0 = 301

Multiplicar o resultado anterior por 10
301 * 10 = 3010

Obter o resto da divisão da conta anterior por 11
3010 % 11 = 7

Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    o resultado é o valor da conta

O primeiro dígito do CPF é 7

CÁLCULO DO SEGUNDO DÍGITO DO CPF

Colete a soma dos 9 primeiros dígitos do CPF,
MAIS O PRIMEIRO DÍGITO, multiplicando cada um 
dos valores por uma contagem regressiva começando
de 11

- Somar todos os resultados

- Multiplicar o resultado anterior por 10

- Obter a divisão do resultado anterior por 11

- Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta
"""
import numpy as np

cpf_entrada = '14488125778'
cpf_fmt = cpf_entrada.replace('.', '').replace('-', '')
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

if cpf_entrada == cpf_gerado:
    print(f'{cpf_entrada=} é valido')