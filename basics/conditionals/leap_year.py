print("\n\t¿Quieres saber si algún año es común o bisiesto?")
print("\n¡Muy fácil! Solo ingresa el año deseado y nosotros haremos el resto...")

year = int(input("\nAño: "))

if year < 1582:
    print(year, "no está dentro de la era Gregoriana.")
elif year % 4 != 0:
    print(year, "es un año común.")
elif year % 100 != 0:
    print(year, "es un año bisiesto.")
elif year % 400 != 0:
    print(year, "es un año común.")
else:
    print(year, "es un año bisiesto.")
