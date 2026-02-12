pessoas = {"kakau", "kakaua", "joninhas"}
numeros_primeiro = {1 , 2, 3, 4}
numeros_segundo = {4, 6, 7, 8}

uniao = numeros_primeiro | numeros_segundo
print(uniao) #unir os conjuntos

diferenca = numeros_primeiro - numeros_segundo
print(diferenca) #vai fazer a sua diferenca

intersecao = numeros_primeiro & numeros_segundo
print(intersecao) #ira mostrar o mesmo dado que tem em ambos

diferenca_simetrica = numeros_primeiro ^ numeros_segundo
print(diferenca_simetrica) #temo que ver isso ae

pessoas.add("lulu viado")
print(pessoas) #explicativo

pessoas.remove("kakau")
print(pessoas) #explicativo denovo

pessoas.discard("kakaua")
print(pessoas) #descarta da lista sem remover

#pessoas.clear() que limpa tudo
