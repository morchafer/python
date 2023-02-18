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


testYears = [1900, 2000, 2016, 1987, 2020]
testMonths = [2, 2, 1, 11, 16]
testResults = [28, 29, 31, 30, None]
for i in range(len(testYears)):
    yr = testYears[i]
    mo = testMonths[i]
    print(yr, mo, "->", end="")
    result = daysInMonth(yr, mo)
    if result == testResults[i]:
        print("OK")
    else:
        print("Error")
