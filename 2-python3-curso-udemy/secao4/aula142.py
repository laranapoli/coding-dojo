lista = [
    'a', 1, 1.1, True, [0, 1, 2], (1, 2),
    {0, 1}, {'nome': 'Luiz'},
]

for item in lista:
    if isinstance(item, set):
        item.add(5)
        print(item, isinstance(item, str))

    if isinstance(item, (int, float)):
        print('NUM')
        print(item, item * 2)