"""
INTRODUÇÃO AOS PACKAGES

- Todas as importações do PROGRAMA INTEIRO precisam ser acessíveis do ponto de vista do main
"""
from sys import path
print(__name__)

print(*path, sep='\n')
from aula157_package import modulo