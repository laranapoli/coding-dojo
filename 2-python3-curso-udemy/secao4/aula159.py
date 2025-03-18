"""
DUNDER INIT

- Packages podem ser inicializados com o arquivo dunder init
- Esse arquivo é executado assim que o package é importado
- Posso "enganar" o python importando funções do módulo no dunder init
- O dunder init é um local onde o import * não é uma má prática
"""

import aula157_package
from aula157_package import fala_oi

fala_oi()