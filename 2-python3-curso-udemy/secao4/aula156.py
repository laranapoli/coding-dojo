"""
SINGLETON = Só pode existir uma instância daquela coisa

- Quando importamos módulo, Python salva na memória 
para não importar de novo futuramente
"""
import importlib

import aula153

for i in range(10):
    print(i)
    import aula153
    # Se quiser recarregar:
    importlib.reload(aula153) 