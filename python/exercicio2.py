
ano_nascimento = (int(input("Digite o ano que vc nasceu: ")))
ano_atual = (int(input("Digite o ano Atual: ")))

idade = ano_atual - ano_nascimento 

print("Voce tem", idade, "anos ")

if idade >= 18:
    print("voce é adulto")
else:
    print("voce é de menor")