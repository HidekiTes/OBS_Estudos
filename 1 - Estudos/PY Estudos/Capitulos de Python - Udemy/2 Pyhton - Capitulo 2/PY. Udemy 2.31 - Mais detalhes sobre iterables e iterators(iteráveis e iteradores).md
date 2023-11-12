```python
'''
Mais detalhes sobre iterables e iterators(iteráveis
e iteradores)
'''
iterable = ['Eu', 'Tenho','__iter__']
iterator = iter(iterable)
print(next(iterator))
print(next(iterator))
print(next(iterator))
# print(next(iterator))
```