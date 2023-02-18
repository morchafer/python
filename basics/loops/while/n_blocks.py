bloques = int(input("Ingrese el número de bloques: "))
conteoDeBloques = 0
i = 0
while i <= bloques:
    i += 1
    conteoDeBloques = conteoDeBloques + i
    if conteoDeBloques + i >= bloques:
        break
    else:
        continue
print("Con", bloques, "bloques puedes construir", i, "capas.")
