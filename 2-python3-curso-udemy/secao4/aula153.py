"""
- Importar um módulo inteiro não muda nada a performance do programa
    import sys

    > Vantagens: Você tem o namespace do módulo
    > Desvantagens: Nomes grandes

- Importar partes
    from sys import plataform

    > Vantagens: Nomes menores
    > Desvantagens: Sem o namespace do módulo (definir um novo valor para platform sobrescreve!)

- Alias:
    from sys import platform as plat

- MÁ PRÁTICA:
    from sys import *

    > Deixa tudo do módulo disponível - define várias coisas
"""

import sys
print(sys.platform)

print('------------')
from sys import platform

platform = 'xpto'

print(platform)

print('------------')
from sys import platform as plat

platform = 'xpto'

print(plat)

# sys.exit()
