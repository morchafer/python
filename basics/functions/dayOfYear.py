def isLeapYear(year):
    if year < 1582:
        print(year, "no está dentro de la era Gregoriana.")
    elif year % 4 != 0:
        return False
    elif year % 100 != 0:
        return True
    elif year % 400 != 0:
        return False
    else:
        return True


def daysInMonth(year, month):
    bisiesto = True
    meses30 = [4, 6, 9, 11]
    meses31 = [1, 3, 5, 7, 8, 10, 12]
    if bisiesto == isLeapYear(year):
        if month in meses30:
            return 30
        elif month in meses31:
            return 31
        elif month == 2:
            return 29
        else:
            return None
    else:
        if month in meses30:
            return 30
        elif month in meses31:
            return 31
        elif month == 2:
            return 28
        else:
            return None


def dayOfYear(year2, month2, day):
    meses = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    sumaDias = 0
    for i in range(len(meses)):
        if month2 <= 12 and day <= 366:
            if month2 == meses[i]:
                controlDias = 0
                controlDias += daysInMonth(year2, meses[i])
                diferenciaDias = controlDias
                diferenciaDias -= day
                numDias = controlDias - diferenciaDias
                sumaDias += numDias
            elif month2 > meses[i]:
                sumaDias += daysInMonth(year2, meses[i])
            else:
                break
        else:
            print("Error, ingresa un mes y día válido")
            break
    return sumaDias


print(dayOfYear(2000, 12, 31))
