# cipherC()

> cipherC() recibe dos argumentos; message como una cadena, y steps como un entero. Retorna una cadena con el mensaje inicial cifrado utilizando el desplazamiento de César.

- Se crea la variable `cipher` donde se almacenará el mensaje cifrado: `cipher = ''`

- Itera en cada caracter de `message` con la variable de control `c`; si `c` no es letra (`False`) se niega (not False = True) y entra al bloque if, en donde se guarda el caracter actual de `c` tal como está (porque no es una letra) y continúa con la siguiente iteración de for.

  ```py
    for c in message:
        if not c.isalpha():
            cipher += c
            continue
  ```

  Si lo anterior no se cumple (significa que `c` sí es una letra) y si `c` es mayúscula entonces se guarda el punto de código de `c` en la variable `code` y se inicia un for iterando `i` en un rango del valor del argumento `steps`:

  ```py
    elif c.isupper():
        code = ord(c)
        for i in range(steps):
  ```

  Dentro del bucle for, se condiciona si `code` es igual a 90 (90 es el punto de código de la letra Z), de ser así, entonces code será igual a 65 (65 es el punto de código de la letra A) y continúa con la siguiente iteración de for. Si el filtro no se cumple, se actualiza la variable `code` en +1 (que será el punto de código resultante que reemplazará a `c`):

  ```py
    for i in range(steps):
        if code == 90:
            code = 65
            continue
        code += 1
  ```

  Al terminar el for, se actualiza la variable `cipher`, añadiendo el caracter correspondiente a `code`:

  ```py
    cipher += chr(code)
  ```

  Si la letra no es mayúscula, y si es minúscula, es el mismo planteamiento, con sus respectivos puntos de códigos:

  ```py
    elif c.islower():
        code = ord(c)
        for i in range(steps): #(97-122)
            if code == 122:
                code = 97
                continue
            code += 1
        cipher += chr(code)
  ```

Al terminar de iterar `c` en `message`, la función retorna la variable `cipher` con el mensaje cifrado.
