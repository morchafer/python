def arraysEval(cantidad_elementos):
    if type(cantidad_elementos) != type(0):
        print('Error: debes ingresar un entero como argumento.')
        quit()
    elif cantidad_elementos == 0:
        print('Error: debes ingresar un entero mayor a cero para la cantidad de elementos.')
        quit()
    primer_arreglo = []
    segundo_arreglo = []
    while len(primer_arreglo) != cantidad_elementos:
        primer_arreglo.append(
            input(f'Ingresa el elemento #{len(primer_arreglo)+1} del primer arreglo: '))
        segundo_arreglo.append(
            input(f'Ingresa el elemento #{len(segundo_arreglo)+1} del segundo arreglo: '))
    print('Elementos del primer arreglo antes de la evaluación: ', primer_arreglo)
    index = 0
    while True:
        if primer_arreglo[index] in segundo_arreglo:
            if index == len(primer_arreglo)-1:
                primer_arreglo.pop(index)
                break
            primer_arreglo.pop(index)
            continue
        elif index == len(primer_arreglo)-1:
            break
        index += 1
    print('Elementos del segundo arreglo: ', segundo_arreglo)
    print('Elementos del primer arreglo después de la evaluación: ', primer_arreglo)
