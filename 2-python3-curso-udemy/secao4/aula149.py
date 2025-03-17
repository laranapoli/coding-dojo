"""
TRY EXCEPT
"""

try:
    a = 10
    b = 0
    print('antes da divisão')
    c = a/b[0]
    print('depois da divisão')
except ZeroDivisionError:
    print('caiu na exceção de divisão por zero')
except NameError:
    print('Caiu na exceção de Nome não definido')
except Exception as error: # Classe superior = trata qualquer erro
    print('ERRO DESCONHECIDO')
    print('msg:', error)
    print('Nome:', error.__class__.__name__)

print('CONTINUANDO FORA DO TRY-EXCEPT')