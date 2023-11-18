'''
Recarregando módulos, importlib e singleton
'''
import importlib

import aula_41_m

print(aula_41_m.variavel)

for i in range(10):
    importlib.reload(aula_41_m)
    print(i)

print('Fim')