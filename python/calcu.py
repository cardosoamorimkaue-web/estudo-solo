num1 = int(input('Digite um Numero: '))
sinal = (input('Qual o seu operador? '))
num2 = int(input('Digite o Segundo Numero: '))

if sinal == '+':
        s = num1 + num2
        print(f'A soma é {s}')
elif sinal == '-':
        dmi = num1 - num2
        print(f'a subtração é {dmi}')
elif sinal == '*':
        mult = num1 * num2
        print(f'A multiplicação é {mult}')
else:
        div = num1 / num2
        print(f'A divisão é: {div}')