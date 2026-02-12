frase = "Curso em Video python"
'''
frase[9]
#SERA DO 0(C) ate 0 9(V)
frase[9:13]
#sera do V(9) ate o e(12) pq o indice final ser ignorado (nesse caso (o)13 )
frase[9:21:2]
#sera do 9(V) ate so 21(q n tem) pulando de dois em dois
frase[:5]
#sera do começo ate o 5(o espaco)parando no 4(o)
frase[15:]
#sera do 15(P) ate o final
frase[9::3]
#começara do 9(V) ate o final pulando de 3 em 3

'''

'''em resumo {1}:{2}:{3} o 1 define o começo
    o 2 o final do fatiamento
    o 3 quantas casas vai pular a frase/string
'''

'''ANALISE
len() vai retornar o valor de caracteres
cont() vai contar (ta no nome burro) os caracteres que vc quiser, podendo usar o fatiamento nele
find() vai encontrar (que coisa n?) uma frase ou letras expecificas e retornar o indice que começa ('deo') vai retornar 11
fazendo 'curso' IN frase vai retornar se existe nessa variavel nesse caso true
'''

'''TRANSFORMAÇÃO
replace() [trocar] vai pegar uma frase ou letra e vai troca-la por outra de usa escolha
    ex: frase.replace('python','android')
upper() vai por em maiusculo
lower() vai por em minusculo
capitalize() vai organizar a frase entre M e N no caso a primeira letra em Maiusculo e o restante em minusculo
title() vai por em maiusculo tudo que tiver depois do espaco C E V P
strip() vai remover os espaços inuteis
    ex: "   aprendo python   " vai ser "aprendo python"
 rstrip vai remover os espaços da direita
 istrip vai remover os da esquerda
 split() vai separar uma string pelo espaco e colocar em uma lista
join vai juntar as strings
    ex: '-'.join(frase) vai retornar a frase colocando - no lugar dos espaços
'''
print(frase.lower().find('video'))
