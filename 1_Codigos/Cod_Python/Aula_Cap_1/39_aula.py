'''
Tipo list - Introdução as listas mutáveis em Python

Listas em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis: append, insert, pop, del, clear, extend, +
'''
#        +01234
#        -54321
string = 'ABCDE'  # 5 caracteres (len)
# print(bool([])) # falsy
# print(lista, type(lista))


lista = [123, True, 'Luiz Otavio', 1.2, []]
lista[-3] = 'Pedro'
print(lista )
print(lista[2].upper, type(lista[2]))
