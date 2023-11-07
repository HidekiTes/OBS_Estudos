'''
Argumentos nomeados e argumentos posicionais (não nomeados)
em funções

Argumento nomeado tem nome com sinal de igual
Argumento não nomeado recebe apenas o argumento (valor)
'''

def soma(x, y, z):
    # Definição
    print(f'{x=} y={y} z={z}', '|', 'x+y+z=',x + y + z)

soma (1,2,3)
soma(1,y=2,z=5)
print(1,2,3, sep='-')