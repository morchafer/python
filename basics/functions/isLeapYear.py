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


testData = [1900, 2000, 2016, 1987]
testResults = [False, True, True, False]
for i in range(len(testData)):
    yr = testData[i]
    print(yr, "->", end="")
    result = isLeapYear(yr)
    if result == testResults[i]:
        print("OK")
    else:
        print("Error")
