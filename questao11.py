#variaveis

valorcarro:float
precoAvista:float
taxaJuros:float

valorcarro = 0 
precoAvista = 0
taxaJuros = 0.03

valorcarro = float(input("  informe o valor do carro:  "))
precoAvista = valorcarro - (valorcarro * 0.20)

for n in range(6, 66, 6):
    print(f"{n} -  {valorcarro + valorcarro * taxaJuros} ")
    taxaJuros = taxaJuros + 0.03 

