'''
While e Break - Estrutura de Repetição

Repetições
while(enquanto)
Executa uma ação equanto uma condição for verdadeira
'''
condicao = True

while condicao:
    nome = input('Qual o seu nome: ')
    print(f'Seu nome é {nome}')

    if nome == 'sair':
        break

print('Acabou')

