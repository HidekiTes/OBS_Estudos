```python
'''
Introdução aos Packages (pacotes em Python)
'''
from sys import path
# Nome da Pasta - Nome do arquivo
import aula42_package.modulo
from aula42_package import modulo
from aula42_package.modulo import *
  
# from aula99_package.modulo import soma_do_modulo
  
# print(*path, sep='\n')
print(soma_do_modulo(1, 2))
print(aula42_package.modulo.soma_do_modulo(1, 2))
print(modulo.soma_do_modulo(1, 2))
print(variavel)
print(nova_variavel)
```

Arquivo dentro de uma pasta - aula42_package/modulo.py
```python
# __all__ = [
# 'variavel',
# 'soma_do_modulo',
# 'nova_variavel',
# ]
  
variavel = 'Alguma coisa'

  
def soma_do_modulo(x, y):
return x + y


nova_variavel = 'OK'
```