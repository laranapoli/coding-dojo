"""
MÓDULOS PRÓPRIOS

- O primeiro módulo executado chama-se __main__
- O python conhecce a pasta onde __main__ está e as pastas abaixo dele
- Por padrão: NÃO reconhece pastas e módulos acima do __main__
- O python conhece todos os módulos e pacotes presentes nos caminhos de sys.path
- PASTAS no python são chamadas de PACOTES quando existem MÓDULOS lá dentro
"""
import sys

print('Esse módulo se chama', __name__)
print(*sys.path, sep='\n')
print()

import aula153

print('O módulo da aula 153 se chama', aula153.__name__)

# Import variável
print('Variável importada do módulo da aula 153:', aula153.platform)