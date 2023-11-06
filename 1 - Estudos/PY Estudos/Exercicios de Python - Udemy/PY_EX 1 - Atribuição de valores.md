## Exercício de Informações Pessoais
Você foi fornecido com um código que contém informações pessoais de uma pessoa. Sua tarefa é criar um programa que imprima essas informações de maneira organizada. Use as variáveis nome, sobrenome, idade, ano_nascimento, maior_de_idade, e altura_metros para exibir os seguintes detalhes:

1. Imprima o nome da pessoa.
2. Imprima o sobrenome da pessoa.
3. Imprima a idade da pessoa.
4. Imprima o ano de nascimento da pessoa (calculado a partir da idade).
5. Determine se a pessoa é maior de idade e imprima "É maior de Idade?" seguido da resposta.
6. Imprima a altura da pessoa em metros.

Lembre-se de usar as variáveis fornecidas e fornecer a saída de maneira organizada e legível.

```python
# Resultado  
nome = 'Pedro Luiz'  
sobrenome = 'Barros'  
idade = 22  
ano_nascimento = 2023 - idade  
maior_de_idade = idade >= 18  
altura_metros = 1.69  
  
# Exercicio  
print('Nome:', nome)  
print('Sobrenome:', sobrenome)  
print('Idade:', idade)  
print('Ano de Nascimento:', ano_nascimento)  
print('É maior de Idade?', maior_de_idade)  
print('Altura em Metros:', altura_metros)
```