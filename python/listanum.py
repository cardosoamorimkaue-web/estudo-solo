numeros = []
for l in range(5):
    l = int(input('digite um numero:'))
    numeros.append(l)
Total = sum(numeros)
print(f'seus numeros foram {numeros} e o total deles é {Total}')