"""
OPERADORES DE ATRIBUIÇÃO

+=
-=
*=
/=
//=
**=
%=
"""

# continuando while

contador = 0

while contador <= 20:
    contador += 1
    

    if contador == 3:
        print(f'Não vou mostrar o {contador}')
        continue

    print(contador)

    if contador == 10:
        break  # Finaliza o laço



