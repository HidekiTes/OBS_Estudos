```python
# Conversão de tipos (Coerção)

"""
Conversão de tipos ou Coerção
Type convertion, type casting, coercion é o ato de converter um tipo em outro
Tipos imutáveis e primitivos: str, int, float, bool
"""

#print('1'+1) #Dá erro por ser tipos de dados diferentes
print(int('1'),type(int('1'))) # O type('1') converte a srt para int
print(float('1.2')+1) # o type ('1.2') converte a srt para float
print(bool(' ')) # OBS: Campo com dado lá dentro é considerado como "true"
print(str('11') + 'b')
```