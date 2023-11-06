```python
'''
Operadores in e not in

Strings são iteráveis (Iterável = Navegação individual)
0 1 2 3 4
P e d r o
5 4 3 2 1
'''

# nome = 'Pedro'
# print(nome[2])
# print(nome[-2])
# print('d' in nome)
# print('vio' in nome)
# print(10 * '-')
# print('dro' not in nome)
# print('vio' not in nome)

nome = input("Digite o seu nome: ")
encontrar = input('Digite o que deseja encontrar: ')

if encontrar in nome:
print(f'{encontrar} está em {nome}')
else:
print(f'{encontrar} não está em {nome}')
```