```python
'''
__init__.py é um arquivo de inicialização dos packages em Python
'''
# from sys import path
# https://stackoverflow.com/questions/2386714/why-is-import-bad
  
# import aula44_package.modulo
# from aula44_package import modulo
# print(modulo.soma_do_modulo(1, 2))
# print(variavel)
# print(nova_variavel)
# from aula44_package.modulo import fala_oi, soma_do_modulo
  
# print(__name__)
# fala_oi()
  
from aula44_package import falar_oi, soma_do_modulo
  
print(soma_do_modulo(2, 3))
falar_oi()
```

Arquivo dentro de uma pasta - aula44_package/`__init__`.py
```python
from aula44_package.modulo import *
from aula44_package.modulo_b import *
```

Arquivo dentro de uma pasta - aula44_package/modulo.py
```python
# __all__ = [
# 'variavel',
# 'soma_do_modulo',
# 'nova_variavel',
# ]
# from aula44_package.modulo_b import fala_oi
  
variavel = 'Alguma coisa'
  
def soma_do_modulo(x, y):
return x + y
```

Arquivo dentro de uma pasta - aula44_package/modulo_b.py
```python
def fala_oi():
print('oi')
```