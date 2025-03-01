"""
Listas em Python

- Mutável
- Suporta valores de qualquer tipo
- Índices e fatiamento
- Se a lista estiver vazia = False
- Métodos úteis:
    append, 
    insert: Recebe 2 argumentos: índice e valor a ser inserido
    pop, del, clear, extendm +

- Create Read Update Delete = CRUD
- Lista é mais útil para add e remover coisas do final dela! 
    Fazer isso com intermediários = O(n)
"""

lista = [10, 20, 30, 40]
print('Lista original: ', lista)

del lista[2]

print('Resultado do del lista[2]: ', lista)

lista.append(50)

print('Resultado do append(50): ', lista)

lista.pop() # Retorna o item removido

print('Resultado do pop(): ', lista)

lista.pop(1) # Pode remover intermediários, mas tem o problema do custo computacional

print('Resultado do pop(1): ', lista)

lista.insert(1, 20)

print('Resultado do insert(1, 20): ', lista)