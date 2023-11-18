'''
O ponto de vista do __main__ pode te confundir em módulos e pacotes Python
'''
# from sys import path

# import aula43_package.modulo
# from aula43_package import modulo
# from aula43_package.modulo import *

# # from aula43_package.modulo import soma_do_modulo

# # print(*path, sep='\n')
# print(soma_do_modulo(1, 2))
# print(aula43_package.modulo.soma_do_modulo(1, 2))
# print(modulo.soma_do_modulo(1, 2))
# print(variavel)
# print(nova_variavel)
from aula43_package.modulo import fala_oi, soma_do_modulo

print(__name__)
fala_oi()