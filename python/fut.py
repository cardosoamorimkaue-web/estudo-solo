vit = int(input('numero de vitorias: '))
derr = int(input('numero de derrotas: '))
emp = int(input('numero de empates: '))
Total = (vit * 3) + emp
print(f"Você teve {vit} Vitorias, {derr} derrotas e {emp} empates, então sua pontuação final é {Total}")