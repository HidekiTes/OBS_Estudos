```python
'''  
Formatação de Strings com f-strings  
'''  
  
nome = 'Pedro L'  
altura = 1.69  
peso = 45  
imc = peso / altura ** 2 # ... pode ser usado como placeholder  
  
# f (f-strings) antes de strings permitem a inclusão de variáveis  
linha_1 = f'{nome} tem {altura:.2f} de altura'linha_2 = f'pesa {peso} kg e seu imc é: {imc:.2f}'  
  
print(linha_1)  
print(linha_2)  
  
# Pedro Luiz tem 1.69 de altura, pesa 45 kg  
# e seu IMC é 9832579872357
```