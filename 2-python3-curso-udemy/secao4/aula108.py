"""
Escopo de funções
Escopo significa o local que aquele código pode atingir.
Existe o escopo global e local.
O escopo global é o escopo onde todo o código é alcançável.
O escopo local é o escopo onde apenas nomes do mesmo local
podem ser alcançados.
Não temos acesso a nomes de escopos internos nos escopos
externos.
A palavra 'global' faz uma variável do escopo externo ser
a mesma no escopo interno.
Tudo que está dentro da função, está protegido!
"""

# O que eu faço na função, fica na função

var_escopo_global = 1

def escopo(): # Parâmetros da função fazem parte do escopo da função
    # Para manipular a variável do escopo de fora, declara ela como global
    global var_escopo_global  # global é uma má prática
    var_escopo_global = 'xpto'

    print(var_escopo_global) # Isso é uma má prática de programação

    def outra_funcao():
        ...
        # Só é possível acessar elementos do escopo de fora

print(var_escopo_global)
escopo()
print(var_escopo_global)