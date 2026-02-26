frase = input('Digite uma frase: ')
for f in frase:
    to = len(frase)
    a = frase.count('a')
    e = frase.count('e')
    i = frase.count('i')
    o = frase.count('o')
    u = frase.count('u')
print(f"A sua frase tem {to} letras e {a} são a's {e} e's, {i} i's, {o} o's e {u} u's")