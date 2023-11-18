```python
'''
Salvando dados Python em JSON com módulo json
'''
  
import json
  
pessoa = {
'nome': 'Luiz Otávio 2',
'sobrenome': 'Miranda',
'enderecos': [
{'rua': 'R1', 'numero': 32},
{'rua': 'R2', 'numero': 55},
],
'altura': 1.8,
'numeros_preferidos': (2, 4, 6, 8, 10),
'dev': True,
'nada': None,
}
  
with open('aula_67.json', 'w', encoding='utf8') as arquivo:
json.dump(
pessoa,
arquivo,
ensure_ascii=False,
indent=2,
)
  
with open('aula_67.json', 'r', encoding='utf8') as arquivo:
pessoa = json.load(arquivo)
# print(pessoa)
# print(type(pessoa))
print(pessoa['nome'])
```

Arquivo gerado - aula_67.json
```json
{
"nome": "Luiz Otávio 2",
"sobrenome": "Miranda",
"enderecos": [
{
"rua": "R1",
"numero": 32
},
{
"rua": "R2",
"numero": 55
}
],
"altura": 1.8,
"numeros_preferidos": [
2,
4,
6,
8,
10
],
"dev": true,
"nada": null
}
```