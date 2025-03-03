"""
Closure e funções que retornam outras funções
Usada no paradigma de programação PROGRAMAÇÃO FUNCIONAL
"""

def criar_saudacao(saudacao):
    def saudar(nome):
        return f'{saudacao}, {nome}'
    return saudar

falar_bom_dia = criar_saudacao('Bom dia') # Temos uma função criando outra função
falar_boa_noite = criar_saudacao('Boa noite')

print(falar_bom_dia('Lara'))
print(falar_boa_noite('Lara')) # Isso é closure (fechamento)