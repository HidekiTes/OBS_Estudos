```python
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
```

Arquivo dentro de uma pasta - aula43_package/modulo.py
```python
# __all__ = [
# 'variavel',
# 'soma_do_modulo',
# 'nova_variavel',
# ]
from aula43_package.modulo_b import fala_oi
  
variavel = 'Alguma coisa'
  
def soma_do_modulo(x, y):
return x + y

  
nova_variavel = 'OK'
# fala_oi()
```

Arquivo dentro de uma pasta - aula43_package/modulo_b.py
```python
def fala_oi():
print('oi')
```