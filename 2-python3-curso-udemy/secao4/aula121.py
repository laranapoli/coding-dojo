"""
MÉTODOS ÚTEIS DOS DICIONÁRIOS
- len - quantas chaves
- keys - iterável com as chaves
- values - iterável com valores
- items - iterável com chaves e valores
- setdefault - adiciona valor se a chave não existe
- copy - retorna uma cópia rasa
- get- obtém uma chave
- pop - apaga um item com a chave especificada (del)
- popitem - apaga o último item adicionado
- update - atualiza um dicionário com outro
"""

pessoa = {
    'nome': 'Lara',
    'sobrenome': 'Nápoli',
    'sobrenome': 'Marques',
}

print(f'Len: {pessoa.__len__()}')

print(f"Get chave repetida - retorna a última: {pessoa.get('sobrenome')}")

print(f"Keys: {pessoa.keys()}") # Retorna um dict_keys

print(f"Values: {pessoa.values()}") # Retorna um dict_values

print(f"Items: {pessoa.items()}") # Retorna um dict_items

print('Set Default: Atribui nova chave ao dict (se ela já não existir)')
pessoa.setdefault('idade', 18)
print(pessoa)

print('---------------------------------')

# Shallow copy - cópia rasa 
# Faz a cópia efetiva apenas de valores imutáveis 
# Se tiver uma lista dentro do dicionário, o '.copy()' 
# criará apenas um reapontamento! (2 dicts apontando 
# para a mesma lista)

d1 = {
    'c1': 1,
    'c2': 2,
    'l1': [0, 1, 2],
}
d2 = d1.copy()

d2['c1'] = 'outro valor'
d2['l1'][1] = 999999

print(d1)
print(d2)

# Para fazer uma cópia profunda, usar o módulo copy
print('---------------------------------')
print('Mesmo código, mas criando um deep copy')
import copy

d1 = {
    'c1': 1,
    'c2': 2,
    'l1': [0, 1, 2],
}
d2 = copy.deepcopy(d1)

d2['c1'] = 'outro valor'
d2['l1'][1] = 999999

print(d1)
print(d2)

print('---------------------------------')
print('pop - elimina chave, mas atribui a variável')
print("pessoa.pop('nome')")
nome = pessoa.pop('nome')
print(f'{nome=}')

print('---------------------------------')
print('popitem - elimina última chave, tb atribui a variável')
print("ultima_chave = pessoa.popitem()")
ultima_chave = pessoa.popitem()
print(f'{ultima_chave=}')

print('---------------------------------')
print('Update: Atualiza o dicionário:')
pessoa.update({
    'sobrenome': 'novo valor',
    'nome': 'novo valor' # Se não existir, cria nova chave
})
pessoa.update(nome='Novo valor', idade=27)
print(f"{pessoa=}")

# Update também pode receber um iterável (tupla de tuplas ou lista de listas)