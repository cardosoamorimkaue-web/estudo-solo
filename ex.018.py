import math 
angulo = int(input('Qual o angulo? '))

print(f"O cosseno é {math.cos(math.radians(angulo)):.2f} O seno de {math.sin(math.radians(angulo)):.2f} E a tangente é {math.tan(math.radians(angulo)):.2f}")

'''
    correção
from math import radians, cos, sin, tan 
angulo = int(input('digite o angulo '))
  nesse caso o valor a ser feito é em radianos 
seno = sin(radians(angulo)) vai calcular em radiando e depois achar o valor
cosseno = math.cos(radians(angulo))3
tangente = math.tan(radians(angulo))



'''