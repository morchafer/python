grupo = {}

while True:
    nombre = input(
        "Ingresa el nombre del estudiante (o exit para detenerse): ")
    if nombre == 'exit':
        break
    calif = int(input("Ingresa la calificación del alumno (0-10): "))
    if nombre in grupo:
        grupo[nombre] += (calif,)
        """ Nota: no se actualiza la tupla existente (por inmutabilidad). Se está concatenando una tupla con otra, esto las une en una sola tupla."""
    else:
        grupo[nombre] = (calif,)

for nombre in sorted(grupo.keys()):
    sum = 0
    contador = 0
    for calif in grupo[nombre]:
        sum += calif
        contador += 1
    print(nombre, ":", sum / contador)
