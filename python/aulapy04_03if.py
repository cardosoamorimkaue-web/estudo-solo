#5
'''                                                            #dia 04/03 de lógica 
a = int(input("Digite o 1° Valor: "))
b = int(input("Digite o 2° Valor: "))
c = int(input("Digite o 3° Valor: "))
if a + b > c and a + c > b and b + c > a:
    if a == b == c:
        print("equilatero")
    #elif a == b or a == c or b == c:
    elif a == b != c or a == c != b or b == c != a:
        print("Isoseles")
    elif a != b != c:
        print("escaleno")
else:
    print('Não é triangulo, burro')

#8
idade = int(input('idade: '))
cnh = input('Sim ou Não')

if idade >= 18 and cnh == 'Sim':
    print('pode DIRIGIR')
else:
    print("Não pode")
## TRATAMENTO DE ERRO
idade = int(input('idade: '))
cnh = input('s ou n')
if idade >= 18:
    if cnh == "s":
        print('pode dirigir')
    else:
        print('falta cnh')
else:
    print('Não pode')
'''
#9
n1 = int(input("numero 1: "))
n2 = int(input("numero 2: "))
n3 = int(input("numero 3: "))

m = n1


print(m)

