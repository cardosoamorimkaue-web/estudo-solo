positivo = []
negativo = []

while True:
    num = int(input('Digite uma sequencia de numeros: '))
    if num == 0:
        break


    if num > 0:
        positivo.append(num)
    elif num < 0:
        negativo.append(num)
print(negativo, positivo)