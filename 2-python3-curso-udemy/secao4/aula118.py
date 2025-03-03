"""
DICIONÁRIOS (dict)
Dicionários são estruturas de dados do tipo
par chave e valor.
Chaves podem ser consideradas como o "índice"
que vimos na lista e podem ser de tipos imutáveis
como: str, int, float, bool, tuple, etc.
O valor pode ser de qualquer tipo, incluindo outro
dicionário.
Usamos as chaves - {} - ou a classe dict para criar
dicionários.
Imutáveis: str, int, float, bool, tuple
Mutável: dict, list

"""

pessoa = {
    'nome': 'Lara',
    'sobrenome': 'Nápoli',
    'enderecos': [
        {'rua': 'tal tal', 'número': 123}
    ]
}

print(pessoa['nome'])

for chave in pessoa:
    print(chave, pessoa[chave])

del pessoa['sobrenome']

for chave in pessoa:
    print(chave, pessoa[chave])

if pessoa.get('sobrenome') is None:
    print('CHAVE NÃO EXISTE')

print(pessoa.get('sobrenome', 'valor padrão'))