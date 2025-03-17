""" TRY EXCEPT ELSE FINALLY"""

try:
    print('Executa try')
    10 / 0
except:
    ...
else:
    print('else')
finally: # O finally SEMPRE será executado, mesmo que ocorra um erro
    print('Executa finally')


for i in range(3):
    print(i)
else:
    print('else')