def isLeapYear(yr):
    if yr % 4 != 0:
        return False
    elif yr % 100 != 0:
        return True
    elif yr % 400 != 0:
        return False
    else:
        return True


def lifeNum(day, month, year):
    example = 0
    months_30 = [4, 6, 9, 11]
    months_31 = [1, 3, 5, 7, 8, 10, 12]

    # Manejo de errores:

    if type(example) != type(day) or type(example) != type(month) or type(example) != type(year):
        print("Error: lifeNum() requiere números enteros para sus tres argumentos (day, month, year).")
        return
    elif year < 1910 or year > 2020:
        print("Error: el argumento 'year' requiere un valor entero en el rango de 1910 a 2020.")
        return
    elif month < 1 or month > 12:
        print("Error: el argumento 'month' requiere un valor entero en el rango de 1 a 12.")
        return
    elif not isLeapYear(year):
        if month == 2:
            if day < 1:
                print(
                    "Error: el argumento 'day' requiere un valor entero en el rango de 1 a 28.")
                return
            elif day >= 29:
                print("Error:", year, "no es bisiesto.",
                      "Para el mes", month, "se requiere un valor")
                print("entero del argumento 'day', comprendido en el rango de 1 al 28.")
                return
    elif month == 2:
        if day < 1 or day > 29:
            print(
                "Error: el argumento 'day' requiere un valor entero en el rango de 1 a 29.")
            return
    for i in months_30:
        if month == i:
            if day < 1 or day > 30:
                print(
                    "Error: el argumento 'day' requiere un valor entero en el rango de 1 a 30.")
                return
            else:
                break
    for j in months_31:
        if month == j:
            if day < 1 or day > 31:
                print(
                    "Error: el argumento 'day' requiere un valor entero en el rango de 1 a 31.")
                return
            else:
                break

    # Si no hay ninguna excepción en el ingreso de los argumentos, inicia el proceso de la función:

    total = 0
    for d in str(day):
        total += int(d)
    for m in str(month):
        total += int(m)
    for y in str(year):
        total += int(y)
    totalList = list(str(total))
    while True:
        if len(totalList) > 1:
            total = 0
            for t in totalList:
                total += int(t)
            del totalList[:]
            for tt in str(total):
                totalList.append(tt)
        else:
            break
    return total
