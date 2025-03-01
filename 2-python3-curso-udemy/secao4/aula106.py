"""
Argumentos nomeados e não nomeados em funções
Argumento nomeado tem nome com sinal de igual
Argumento não nomeado recebe apenas o argumento (valor) = POSICIONAL
"""

def soma(x, y):
    # Definição
    print(f'{x=} {y=} | x + y =', x + y)

# print(soma(1, 2)) # Isso retorna um 'bug' pq a função soma retorna None

soma(1, 2) # Exemplo de argumentos não nomeados (posicionais)
soma(y=2, x=1)  # Usando argumentos nomeados

# A partir do momento em que nomeamos um parâmetro na chamada da função, 
# todos os subsequentes precisam ser nomeados também