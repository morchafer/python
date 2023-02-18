bloques = int(input("Ingrese el número de bloques: "))
conteoDeBloques = 0  # Inicializa la variable en cero

# Declaramos la variable de control con un recorrido en el rango del 1 al numero de bloques + 1 para que la función range() tome el valor real de la variable bloques y no uno menos.
for i in range(1, bloques+1):
    # Actualizamos conteoDeBloques sumandole el valor de i del turno actual del ciclo
    conteoDeBloques = conteoDeBloques + i
    if conteoDeBloques + i >= bloques:  # Condicionamos la variable conteoDeBloques; si la suma de conteoDeBloques más el valor actual de i es mayor o igual al número de bloques, entonces sale del bucle e imprime
        break
    else:  # De lo contrario...
        continue  # ...continúa con el ciclo for en el siguiente turno de i
print("Con", bloques, "bloques puedes construir", i, "capas.")
