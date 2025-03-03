"""
SETS
Representados graficamente pelo diagrama de Venn

- São mutáveis, pórem aceitam apenas tipos imutáveis
- Não garante a ordem
- São muito eficientes para remover duplicatas de iteráveis!
- Sets não tem índices
- São iteráveis (for, in, not in)

MÉTODOS ÚTEIS:
- add
- update
- clear
- dicard
"""

s1 = set('Lara')
print(s1, type(s1))

# s2 = {1, 2, 3, [123]} # TypeError: unhashable type: 'list' - tipo mutável
# print(s2)

# Pelo set não ter índice, o código abaixo retorna erro
# print(s1[1])

print('L' in s1)

# Método add
print('----------', "s1.add('Luiz')", '----------')
s1.add('Luiz') # Só aceita UM valor
print(s1)

print('----------', "s1.update('Luiz')", '----------')
print('Adiciona de forma iterada')
s1.update('Luiz')
print(s1)

print('----------', "s1.update(('valor', 1, 2, 3))", '----------')
print('Update pode ser usado para enviar vários valores!')
s1.update(('valor', 1, 2, 3))
print(s1)

print('----------', "s1.discard('L')", '----------')
print('discard descarta um valor específico')
s1.discard('L')
print(s1)

print('----------', "s1.clear()", '----------')
print('clear vai limpar o set!')
s1.clear()
print(s1)

# Operadores úteis: 
# união | união 
# intersecção & (intersection) - Itens presentes em ambos 
# diferença - Itens presentes apenas no set da esquerda 
# diferença simétrica ^- Itens que não estão em ambos
s2 = {1, 2, 3}
s3 = {2, 3, 4}
print(f'{s2 | s3=}')
print(f'{s2 & s3=}')
print(f'{s2 - s3=}')
print(f'{s3 - s2=}')
print(f'{s2 ^ s3=}')


