"""
args - Argumentos não nomeados
* - *args (empacotamento e desempacotamento)
"""

# Lembrando o desempacotamento:
x, y, *resto = 1, 2, 3, 4, 'a'
print(x, y, resto)

# x e y = desempacotamento
# resto = empacotamento

# def soma(x, y):
#     return x + y

def soma(*args):
    print(args, type(args)) # args EMPACOTA tudo enviado para função em uma tupla
    total = 0
    for arg in args:
        total += arg
    
    return total


soma(1, 2, 3, 4, 5, 6) # Não gera erro pq a função soma está EMPACOTANDO tudo em args

soma_xpto = soma(1, 2, 3)
print(soma_xpto)

# Função do python de soma
print(sum((1, 2, 3)))

# A chamada abaixo gera erro pq a função recebe uma tupla dentro de outra tupla
numeros = 1, 2, 3  # Isso define uma tupla
# soma(numeros)

# A maneira correta de fazer isso é desempacotar
soma(*numeros) # DESEMPACOTA uma tupla para enviar como parâmetros para função