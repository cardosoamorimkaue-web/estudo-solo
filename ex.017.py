import math
catetoposto = float(input('Qual a medida do op.cateto? '))
adjcateto = float(input('Qual a medida do adj.cateto? '))
hipo = catetoposto ** 2 + adjcateto ** 2 

print(f'A hipotenusa é {math.sqrt(hipo):.2f}')

'''

    correção
import math 
co = float(input('Valor do cateto oposto: '))
ca = float(input('Valor do cateto adj: '))
hipo = math.hypot(co, ca)
print(hipo)

'''