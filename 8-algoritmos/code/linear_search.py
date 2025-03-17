"""
Big O - Tempo
- Pior caso: Elemento na última posição ou fora da lista => O(n)
- Melhor caso: Elemento na primeira posição => O(1)
- Caso médio: O(n)

Big O - Espaço
- Quantidade é fixa na memória, independente do tamanho da lista => O(1)
"""

def linear_search(input_list, target):
    for i in range(len(input_list)):
        if input_list[i] == target:
            return f"Found target at position {i}"
    return "Element not found"


numeros = [4, 9, 15, 10]

print(linear_search(numeros, 9))
print(linear_search(numeros, 20))
