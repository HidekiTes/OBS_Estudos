'''
Operador Lógico "and"

and (e) or (ou) not (não)
and - Todas as condições precisam ser verdadeiras
Se qualquer valor for considerado falso, a expressão
inteira será avaliada naquele valor
São consideradas falsy
0 0.0 '' false
Também existe o tipo None que é usado para representar
um não valor
'''

entrada = input ('[E]ntrar [S]air: ')
senha_digitada = input('Senha: ')

senha_permitida = '123456'

# if True:
if entrada == 'E' and senha_permitida == senha_permitida:
    print('Entrar')
else:
    print('Sair')

# Avaliação de curto circuito
# Caso tenha um False, ela para e considera como false
# print(True and True and True)
# print(True and True and False)


