'''
Operador Lógico "or"

and (e) or (ou) not (não)
or - Qualquer condição verdadeira avalia toda a expressão
como verdadeira.
Se qualquer valor for considerado verdadeiro, A expressão
inteira será avaliada naquele valor.
São considerados falsy (que você já viu)
0 0.0 '' False
Também existe o tipo None que é usado para representar um
não valor
'''

entrada = input ('[E]ntrar [S]air: ')
senha_digitada = input('Senha: ')

senha_permitida = '123456'

# if True:
if (entrada == 'E' or entrada == 'e') and senha_permitida == senha_permitida:
    print('Entrar')
else:
    print('Sair')

# Avaliação de Curto Circuito #1
# Caso tenha um verdadeiro de inicio, ela será verdadeira
# Ela irá reconhecer o primeiro valor
# print(True and 0 and False or 'abc')

# Avaliação de Curto Circuito #2
# Estrutura de If simplificada
# senha = input('Senha: ') or 'Sem Senha'
# print(senha)


