# displayLED()

> displayLED() recibe como argumento un valor entero positivo y dibuja en consola ese valor mediante símbolos #.

- Se hace la conversión de `n` a una cadena y se concatena un espacio al final como herramienta para controlar los prints posteriormente.

  ```py
    arg = str(n) + " "
  ```

- Cuando la variable `count` es igual a `6`, `displayLED()` termina su ejecución. Si esto no se cumple, se verifica si el valor actual de `i` es diferente de `" "` (un espacio), de ser así, se concatena `i` con el valor actual de `count` y se guarda en `key` para utilizarla como indice (clave) en el diccionario `nums`:

  ```py
    while True:
        for i in arg:
            if count == "6":
                return
            else:
                if i != " ":
                    key = i + count
                    print(nums[key], end="")
  ```

- Si `i != " "` no se cumple significa que el for llegó al caracter final (el espacio agregado anteriormente) por lo tanto imprime un salto de linea para seguir formando los números en la siguiente línea. Después se actualiza la variable `count`, y se rompe el for, por lo tanto, vuelve a comenzar porque está en un bucle While hasta que `count` sea igual a `6`. El código quedaría de esta forma:

  ```py
    while True:
        for i in arg:
            if count == "6":
                return
            else:
                if i != " ":
                    key = i + count
                    print(nums[key], end="")
                else:
                    print()
                    count = int(count) + 1
                    count = str(count)
                    break
  ```
