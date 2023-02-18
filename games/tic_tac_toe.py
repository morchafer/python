from random import randrange
from os import system


def tableroActual(tablero):
    # la función acepta un parámetro que contiene el estado actual del tablero y lo muestra en consola
    # tablero = [[1, 2, 3], [4, "X", 6], [7, 8, 9]]

    for columna0, columna1, columna2 in tablero[0], tablero[1], tablero[2]:
        print("+-------+-------+-------+")
        print("|       |       |       |")
        print("|  ", columna0, "  ", end="")
        print("|  ", columna1, "  ", end="")
        print("|  ", columna2, "  |")
        print("|       |       |       |")
    print("+-------+-------+-------+")

    movimientoUsuario(tablero)


def movimientoUsuario(tablero):
    # la función acepta el estado actual del tablero y pregunta al usuario acerca de su movimiento,
    # verifica la entrada y actualiza el tablero acorde a la decisión del usuario
    # tablero = [[1, 2, 3], [4, "X", 6], [7, 8, 9]]

    # {1:(0, 0), 2:(0, 1), 3:(0, 2), 4:(1, 0), 6:(1, 2), 7:(2, 0), 8:(2, 1), 9:(2, 2)}
    cuadrosDisponibles = cuadrosVacios(tablero)
    movUsuario = int(input("Ingresa tu movimiento: "))
    while movUsuario < 1 or movUsuario > 9 or movUsuario == 5 or movUsuario not in cuadrosDisponibles:
        movUsuario = int(input("Error, ingresa un número válido: "))
    for i in cuadrosDisponibles:
        if i == movUsuario:
            fila, columna = cuadrosDisponibles.get(i)
            tablero[fila][columna] = "O"
            break

    movimientoMaquina(tablero)


def cuadrosVacios(tablero):
    # la función examina el tablero y construye una lista de todos los cuadros vacíos
    # la lista está compuesta por tuplas, cada tupla es un par de números que indican la fila y columna
    # tablero = [[1, 2, 3], [4, "X", 6], [7, 8, 9]]

    diccCuadrosVacios = {}
    for vacio1, vacio2, vacio3 in tablero:
        if vacio1 in range(1, 4):
            diccCuadrosVacios.update({1: (0, 0)})
        if vacio2 in range(1, 4):
            diccCuadrosVacios.update({2: (0, 1)})
        if vacio3 in range(1, 4):
            diccCuadrosVacios.update({3: (0, 2)})

        if vacio1 in range(4, 7):
            diccCuadrosVacios.update({4: (1, 0)})
        if vacio3 in range(4, 7):
            diccCuadrosVacios.update({6: (1, 2)})

        if vacio1 in range(7, 10):
            diccCuadrosVacios.update({7: (2, 0)})
        if vacio2 in range(7, 10):
            diccCuadrosVacios.update({8: (2, 1)})
        if vacio3 in range(7, 10):
            diccCuadrosVacios.update({9: (2, 2)})

    # {1:(0, 0), 2:(0, 1), 3:(0, 2), 4:(1, 0), 6:(1, 2), 7:(2, 0), 8:(2, 1), 9:(2, 2)}
    return diccCuadrosVacios


def victoria(tablero):
    # la función analiza el estado del tablero para verificar si
    # el jugador que utiliza las 'O's o las 'X's ha ganado el juego
    # tablero = [[1, 2, 3], [4, "X", 6], [7, 8, 9]]

    fila0, fila1, fila2 = tablero
    uno, dos, tres = fila0
    cuatro, cinco, seis = fila1
    siete, ocho, nueve = fila2

    if uno == dos == tres:
        print("El ganador es: ", uno)
        input("Presiona ENTER para salir...")
    elif cuatro == cinco == seis:
        print("El ganador es: ", cuatro)
        input("Presiona ENTER para salir...")
    elif siete == ocho == nueve:
        print("El ganador es: ", siete)
        input("Presiona ENTER para salir...")
    elif uno == cuatro == siete:
        print("El ganador es: ", uno)
        input("Presiona ENTER para salir...")
    elif dos == cinco == ocho:
        print("El ganador es: ", dos)
        input("Presiona ENTER para salir...")
    elif tres == seis == nueve:
        print("El ganador es: ", tres)
        input("Presiona ENTER para salir...")
    elif uno == cinco == nueve:
        print("El ganador es: ", uno)
        input("Presiona ENTER para salir...")
    elif tres == cinco == siete:
        print("El ganador es: ", tres)
        input("Presiona ENTER para salir...")
    else:
        system("cls")
        tableroActual(tablero)


def movimientoMaquina(tablero):
    # la función dibuja el movimiento de la maquina y actualiza el tablero

    cuadrosDisponibles2 = cuadrosVacios(tablero)
    control = True
    while control:
        for i in cuadrosDisponibles2:
            aleatorio = randrange(1, 10)
            if i == aleatorio:
                control = False
                fila, columna = cuadrosDisponibles2.get(i)
                tablero[fila][columna] = "X"
                break

    victoria(tablero)

    # {1:(0, 0), 2:(0, 1), 3:(0, 2), 4:(1, 0), 6:(1, 2), 7:(2, 0), 8:(2, 1), 9:(2, 2)}
    # tablero = [[1, 2, 3], [4, "X", 6], [7, 8, 9]]


print("\n\t--- Tic Tac Toe ---")
print("\nReglas a considerar: \n")
print("1. La computadora utiliza la letra 'X' para representar sus movimientos.")
print("2. El usuario utiliza la letra 'O' para representar sus movimientos.")
print("3. La computadora inicia siempre el juego con un movimiento en el centro del tablero.")
print("4. Para ingresar un movimiento simplemente escribe el número del cuadro que quieres cubrir.")
print("5. Gana el primero que logre unir tres de sus letras en vertical, horizontal o diagonal.")
print("\nSuerte, y que gane el mejor ;)\n")

tablero = [[1, 2, 3], [4, "X", 6], [7, 8, 9]]
tableroActual(tablero)
