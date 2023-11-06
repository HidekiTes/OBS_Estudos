```python
'''
Formatação básica de strings

s - string
d - int
f - float
.<numero de digitos>f
x ou X - Hexadecimal
(Caractere)(><^)(quantidade)
> - Esquerda
< - Direita
^ - Centro
= - Força o numero a aparecer antes dos zeros
Sinal - + ou -
Ex. 0>-100,.1f
Conversion flags - !r !s !a
'''

variavel = 'ABC'
print(f'{variavel}')
print(f'{variavel: >10}')
print(f'{variavel: ^10}.')
print(f'{variavel: <10}.')
print(f'{1000.8927348239:0=+10,.1f}')
print(f'O Hexadecimal de 1500 é {1500:08X}')
print(f'{variavel!r}') #Vamos estudar depois
```