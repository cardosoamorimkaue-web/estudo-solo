import random

alunos = ['kakau','lulu','lolo','jaja']
random.shuffle(alunos)
print(alunos)

alunosT = input('LISTA DE ALUNOS: ').split()
print(F"{random.sample(alunosT,4)}")