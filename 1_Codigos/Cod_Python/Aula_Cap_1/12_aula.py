'''
Formatação de Strings com o método format
'''

a = 'A'
b = 'B'
c = 1.1

# Caso dê erro de "out of range" o valor não existe
string = 'b={nome2} a={nome1} c={nome3:.2f}'
# Caso um parâmtero seja nomeado, os outros precisam também

formato = string.format(
    nome1=a,
    nome2=b,
    nome3=c)

print(formato)