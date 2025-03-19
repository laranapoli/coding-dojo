"""
GROUPBY - Agrupando valores (itertools)
"""
from itertools import groupby

alunos = [
    {'nome': 'Luiz', 'nota': 'A'},
    {'nome': 'Letícia', 'nota': 'B'},
    {'nome': 'Fabrício', 'nota': 'A'},
    {'nome': 'Rosemary', 'nota': 'C'},
    {'nome': 'Joana', 'nota': 'D'},
    {'nome': 'João', 'nota': 'A'},
    {'nome': 'Eduardo', 'nota': 'B'},
    {'nome': 'André', 'nota': 'A'},
    {'nome': 'Anderson', 'nota': 'C'},
]

# alunos = ['a', 'a', 'b', 'c', 'a']  # É necessário que os dados estejam ordenados

ordena = lambda a: a['nota']

alunos_ordenados = sorted(alunos, key=ordena)
# print(alunos_ordenados)


grupos = groupby(alunos_ordenados, key=ordena)

for chave, grupo in grupos:
    print(chave)
    for aluno in grupo:
        print(aluno)
    print()