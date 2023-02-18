# isPal()

> isPal() recibe como argumento una cadena y retorna un booleano dependiendo si la cadena es un palíndromo o no.

- Se inician las variables necesarias:

  ```py
    # contador para los índices negativos
    count = -1

    # aquí se guardarán las letras del argumento 'text' en el orden en que se encuentren (sin espacios)
    textFront = ''

    # y aquí las letras (sin espacios) pero comenzando por la derecha del argumento 'text'
    textBack = ''
  ```

- Se itera `c` en `text` para ignorar los espacios detectados, o en su defecto, almacenar cada letra de cada iteración:

  ```py
    for c in text:
        if c.isspace():
            continue
        else:
            textFront += c
  ```

- Después, comienza otro bucle for, esta vez para iterar tantas veces sean necesarias en `text` con el fin de actualizar el contador de índices negativos `count` e ir almacenando la letra de la iteración actual en `textBack` si es necesario.

  ```py
    for i in range(len(text)):
        if text[count].isspace():
            count -= 1
            continue
        else:
            textBack += text[count]
            count -= 1
  ```

- Una vez que se tienen las letras de izquierda a derecha y viceversa, se hace la conversión de ambas cadenas a todas las letras en minúsculas (para poder compararlas sin problemas), y se inicia un nuevo contador para ayudar a comparar ambas cadenas.

  ```py
    textFront_ = textFront.lower()
    textBack_ = textBack.lower()
    count_ = 0
  ```

- Para ello, se toma `textFront` como base para iterar y comparar la variable de control con cada caracter de `textBack`; realizando la comparación de caracteres se actualiza el contador de índices en +1, o por el contrario, al primer par de caracteres que se detecten diferentes, ya no cumple la característica de palíndromo, por lo tanto la función retorna `False`.

  ```py
    for j in textFront_:
        if j == textBack_[count_]:
            count_ += 1
            continue
        else:
            return False
  ```

Si el bucle for termina con éxito todas sus iteraciones, significa que todos los pares de caracteres comparados de `textFront` y `textBack` son iguales, lo que significa que `text` sí es palíndromo, por lo tanto retorna `True`.
