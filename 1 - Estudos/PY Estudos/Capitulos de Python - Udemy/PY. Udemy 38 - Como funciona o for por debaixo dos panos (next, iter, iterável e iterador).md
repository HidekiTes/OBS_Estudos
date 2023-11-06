```python
'''
Como funciona o for por debaixo dos panos (next, iter, iterável e iterador)

Iterável -> str, range, etc (__iter__)
Iterador -> Quem sabe entregar um valor por vez
Next -> Me entregue o próximo valor
Iter -> Me entregue seu iterador
'''
# for letra in Texto
texto = "Luiz" # iteravel
# iterator = iter(texto) # iterator

# while True:
# try:
# letra = next(iterator)
# print(letra)
# except StopIteration:
# break

for letra in texto:
print(letra)
```