"""
Cuidados com dados mutáveis
= - copiado o valor (imutáveis)
= - aponta para o mesmo valor na memória (mutável)
"""

nome = 'Luiz'  # Será coletado pelo garbage collector
nome = 'João'

lista_a = ['Luiz', 'Maria']
lista_b = lista_a  # Apontará para o mesmo valor na memória

print('Lista b criada:', lista_b)

lista_a[0] = 'elemento_alterado_em_a'

print('Lista b após alteração em a: ', lista_b)

# Para criar nova lista em outro local na memória:
lista_b = lista_a.copy()

