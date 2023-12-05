main.py
``` python
'''
DocStrings em funções (Documentação)

DocStrings de várias linhas
DocStrings em funções 
Docstrings em class
'''

# import uma_linha
# import varias_linhas
import documentando_funcoes

# print(dir(uma_linha))
# print(uma_linha.__doc__)
# print(uma_linha.__file__)
# print(uma_linha.__name__)
help(documentando_funcoes)
```

documentando_funcoes.py
```python
'''
Este é um módulo de exemplo
Este módulo contém funções e exemplos de documentação de funções.
A função soma você já conhece bastante.
'''
variavel_1 = 1

# def soma(x, y):


def soma(x: int | float, y: int | float) -> int | float:
    '''
    Soma x e y
    Este módulo contém funções e exemplos de documentação de funções.
    A função soma você já conhece bastante.
    :param x: Número 1
    :type x: int or float
    :param y: Número 2
    :type y: int or float
    :return: A soma entre x e y
    :rtype: int or float
    '''
    return x + y


def multiplica(
    x: int | float,
    y: int | float,
    z: int | float | None = None
) -> int | float:
    '''
    Multiplica x, y e/ou z
    Multiplica x e y. Se z for enviado, multiplica x, y, z.
    '''
    if z is None:
        return x * y
    return x * y * z


variavel_2 = 2
variavel_3 = 3
variavel_4 = 4
```