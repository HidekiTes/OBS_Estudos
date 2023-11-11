'''
Como importar coisas do seu prórpio módulo 
(ponto de vista do __main__)
'''
# nos caminhos de sys.path

import aula_40_m
from aula_40_m import soma, variavel_modulo

print('Este módulo se chama', __name__)
# print('Este módulo se chama', __name__)
print(aula_40_m.variavel_modulo)
print(variavel_modulo)
print(soma(2, 3))
print(aula_40_m.soma(2, 3))