# miLista = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9, 4, 5, 6, 7, 8, 12, 45, 23]
miLista = []
listaNueva = []
ide = 0
cantidad = int(
    input("Ingresa la cantidad de valores que deseas agregar a tu lista: "))
for valores in range(cantidad):
    num = int(input("Ingresa un número: "))
    miLista.append(num)
miLista.sort()
for i in miLista:
    if i == miLista[ide+1]:
        ide += 1
        continue
    else:
        ide += 1
        listaNueva.append(i)
        if ide == len(miLista)-1:
            listaNueva.append(miLista[-1])
            break
print("La lista solo con elementos únicos: ")
print(listaNueva)
