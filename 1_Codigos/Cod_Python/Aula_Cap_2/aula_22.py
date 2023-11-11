'''
Empacotamento e desempacotamento de dicionarios
'''
a,b = 1,2
a,b = b,a
# print(a,b)

pessoa = {
    'nome':'Aline',
    'sobrenome':'Souza',
}

dados_pessoa = {
    'idade': 16,
    'altura': 1.6,
}

pessoas_completa = {**pessoa, **dados_pessoa}
# print(pessoas_completa)

# args e kwargs
# args (já vimos)
# kwargs - keyword arguments (argumentos nomeados)
def mostro_argumentos_nomeados(*args, **kwargs):
    print('Não Nomeados:',args)

    for chave, valor in kwargs.items():
        print(chave,valor)

# mostro_argumentos_nomeados(1,2,nome='Joana',qlq=123)
# mostro_argumentos_nomeados(**pessoas_completa)

configurações = {
    'arg1':1,
    'arg2':2,
    'arg3':3,
    'arg4':4,
}
mostro_argumentos_nomeados(**configurações)

