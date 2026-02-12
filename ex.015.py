dias = int(input('Quantos Dias ele foi alugado? '))
km = float(input('Quantos Km foi percorrido? '))
print(f"Ele percorreu {km}km por {dias} dias então o valor a ser pago será R${(dias*60)+(km*0.15):.2f}")