"""
FUNÇÕES RECURSIVAS E RECURSIVIDADE
- Recursividade = algo que se chama de volta / função que pode se chamar
- Úteis para dividir problemas grandes em partes menores
- Toda função recursiva deve ter:
    - Um problema que possa ser dividido em partes menores
    - Um caso recursivo que resolve o pequeno problema
    - Um caso base que para a recursão
- Fatorial: 5! = 5 * 4 * 3 * 2 * 1 = 120

- Toda vez que usamos funções recursivas, o escopo inteiro está sendo salvo na call stack
    - Por isso é possível ocorrer RecursionError por stack overflow
"""

def recursiva(inicio=0, fim=10):
    # Caso base:
    if inicio >= fim:
        return fim
    
    # Caso recursivo: Contar até chegar ao final
    print(inicio)
    inicio += 1
    return recursiva(inicio, fim)

# recursiva()

def fatorial(n):
    # Caso base
    if n <= 1:
        return 1
    
    return n* fatorial(n - 1)

print(fatorial(5))

