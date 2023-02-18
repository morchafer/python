vocales = 'AEIOU'
palabra = input("Ingresa una palabra: ")
palabra = palabra.upper()

for letra in palabra:
    if letra in vocales:
        continue
    else:
        print(letra)
