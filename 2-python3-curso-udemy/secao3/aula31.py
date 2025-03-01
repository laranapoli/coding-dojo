"""
id = Identidade -> Como o python busca elementos na memória

As vezes queremos saber se o interpretador passou por determinado local.

"""
# Como o python tenta ser eficiente, o lugar na memória é o mesmo!
v1 = 'a'
v2 = 'a'

print(id(v1))
print(id(v2))

# Demarcar se passou em determinado local:
condicao = True
passou_no_if = None

if condicao:
    passou_no_if = True
else:
    print('não passou')


print(passou_no_if, passou_no_if is None)
print(passou_no_if, passou_no_if is not None)