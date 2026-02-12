numeros = [int(num) for num in input("digite uma lista de numeros separado por espaço").split()]

pares = 0
impares = 0


for num in numeros:
    if num % 2 == 0:
        pares += 1
    else:
        impares+= 1

indice = 0
while indice < len(numeros):
    print(f"numero na posição {indice}: {numeros[indice]}")
    indice += 1

print("quantidade de numeros pares: ", {pares})
print("quantidade de numeros impares: ", {impares})