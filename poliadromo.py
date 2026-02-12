frase = str(input('Digite  uma palavra: ')).lower()

invert = frase[::-1]

if invert == frase:
    print('elas são iguais')
else:
    print('elas não são iguais')
