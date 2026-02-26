funcionario= []

for i in range(1):
    nome = input("Digite o nome do funcionario: ")
    funcao = input("Digite a Função: ")
    salario = float(input("Digite o Salario: "))

funcionario.append({'nome': nome,'funcao': funcao, 'salario': salario})

aumento = salario + ( salario * 15 / 100 )

print(f"O funcionario {nome}, teve seu salario aumentado em 15%, resultando no Valor de {aumento:.2F}")