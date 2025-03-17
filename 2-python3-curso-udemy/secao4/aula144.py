""" dir, hasattr e getattr"""

string = 'Lara'
metodo = 'upper'

if hasattr(string, metodo):
    print(f'Existe {metodo}')
    print(string.upper())
    print(getattr(string, metodo)())