```python
'''
Exemplo do uso de sets
'''
letras = set()
  
while True:
letra = input('Digite: ')
letras.add(letra)
  
if 'l' in letras:
print('Parabens')
break
  
print(letras)
```