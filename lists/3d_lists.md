# Listas Tridimensionales

Imagina un hotel. Es un hotel enorme que consta de tres edificios, de 15 pisos cada uno. Hay 20 habitaciones en cada piso. Para esto, necesitas un arreglo que pueda recopilar y procesar información sobre las habitaciones ocupadas/libres.

**Paso uno:** el tipo de elementos del arreglo. En este caso, sería un valor booleano (True/False).

**Paso dos:** análisis de la situación. Resume la información disponible: tres edificios, 15 pisos, 20 habitaciones.

Ahora puedes crear el arreglo:

```py
  habitaciones = [[[False for r in range(20)] for f in range(15)] for t in range(3)]
```

El primer índice (0 a 2) selecciona uno de los edificios; el segundo(0 a 14) selecciona el piso, el tercero (0 a 19) selecciona el número de habitación. Todas las habitaciones están inicialmente desocupadas.

Ahora ya puedes reservar una habitación para dos recién casados: en el segundo edificio, en el décimo piso, habitación 14:

```py
  habitaciones[1][9][13] = True
```

Y desocupa el segundo cuarto en el quinto piso ubicado en el primer edificio:

```py
  habitaciones[0][4][1] = False
```

Verifica si hay disponibilidad en el piso 15 del tercer edificio:

```py
  vacante = 0

  for numeroHabitacion in range(20):
      if not habitaciones[2][14][numeroHabitacion]:
          vacante += 1
```

La variable `vacante` contiene 0 si todas las habitaciones están ocupadas, o en dado caso el número de habitaciones disponibles.
