# Hipótesis de Lothar Collatz

c0 = int(input("Ingresa un número: "))
pasos = 0
while True:
    if c0 > 0:
        while c0 != 1:
            pasos += 1
            if c0 % 2 == 0:
                c0 = c0 // 2
                print(c0)
                continue
            else:
                c0 = 3 * c0 + 1
                print(c0)
                continue
        print("Pasos totales: " + str(pasos))
        break
    else:
        c0 = int(input("El número debe ser un entero mayor que cero: "))
        continue
