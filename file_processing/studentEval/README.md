# studentEval()

> studentEval() recibe como argumento el nombre de un archivo .txt como cadena (sin la extensión) e imprime en consola un resumen de su contenido. El contenido de este archivo debe estar escrito con una estructura especial, puesto que se utiliza como base de datos para almacenar registros. Para más información se puede utilizar como argumento `help` que funciona como una palabra reservada del programa (por lo tanto no se podría leer un archivo "help.txt").

## Bloque try-except dentro de la función `studentEval()`

### Procesamiento del stream del archivo:

1. Se abre el stream del archivo a ser procesado: `file = open(file_name + '.txt', 'rt', encoding='utf-8')`

2. Se invoca al método `readlines()` para leer el archivo que contiene los datos a procesar, y el retorno del método se guarda en la variable 'fileR': `fileR = file.readlines()`

3. Una vez obtenidos los datos del archivo de texto, ya no es necesario tener el stream abierto, por lo que se procede a cerrar el stream: `file.close()`

### Inicia el manejo de errores para la excepción `EmptyFileError`:

1. Asegura que `fileR` (fileR es la lista que retornó el método `readlines()` cuyo contenido de cada elemento es cada línea del archivo), no esté vacía; de lo contrario pasa a levantarse la excepción `EmptyFileError`:

   ```py
     if fileR == []:
         raise EmptyFileError
   ```

2. Se crea una variable para controlar el flujo del bucle for siguiente: `for_control = False`

3. Se itera la variable de control `line` en el rango de la longitud de `fileR`:

   ```py
     for line in range(len(fileR)):
   ```

   Dentro del bucle anterior, se inicia un sub-bucle para iterar byte por byte sobre cada elemento de `fileR` (es decir, cada línea):

   ```py
     for byte in fileR[line]:
   ```

   Después se verifica que el byte de la iteración actual sea un espacio, un tabulador, o un salto de línea; en caso de ser alguno de ellos, el bucle continúa con la siguiente iteración:

   ```py
     if byte.isspace() or byte == '\t' or byte == '\n':
         continue
   ```

   En caso de que el byte actual no sea ni espacio, ni tabulador, ni salto de línea, se enciende `for_control`, y se rompe el sub-bucle for:

   ```py
     for_control = True
     break
   ```

   Después, con el valor actual de `for_control`, se accede al cuerpo del if, y se rompe el bucle for principal. De esta manera, el programa estaría entendiendo que el archivo no está vacío, ya que una de sus líneas contiene un caracter que no es ni espacio, ni tabulador, ni salto de línea, por lo tanto debe ser algún caracter visible:

   ```py
     if for_control:
         break
   ```

   Por el contrario, si el sub-bucle for termina sus iteraciones sin encender `for_control`, significa que el if que condiciona que byte sea espacio, tabulador o salto de línea, siempre se estuvo ejecutando; en ese caso, al terminar las iteraciones del sub-bucle for, el siguiente if no se podría ejecutar (porque `for_control` es `False`), por lo tanto el código pasa a verificar la condición de elif, que dicta que, si `line` (`line` en sí es un entero, ya que el bucle principal se iteró en un rango de valores) es igual a la longitud de `fileR`-1 entonces el código accede al cuerpo de elif y levanta la excepción `EmptyFileError`:

   ```py
     elif line == len(fileR)-1:
         raise EmptyFileError
   ```

   **Nota:** la condición es: `line == len(fileR)-1` porque la función `range()` (la cual se utilizó para iterar en el bucle principal), comienza a contar sus valores desde el índice 0 y, lo que se trata de verificar con la condición elif, es que el bucle principal se encuentre en su última iteración (iterando en la última línea del archivo), porque de ser así si ningún byte de la última línea del archivo es espacio, tabulador, o salto de línea, significa que el archivo está vacío (vacío de caracteres visibles), por lo tanto, se debe levantar la excepción `EmptyFileError`.

Finaliza el manejo de errores para la excepción `EmptyFileError`.

Se inicializan las variables necesarias para el procesamiento de la función:

```py
  students = {}
  line_number = 0
  name = ''
  lastname = ''
  full_name = ''
  score = ''
  score_2 = ''
  name_control = True
  lastname_control = True
  dot_control = False
  float_control = False
  int_counter = 0
  spaces_counter = 0
```

Se itera en un bucle for para verificar que la línea de la iteración actual termine con un salto de línea, de ser así, el código continúa con la siguiente iteración del bucle for, de lo contrario, se agrega un salto de línea a la línea de la iteración actual:

```py
  for n in range(len(fileR)):
      if fileR[n].endswith('\n'):
          continue
      fileR[n] += '\n'
```

Posteriormente, nuevamente se inicia un bucle for que itere la variable de control `line` en `fileR`. Dentro del cuerpo del bucle se actualiza la variable `line_number` cuyo propósito es almacenar el número de línea actual (para ayudar en el feedback de los errores), se reemplazan de `line` los tabuladores por espacios y la línea modificada se almacena en `line_2`:

```py
  for line in fileR:
      line_number += 1
      line_2 = line.replace('\t', ' ')
```

- Dentro del actual bucle for, se inicia un sub-bucle for que itera sobre `line_2`, para verificar que el caracter actual de la línea sea un espacio. En dado caso, se actualiza el contador de espacios en +1; de lo contrario se pasa a la siguiente iteración:

  ```py
    for spcs in line_2:
        if spcs == ' ':
            spaces_counter += 1
  ```

- Siguiendo con el bucle for principal, se verifica que `spaces_counter` sea diferente de 2; de ser así se levanta la excepción `LineError`, de lo contrario (es decir, si `spaces_counter` es igual a 2) el código pasa a ejecutar el `else` siguiente:

  ```py
    if spaces_counter != 2:
        raise LineError
    else:
  ```

  **Nota:** es necesario que `spaces_counter` sea igual a 2, ya que esto significa que el bucle for anterior encontró dos espacios en la línea del archivo; dichos espacios son importantes para el correcto procesamiento de los datos de la línea, ya que el formato de cada línea debe ser:

  `[nombre][espacio][apellido][espacio][puntaje]`

  Los espacios funcionan como separadores de cada dato del estudiante; es importante que antes de iniciar el procesamiento de los datos, se verifique que el formato de cada línea sea el adecuado para continuar.

  En caso de que el código haya pasado el filtro anterior acerca del formato de forma exitosa, entonces pasará a ejecutar el procesamiento (`else`).

  Dentro del cuerpo de `else`, se encuentran dos bucles for generales; uno es para realizar los filtros del procesamiento del nombre y apellido del estudiante, y el otro es para realizar los filtros del procesamiento del puntaje del estudiante. Ambos bucles for iteran en un mismo rango de valores; en el rango de la longitud de `line_2`.

  **Nota:** se hizo de esta manera para mantener la sencilla legibilidad del código, aunque también es posible omitir el segundo bucle for e integrar su if dentro del primer bucle for pasándolo como elif.

  - Bucle for para el procesamiento del nombre y apellido del estudiante.

    Se inicia el bucle for iterando en un rango de valores igual a la longitud de `line_2`:

    ```py
      for ch in range(len(line_2)):
    ```

    Se condiciona que el caracter (cuyo índice es el de `ch` de la iteración actual) de `line_2` sea un espacio, de ser así, significa que el procesamiento de la línea (de `line_2`) ha llegado al primer divisor, por lo tanto, todo lo que se encuentre a la izquierda de ese divisor (del espacio) debe ser el nombre del estudiante; aunque esto no se da por hecho, por lo que en las próximas líneas se comprueba con algunos filtros que el nombre sea adecuado.

    ```py
      if line_2[ch].isspace():
    ```

    Entonces, una vez que el bucle for se encuentra con el primer espacio, el código pasa a ejecutar el if de `name_control` (cuyo valor inicial es `True`). Dentro del cuerpo de este if es donde se realiza la comprobación a través de algunos filtros construidos con condicionales.

    Primeramente, se toma de `line_2` un slice que va desde el inicio (desde el inicio de la línea) hasta el valor de `ch` actual; el valor de `ch` actual es el índice del espacio (del divisor) por lo tanto el código tomará el slice desde el inicio hasta un elemento antes del índice `ch`. Este slice se guarda en la variable `name`, y dicha variable es la que se utilizará para realizar las comprobaciones con los filtros, para verificar que el nombre del estudiante sea adecuado.

    ```py
      if name_control:
          name = line_2[:ch]
    ```

    El primer filtro que se realiza es la comprobación de que `name` no esté vacío (porque puede suceder que el primer elemento de `line_2` sea un espacio, de ser así, entonces no habría nada a su izquierda, por lo tanto no se agregaría nada a la variable `name`); si la longitud de `name` es diferente de cero, significa que no está vacía, por lo que el código pasa el primer filtro.

    ```py
      if len(name) != 0:
    ```

    Después, dentro del cuerpo del if del primer filtro, se inicia un bucle for iterando `n` en `name` (name es una cadena en todo momento) para realizar las comprobaciones del segundo filtro, que verifica que `n` (el caracter de `name` de la iteración actual) sea una letra, en dado caso, el código continúa con la siguiente iteración para comprobar el siguiente caracter; de lo contrario, significa que encontró un caracter que no es una letra, por lo tanto `name` no es adecuada para nombre de estudiante, por lo que se levanta la excepción `LineError`.

    ```py
      for n in name:
          if n.isalpha():
              continue
          raise LineError
    ```

    En caso de que `name` no haya pasado el primer filtro, se levanta la excepción `LineError`:

    ```py
      else:
          raise LineError
    ```

    Una vez comprobados los filtros anteriores, significa que `name` sí es adecuada para nombre de estudiante; que no está vacía y que contiene solamente letras (o una sola letra, si `name` contiene solamente un elemento).

    Posteriormente, se concatena un espacio a la variable `name`, con el objetivo de darle estética al formato al momento de imprimir los datos en consola (este espacio divide al nombre y al apellido del estudiante): `name += ' '`

    Finalmente, se desactiva `name_control`; el procesamiento del nombre del estudiante ha terminado: `name_control = False`

    Luego, el bucle for seguirá iterando en el rango de valores de la longitud de `line_2`, tomando cada valor numérico de cada iteración como índice para determinar si el caracter del índice (cuyo valor es el de la iteración actual) es un espacio; después de procesar el nombre y de haber pasado la iteración del primer espacio, el bucle for pasa las iteraciones de los siguientes caracteres, hasta encontrar el segundo espacio (el segundo divisor); es por eso que desde antes es necesario asegurar que `line_2` tenga exactamente dos espacios, no más, no menos, solo dos. Una vez que se encontró el segundo espacio, nuevamente el código entra al cuerpo del if inicial, y, como `name_control` se desactivó, porque el código ya pasó por el procesamiento del nombre anteriormente, ahora pasa a ejecutar el elif de `lastname_control`, cuyo valor inicial es `True`. Dentro del cuerpo del elif de `lastname_control` se realizan prácticamente las mismas operaciones que en el procesamiento de `name_control`.

    Primeramente se toma un slice que va desde el valor de la longitud de `name` hasta el valor actual de `ch`; al hacer esto, se estarían tomando solamente los caracteres que corresponden al apellido del estudiante (sin contar el primero ni el segundo espacio); luego este slice se almacena en la variable `lastname`, y se pasan a realizar los filtros correspondientes.

    ```py
      elif lastname_control:
          lastname = line_2[len(name):ch]
    ```

    Se comprueba que `lastname` no esté vacío:

    ```py
      if len(lastname) != 0:
    ```

    En tal caso, se itera en `lastname` para comprobar que todos los caracteres son letras. Con un solo caracter que no cumpla la condición, se pasa a levantar la excepción `LineError`:

    ```py
      for ln in lastname:
          if ln.isalpha():
              continue
          raise LineError
    ```

    En caso de que `lastname` esté vacío, se levanta la excepción `LineError`:

    ```py
      else:
          raise LineError
    ```

    Si todo sale bien, y `lastname` pasa los filtros anteriores, se concatena un espacio a su cadena: `lastname += ' '`

    Una vez listas las variables `name` y `lastname` estas se concatenan para formar el nombre completo del estudiante, y se almacena la cadena resultante en la variable `full_name`:

    ```py
      full_name = name + lastname
    ```

    Finalmente, se desactiva `lastname_control`, lo que significa que el procesamiento del apellido del estudiante ha terminado: `lastname_control = False`

    Después, el bucle for seguirá iterando en su rango de valores, hasta llegar al último elemento y finalizar su ciclo; después del segundo divisor (el segundo espacio), ya no hay más espacios en `line_2`, por lo tanto, el código simplemente espera el final del bucle for para seguir con el procesamiento del puntaje del estudiante.

  - Bucle for para el procesamiento del puntaje del estudiante.

    Una vez procesados el nombre y el apellido del estudiante, lo siguiente es procesar el puntaje; para ello se abre otro bucle for iterando en el mismo rango de valores que el anterior; en la longitud de `line_2`.

    **Nota:** se hizo de esta manera para mejorar el entendimiento del flujo del código y la legibilidad del mismo.

    Se inicia el bucle for iterando en un rango de valores igual a la longitud de `line_2`:

    ```py
      for ch in range(len(line_2)):
    ```

    Ahora aquí, el controlador de ejecución del condicional if es el salto de línea (`\n`); se hizo de esta manera, porque después del puntaje del estudiante, no debería haber otra cosa en la línea del archivo, por lo tanto debería saltar a la siguiente línea incluso si el archivo contiene solo una línea, desde antes se aseguró que todas las líneas del archivo contengan un salto de línea; y como el salto de línea es realmente el último elemento que puede tener una línea del archivo, se utiliza el índice de `ch` en el que se encuentre para la creación de `score` en la siguiente línea del código.

    ```py
      if line_2[ch] == '\n':
    ```

    **Nota:** el controlador de ejecución del condicional if del bucle anterior, es el espacio; en el bucle anterior si el caracter de `line_2` no era un espacio, no pasaba nada, y pasaba a la siguiente iteración; en este bucle, si el caracter de `line_2` no es un salto de línea, no se ejecuta nada, y pasa a la siguiente iteración, esto significa que el bucle for recorrerá todos los elementos de `line_2` hasta llegar al último (el cual es el salto de línea), y validará la condición de if.

    Una vez dentro del cuerpo de if, se toma un slice que va desde el valor numérico de la longitud de `full_name` hasta el valor actual de `ch` (el valor actual de `ch` es el último índice de `line_2`); al hacer esto, se estarían tomando solamente los caracteres correspondientes al puntaje del estudiante, aunque esto no se da por hecho, por lo que en las siguientes líneas del código se realizan los filtros necesarios. La cadena resultante del slice se almacena en la variable `score`:

    ```py
      score = line_2[len(full_name):ch]
    ```

    Después, inician los filtros para `score`; primeramente se comprueba que `score` no esté vacío:

    ```py
      if len(score) != 0:
    ```

    Si pasa el primer filtro, entonces se inicia un bucle for para verificar que el caracter de `score` cuyo índice es el valor actual de `sc`, sea un dígito; si lo es, se pasa a la siguiente iteración del bucle for; si no lo es, entonces puede que sea un punto (.) decimal.

    ```py
      for sc in range(len(score)):
          if score[sc].isdigit():
              continue
    ```

    **Nota:** el puntaje del estudiante solo puede contener números y un solo punto que separe los enteros de los decimales; aunque no es necesario que el puntaje contenga decimales, pero es una posibilidad que se debe tomar en cuenta. Sin embargo, el puntaje también tiene limitantes respecto a la cantidad de enteros y decimales que se pueden presentar (este filtro se encuentra más adelante).

    Si el caracter de `score` cuyo índice es el valor actual de `sc` no es un dígito, entonces cabe la posibilidad de que sea un punto, para ello se realizan algunas comprobaciones con el elif siguiente: el caracter claramente debe ser un punto, pero además, `dot_control` debe ser igual a `False` (False es su valor inicial), y además también, el valor actual de `sc` debe ser diferente al valor resultante de la longitud de `score` menos 1, en otras palabras, el valor de `sc` debe ser diferente al valor del índice del último elemento de `score`, puesto que el punto decimal no puede encontrarse al final del puntaje, sino entre valores numéricos separando enteros de decimales, o al inicio, si el puntaje contiene solo valores decimales y no enteros. Estas tres condiciones deben cumplirse para que el punto decimal se encuentre en el espacio adecuado; si una sola de las tres no se cumple, entonces no hay más posibilidades de lo que pudiera ser el caracter de `score` de la iteración actual, por lo tanto se pasa a levantar la excepción `LineError` en el else.

    ```py
      elif score[sc] == '.' and dot_control == False and sc != len(score)-1:
    ```

    Si se verifican las tres condiciones, entonces se pasa a activar la variable `dot_control`, señalando que un punto decimal ya ha sido procesado:

    ```py
      dot_control = True
    ```

    Si ni el if ni el elif se cumplen, se levanta la excepción `LineError`:

    ```py
      else:
          raise LineError
    ```

    Si todo sale bien, y no se levanta la excepción `LineError`, entonces `score` ha pasado los filtros, por lo tanto es adecuado para el procesamiento del puntaje, sin embargo, aunque sea adecuado (con adecuado se quiere dar a entender que contiene los caracteres adecuados para el procesamiento, en este caso números y/o un punto), puede que no sea apto, es decir, que exceda los límites en cuanto a cantidad de enteros y decimales que el puntaje del estudiante requiere. El número máximo de enteros que el puntaje puede presentar son 4, esto significa, que si en el archivo de texto, en el puntaje de algún estudiante se presentan 5 enteros, se produciría una excepción (`IntCounterError`). Mientras que en los decimales no existe un límite (ya que solamente se toman en cuenta dos decimales con ayuda de un filtro más adelante), lo recomendable es no ingresar más de 2 decimales en el puntaje del estudiante.

    Para realizar estas comprobaciones se añadió el siguiente filtro; se itera `sc` en el rango de valores igual a la longitud de `score`. En cada iteración se verifica con un condicional que el caracter de `score`, cuyo índice es igual al valor actual de `sc`, sea diferente a un punto (.), y que además `float_control` sea igual a `False` (False es su valor inicial). Si estas condiciones se cumplen, el código entra al cuerpo de if.

    ```py
      for sc in range(len(score)):
          if score[sc] != '.' and float_control == False:
    ```

    Dentro del cuerpo de if, se actualiza el valor de `int_counter` en +1 (señalando que el caracter de la iteración actual es un entero ya que no se ha presentado ningún punto decimal).

    ```py
      int_counter += 1
    ```

    Una vez actualizado el contador de enteros, el código verifica que `int_counter` no haya excedido el límite de enteros (4). Si es así, entonces se levanta la excepción `IntCounterError`:

    ```py
      if int_counter > 4:
          raise IntCounterError
    ```

    Si no es así, el código sigue con la línea siguiente, en donde se va concatenando el caracter de cada iteración en la variable `score_2`.

    ```py
      score_2 += score[sc]
    ```

    **Nota:** se utilizó la variable `score_2` para almacenar el puntaje del estudiante limitado con dos decimales (si es que los tiene); este filtro se encuentra más adelante.

    Una vez que se agregó el caracter de `score` a `score_2`, el bucle continúa con la siguiente iteración.

    En caso de que el puntaje del estudiante contenga un punto decimal, cuando el bucle for llegue a él y el if verifique que el caracter de la iteración actual (que sería el punto) no es diferente a '.' (es decir, a un punto), entonces no se ejecutará el cuerpo de if, y el código pasará a encender la variable `float_control`, señalando que el bucle for ha encontrado un punto en `score`, por lo tanto los caracteres de las siguientes iteraciones ya no serían enteros, sino decimales.

    ```py
      float_control = True
    ```

    Y del mismo modo, se concatena el caracter de la iteración actual con `score_2`.

    ```py
      score_2 += score[sc]
    ```

    Después, el flujo del código ya no entraría al cuerpo del primer if, en donde se verifica la existencia de algún punto; esto porque (aunque los próximos caracteres sí sean diferentes a un punto), la variable `float_control` se activó, por lo tanto no volverá a ser igual a `False` (hasta que se reinicien los valores de las variables). Esto significa que el valor que `int_counter` tiene actualmente es el número de enteros que el puntaje del estudiante tiene; este valor (del contador de enteros) se utiliza para limitar el número de decimales a concatenar en `score_2`, en el siguiente filtro:

    Si la longitud de `score_2` es igual al número de enteros que hay + 3, entonces se rompe el ciclo for, porque se ha llegado a un valor apto para el procesamiento del puntaje.

    ```py
      if len(score_2) == int_counter+3:
          break
    ```

    **Nota:** en la condición se suman `int_counter` + 3 porque: `score_2` ya contiene los enteros en su cadena (si es que los hay), por lo tanto su longitud es mayor al número de enteros, sin embargo lo que se quiere lograr es limitar el número de decimales, para esto se condiciona que la longitud de `score_2` (la cual se irá actualizando en cada concatenación) sea igual al número de enteros + 3; + 3 porque se cuentan tres caracteres después de los enteros, que serían el punto decimal y los dos decimales que se limitan.

Una vez que TODOS los filtros se pasaron con éxito, tanto del nombre, apellido y puntaje del estudiante, lo siguiente es almacenar los datos del estudiante en un diccionario, donde la clave sea el nombre y el apellido, y el valor sea el puntaje. Para esto se utiliza el diccionario `students`. Sin embargo, antes de comenzar a guardar los datos, se necesita un filtro más; el objetivo de este filtro es sencillo: básicamente es recortar la longitud (bastante considerable) de `full_name` (cadena que contiene el nombre y el apellido del estudiante); esto realmente se hace con el fin de seguir un orden en el formato de impresión en consola al momento de mostrar los datos; la cantidad máxima de caracteres que puede tener `full_name` es 30, la cual es suficiente para mostrar un nombre y un apellido. El filtro es el siguiente:

Si la longitud de `full_name` es mayor que 30, entonces se re-escribe `full_name` tomando un slice desde su elemento con índice 0 hasta su elemento con índice 29.

```py
  if len(full_name) > 30:
      full_name = full_name[:30]
```

Una vez comprobado el filtro anterior, ahora sí, lo siguiente es almacenar los datos en el diccionario `students`; primero se comprueba si `full_name` ya se encuentra en el diccionario (ya que no pueden haber dos claves iguales); esto debido a que en el archivo de texto puede aparecer el mismo estudiante varias veces y no solo una vez; si es el caso, entonces simplemente se sumarían los puntajes del estudiante:

```py
  if full_name in students:
```

Si el nombre del estudiante ya está almacenado en el diccionario, entonces se utiliza `full_name` como clave para retornar el valor (el puntaje) del estudiante y sumarle el valor de `score_2` convertido a float (ya que `score_2` sigue siendo una cadena, pero es apta para realizar la conversión a float).

```py
  students[full_name] += float(score_2)
```

Si el nombre del estudiante no se encuentra en el diccionario, significa que es nuevo, por lo tanto se añade otro elemento al diccionario `students` dándole a `full_name` como clave y a `score_2` convertido a float como puntaje.

```py
  else:
      students[full_name] = float(score_2)
```

Finalmente, una vez almacenados los datos del estudiante (de una sola línea), se reinician los valores de las variables preparándolas para la siguiente iteración del bucle for (`for line in fileR`) para procesar la siguiente línea del archivo de texto.

```py
  name = ''
  lastname = ''
  full_name = ''
  score = ''
  score_2 = ''
  name_control = True
  lastname_control = True
  dot_control = False
  float_control = False
  int_counter = 0
  spaces_counter = 0
```

Una vez que el procesamiento de todas las líneas del archivo haya finalizado, y, por lo tanto, el bucle for (`for line in fileR`) haya terminado, lo siguiente es preparar la presentación de los datos para la impresión en pantalla.

Para ello se crea una lista llamada `sKeys` con las claves (nombres y apellidos) del diccionario `students` y se aplica el método `sort()` para ordenar la lista alfabeticamente.

```py
  sKeys = list(students.keys())
  sKeys.sort()
```

Después, se utiliza la lista `sKeys` para iterar sobre ella y realizar algunas operaciones para dar estética al formato de salida.

Se imprime el encabezado de la tabla de los datos:

```py
  print('\n+======== PUNTAJE GENERAL DE CADA ESTUDIANTE ========+')
```

Se itera la variable de control `s` en `sKeys`:

```py
  for s in sKeys:
```

Se resta de 32 la longitud de `s` (`s` es el nombre y apellido de algún estudiante); se resta de 32, debido a que el número máximo de caracteres que puede tener el nombre y apellido del estudiante es 30, sin embargo, para dar un margen a estos casos (en los que el nombre y el apellido del estudiante tienen 30 caracteres juntos), se les resta de 32. El resultado de esta resta se almacena en la variable `spaces`, y después se imprimen una serie de separadores (`|`), tabuladores y un salto de línea para dar formato a la tabla, seguido del nombre y apellido del estudiante (`s`), y se termina el print con el argumento de palabra clave `end=''` para que el siguiente print se muestre enseguida del anterior, en la misma línea:

```py
  spaces = 32 - len(s)
  print('|\t\t\t\t    |\t\t     |\n|   ' + s, end='')
```

Después se itera `sp` en el rango del valor de `spaces`, esto con el fin de imprimir el número de espacios necesarios para imprimir el siguiente separador de la tabla (el que divide el nombre y apellido, del puntaje); de esta manera, la tabla queda con un formato ordenado y único, y no se distorsiona su estructura con los diferentes nombres y apellidos de los estudiantes:

```py
  for sp in range(spaces):
      print(' ', end='')
```

Se imprime el separador que divide al nombre y apellido, del puntaje:

```py
  print('|    ', end='')
```

Después, se reutiliza la variable `spaces` para el mismo objetivo, pero ahora en función del puntaje; para ello se resta de 7 la longitud del valor que retorna la clave `s` del diccionario `students` convertido a una cadena (ya que es un float, y se necesita calcular su longitud):

```py
  spaces = 7 - len(str(students[s]))
```

Se crea la variable `spaceString` con el valor de una cadena vacía, con el objetivo de almacenar los espacios necesarios para la impresión:

```py
  spaceString = ''
```

Se vuelve a iterar en el rango del nuevo valor de `spaces` para concatenar los espacios necesarios a la cadena `spaceString` en función del número de iteraciones dadas:

```py
  for sp in range(spaces):
      spaceString += ' '
```

Una vez terminado el bucle for, se concatena la cadena `spaceString` (que contiene los espacios) con el valor que retorna la clave `s` del diccionario `students` convertido a una cadena para poder concatenarla (ya que el puntaje es un dato tipo float):

```py
  spaceString += str(students[s])
```

Finalmente se imprime la cadena `spaceString`, la cual ya contiene el puntaje del estudiante con los espacios necesarios para no distorsionar la estructura de la tabla; seguido de algunos espacios y un separador final que termina la línea actual de la tabla. El bucle for que itera en `sKeys` repite estas operaciones con los datos de cada estudiante:

```py
  print(spaceString + '     |')
```

Por último, se imprimen el margen y la línea inferior de la tabla:

```py
  print('|\t\t\t\t    |\t\t     |')
  print('+====================================================+\n')
```
