frase = input('Digite uma frase: ').lower()
vogal = 0
consu = 0
for letra in frase:
    
    if letra in 'aeiou':
      vogal += 1
    else:
      consu += 1


print(f'Essa frase tem {vogal} vogais e {consu} consoantes')
'''frase.count('e') and frase.count('i') and frase.count('o') and frase.count('u'):   '''