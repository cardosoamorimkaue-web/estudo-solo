nome =str(input('Digite seu nome Completo: ')).strip() #eliminar os espaços inulteis

M = nome.upper()
n = nome.lower()
T = len(nome) - nome.count(" ") #conta e remove o espaço entre o nome
pn = nome.find(" ")

print(f'''Seu nome em maiusculas é {M}, em Minusculas é {n}, 
ao todo tem {T}letras e seu Primeiro nome tem {pn}letras.''')

##faltou raciocinio nessa ultima parte
