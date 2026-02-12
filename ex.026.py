frase = str(input('Digite uma Frase: ')).strip().lower()
print(f'Existe na frase a letra "a"{frase.count('a')+1} Vezes, ela aparece na primeira vez em {frase.find('a')+1}')
print(f'E a ultima vez em {frase.rfind('a')+1}')