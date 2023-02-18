numerosImpares = 0
numerosPares = 0

# Lee el primer número
numero = int(input("Introduce un número o escriba 0 para detener: "))

# 0 termina la ejecución
while numero != 0:
    # Verificar si el número es impar
    if numero % 2 == 1:
        # Aumentar el contador de números impares
        numerosImpares += 1
    else:
        # Aumentar el contador de números pares
        numerosPares += 1
    # Lee el siguiente número
    numero = int(input("Introduce un número o escriba 0 para detener:"))

# Imprimir resultados
print("Números impares: ", numerosImpares)
print("Números pares: ", numerosPares)
