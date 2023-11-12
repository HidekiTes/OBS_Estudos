```python
'''
Modularização - Entendendo os seus próprios módulos Python e
sys.path no Python
  
O primeiro módulo executado chama-se __main__
Você pode importar outro módulo inteiro ou parte do módulo
O python conhece a pasta onde o __main__ está e as pastas
abaixo dele.
Ele não reconhece pastas e módulos acima do __main__ por
padrão
O python conhece todos os módulos e pacotes presentes
nos caminhos de sys.path
'''
import aula_39_m
  
print('Este módulo se chama', __name__)
```

Arquivo - aula_39_m.py (dentro da mesma pasta)
```python
print('Este módulo se chama', __name__)
```