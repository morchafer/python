hora = int(input("Hora de inicio (formato 24 hrs): "))
minu = int(input("Minuto de inicio (minutos): "))
dura = int(input("Duración del evento (en minutos): "))

# Si el usuario ingresa +24 hrs, este proceso lo convierte a formato 24:
horaFormato24 = hora % 24

# Se suman los minutos ingresados y los minutos de duracion:
minu2 = minu + dura

# El cociente de la siguiente división es/son la/s hora/s resultante/s que podrían salir de la suma de los minutos anteriores:
hora2 = minu2 // 60

# Se suma la hora ingresada al inicio y la hora resultante:
totalHoras = hora2 + horaFormato24

# Si totalHoras se excede de 24, para que la consola no imprima "25, 26, 27, etc.." se calcula el residuo entre 24:
totalHoras2 = totalHoras % 24

# Se calcula el residuo entre 60 (minutos) de la división de la suma de los minutos para "separar" los minutos excedidos:
totalMinutos = minu2 % 60

print("El evento comienza a las " +
      repr(horaFormato24) + ":" + repr(minu), end=" ")
print("y finaliza a las " + repr(totalHoras2) + ":" + repr(totalMinutos))
