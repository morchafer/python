def isSudoku():

    # Manejo de errores e ingreso de filas:

    r1 = input("Ingresa la fila 1: ")
    if len(r1) != 9 or not r1.isdigit() or "0" in r1:
        print("Error: unicamente puedes ingresar nueve dígitos del 1 al 9.")
        return
    r2 = input("Ingresa la fila 2: ")
    if len(r2) != 9 or not r2.isdigit() or "0" in r2:
        print("Error: unicamente puedes ingresar nueve dígitos del 1 al 9.")
        return
    r3 = input("Ingresa la fila 3: ")
    if len(r3) != 9 or not r3.isdigit() or "0" in r3:
        print("Error: unicamente puedes ingresar nueve dígitos del 1 al 9.")
        return
    r4 = input("Ingresa la fila 4: ")
    if len(r4) != 9 or not r4.isdigit() or "0" in r4:
        print("Error: unicamente puedes ingresar nueve dígitos del 1 al 9.")
        return
    r5 = input("Ingresa la fila 5: ")
    if len(r5) != 9 or not r5.isdigit() or "0" in r5:
        print("Error: unicamente puedes ingresar nueve dígitos del 1 al 9.")
        return
    r6 = input("Ingresa la fila 6: ")
    if len(r6) != 9 or not r6.isdigit() or "0" in r6:
        print("Error: unicamente puedes ingresar nueve dígitos del 1 al 9.")
        return
    r7 = input("Ingresa la fila 7: ")
    if len(r7) != 9 or not r7.isdigit() or "0" in r7:
        print("Error: unicamente puedes ingresar nueve dígitos del 1 al 9.")
        return
    r8 = input("Ingresa la fila 8: ")
    if len(r8) != 9 or not r8.isdigit() or "0" in r8:
        print("Error: unicamente puedes ingresar nueve dígitos del 1 al 9.")
        return
    r9 = input("Ingresa la fila 9: ")
    if len(r9) != 9 or not r9.isdigit() or "0" in r9:
        print("Error: unicamente puedes ingresar nueve dígitos del 1 al 9.")
        return

    # Verificando los datos de las filas:

    rows = (r1, r2, r3, r4, r5, r6, r7, r8, r9)
    count = 0
    for r in rows:
        for i in r:
            for j in r:
                if i == j:
                    count += 1
            if count > 1:
                print("No es un Sudoku.")
                return False
            else:
                count = 0

    # Verificando los datos de las columnas:

    x = 0
    c1, c2, c3, c4, c5, c6, c7, c8, c9 = '', '', '', '', '', '', '', '', ''
    columns = (c1, c2, c3, c4, c5, c6, c7, c8, c9)
    for col in columns:
        col = r1[x] + r2[x] + r3[x] + r4[x] + \
            r5[x] + r6[x] + r7[x] + r8[x] + r9[x]
        x += 1
    count_2 = 0
    for c in columns:
        for i in c:
            for j in c:
                if i == j:
                    count_2 += 1
            if count_2 > 1:
                print("No es un Sudoku.")
                return False
            else:
                count_2 = 0

    # Verificando los datos de los campos 3x3s:

    f1 = r1[0:3] + r2[0:3] + r3[0:3]
    f2 = r1[3:6] + r2[3:6] + r3[3:6]
    f3 = r1[6:] + r2[6:] + r3[6:]
    f4 = r4[0:3] + r5[0:3] + r6[0:3]
    f5 = r4[3:6] + r5[3:6] + r6[3:6]
    f6 = r4[6:] + r5[6:] + r6[6:]
    f7 = r7[0:3] + r8[0:3] + r9[0:3]
    f8 = r7[3:6] + r8[3:6] + r9[3:6]
    f9 = r7[6:] + r8[6:] + r9[6:]

    fields = (f1, f2, f3, f4, f5, f6, f7, f8, f9)
    count_3 = 0
    for f in fields:
        for i in f:
            for j in f:
                if i == j:
                    count_3 += 1
            if count_3 > 1:
                print("No es un Sudoku.")
                return False
            else:
                count_3 = 0

    print("Sí es un Sudoku.")
    return True
