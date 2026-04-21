#lista FOR 2

#1) Peça para o usuário digitar um número inteiro. Mostre todos os números de 1 até esse número (inclusive).
'''
numero = int(input('Digita um Numero: '))

for i in range(1,numero + 1):
    print(i)
'''

#2) Peça para o usuário digitar um número inteiro. Mostre apenas os números pares de 0 até esse número.
'''
num = int(input('Digita ae: '))
for i in range(0, num + 1):
    if i % 2 == 0:
        print(i)
'''

#3) Peça para o usuário digitar 10 números. Ao final, mostre a soma de todos eles.
'''
num = 0

for i in range(10):
    i = int(input('Digite um Numero: '))
    num += i
print(f'A Soma de tudo é {num}')
'''

#4) Peça para o usuário digitar um número inteiro. Mostre a soma de todos os números de 1 até esse número.
'''
num = int(input('Digita um Numero: '))
soma = num
for i in range (1, num):
    soma += i
print(soma)
'''

#5) Peça para o usuário digitar um número inteiro. Mostre o fatorial desse número.
'''
num = int(input('Digita um Numero: '))
mult = 1

for i in range(1, num + 1):
    mult *= i 
    print(i)
print(mult)
'''

#6) Peça para o usuário digitar um número inteiro. Mostre a tabuada desse número de 1 a 10.
'''
num = int(input('Digita um Numero: '))

for i in range(1, 11):
    resultado = num * i
    print(i)
    print(f'{num} X {i} = {resultado}')
'''

#7) Peça para o usuário digitar 5 números. Ao final, informe qual foi o maior número digitado.
'''
num = int(input('Digita ae: '))
maior = num

for i in range (4):
    num = int(input('Digita ae2: '))
    if num > maior:
        maior = num
print(maior)
'''

#8) Peça para o usuário digitar um número inteiro. Mostre todos os divisores desse número.
'''
num = int(input('Digita um Numero: '))

for i in range(1, num+1):
    if num % i == 0:
        print(i)
'''

#9) Peça para o usuário digitar um número inteiro. Verifique e informe se ele é primo.
'''
num = int(input('Digita um Numero: '))
ePrimo = True

for i in range (2, num):
    if num % i == 0:
        ePrimo = False
        break
if ePrimo:
    print('É Primo')
else:
    print('Não é Primo ora bolas em')
'''

#10) Peça para o usuário digitar um número inteiro. Conte quantos números primos existem menores do que esse número.

'''
num = int(input('Digita ae '))
cont = 1

for i in range(2, num):
'''