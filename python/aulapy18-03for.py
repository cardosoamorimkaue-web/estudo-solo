#LISTA 6 for
'''
for i in range(1,7):
    print(i)
'''
'''
for i in range(1,7,2):
    print(i)
'''

'''
inicio = 1
fim = 10
passo = 1
#(onde começa,onde Termina, de quanto vai pular)
for i in range (inicio + 5, fim + 1, passo):
    print(f'Valor de i: {i}')
'''
'''
palavra = input('Digita ae ')
tamanho = len(palavra)
for p in range(0, tamanho):
    print(f'A letra {palavra[i]} está na posição {i})
'''
'''
numero = int(input('numero: '))

for i in range(1, 11):
    resultado = numero * i
    print(f'{numero} x {i} = {resultado}')
'''
'''
n = int(input('numero: '))
soma = 0 
for i in range (1, n + 1):
    soma+= i
print(f'Soma Final: {soma}')
'''
'''
n = int(input('numero: '))
soma = 0
for i in range(0, n + 1):
    if i // 2 == 1:
        soma+= i
        print(f'i = {i} | soma = {soma}')
print(f'Soma dos Impares: {soma}')

n = int(input('numero: '))
soma = 0
for i in range(0, n + 1):
    if i % 2 == 0:
        soma+= i
        print(f'i = {i} | soma = {soma}')
print(f'Soma dos Pares: {soma}')
'''