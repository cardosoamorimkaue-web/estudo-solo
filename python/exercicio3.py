numeros = []
for i in range (6):
    num = int(input("digite um numero: "))
    numeros.append(num)

pares = []
impares = []

for n in numeros:
    if n % 2 == 0:
     pares.append(n)
    else:
     impares.append(n)
    

somap = sum(pares)
somai = sum(impares)

print()
print("os numeros foram: ", numeros)
print("Seus pares: ", pares)
print("O total dos Pares é: ", somap)
print("Seus numeros impares são: ",impares)
print("A soma dos ímpares é: ", somai)
