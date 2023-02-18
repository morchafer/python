print("\n\t\t---Calculadora de Impuesto Personal de Ingresos (IPI)---")
print()
print("Bienvenid@, para continuar por favor digita tu ingreso anual...")
print("Nota: toma en cuenta los valores decimales (máximo 2) si es necesario.")
ingresoAnual = float(input("Ingreso anual: "))
if ingresoAnual <= 85_528:
    ipi = ((ingresoAnual/100)*18) - 556.2
    if ipi <= 0:
        print("\n\t¡No tienes impuestos pendientes!")
    if ipi > 0:
        print("\n\tTu IPI es de " + str(round(ipi, 2)) + " pesos.")
elif ingresoAnual > 85_528:
    ipi = 14_839.2 + (((ingresoAnual - 85_528)/100)*32)
    if ipi <= 0:
        print("\n\t¡No tienes impuestos pendientes!")
    if ipi > 0:
        print("\n\tTu IPI es de " + str(round(ipi, 2)) + " pesos.")
