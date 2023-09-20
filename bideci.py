binario = input("Coloque el numero binario: ")
binario_rev = binario[::-1]
longitud = len(binario)
decimal = 0
contador = 0
while contador < longitud:
    if binario_rev[contador] == "1":
        decimal += 2**contador
    contador +=1

print(decimal)