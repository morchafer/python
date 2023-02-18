# chistogram()

> chistogram() recibe como argumento el nombre de un archivo .txt como cadena (sin la extensión), y crea un archivo .hist registrando en él el número de veces que se repite cada una de las letras presentadas en el contenido del archivo de texto. Este archivo se crea en el mismo nivel de ruta que el archivo fuente.

## Inicia el bloque try-except:

`try:`

1. Se abre el stream del archivo que contiene los datos a leer: `fileR = open(file_name + '.txt', 'rt', encoding='utf-8')`

2. Se inicia el diccionario `letters` con las letras del alfabeto y con un valor inicial de `0` para cada una de las letras. Dicho diccionario servirá para almacenar el número de veces que la letra se repite en el archivo de texto.

3. Se itera sobre el contenido del archivo: `for ch in fileR.read():`

4. Se compara el byte (caracter) actual del archivo con cada clave (letra) de 'letters': `if ch.lower() == l:`. Si coinciden, entonces se incrementa en +1 el valor de dicha letra: `letters[l] += 1`

5. Se crea un diccionario que almacenará las letras que únicamente aparecen en el texto: `noZeroDict = {}`

6. Se itera en `letters` para identificar las letras cuyo valor sea cero, en tal caso, el código continúa con la siguiente iteración. Si no es el caso, significa que la letra de la iteración actual es diferente de cero, por lo tanto se almacena en `noZeroDict`:

   ```py
           for l in letters:
               if letters[l] == 0:
                   continue
               noZeroDict[l] = letters[l]
   ```

7. Se extraen los valores de `noZeroDict` y se almacenan como una lista en la variable 'val': `val = list(noZeroDict.values())`

8. Se inicia una variable de control para el próximo bucle while: `control = True`

9. Se crea una lambda que se utilizará para procesar el ordenamiento de los valores de las letras: `sortV = lambda a, b: a < b`

10. `while control:`

    1. Se apaga la variable de control: `control = False`

    2. Se itera en el rango de la longitud de la lista `val` menos uno; `-1` para evitar un error de indexación, debido a que en la siguiente línea del código se compara el elemento de la iteración actual con el siguiente. Si no se especificara `-1`, cuando el bucle for llegara al último elemento de la iteración, la línea siguiente intentaría comparar ese elemento (el último) con el siguiente elemento, lo que provocaría una excepción `IndexError`. Se especifica `-1` para que el bucle for itere hasta el penúltimo elemento: `for i in range(len(val) - 1):`

    3. Se utiliza la lambda `sortV` para verificar que el elemento de la lista `val` con un índice igual al número de la iteración actual sea `menor` (<) al elemento de la lista `val` con un índice igual al número de la iteración actual + 1, es decir, el siguiente elemento de la lista `val`. En la lambda se especificó que `a < b` para organizar el ordenamiento de mayor a menor; esto significa que el elemento con el valor más pequeño quedará al final de la lista y el elemento con el valor más grande quedará al inicio: `if sortV(val[i], val[i+1]):`

       **Nota:** Se utilizó un ordenamiento tipo burbuja para organizar los valores.

       Si la verificación de la lambda retorna `True`, entonces el código entra al cuerpo del if y vuelve a encender la variable de control para que el bucle while se siga repitiendo al terminar el bucle for.

       Posteriormente se realiza el cambio de valores en la misma lista `val`:

       ```py
         val[i], val[i+1] = val[i+1], val[i]
       ```

       Debido a que el elemento (de `val`) de la iteración actual es menor al siguiente elemento (de `val`) el elemento de la iteración actual debe recorrerse, por lo tanto se procesa la sobreescritura de valores: donde el 'espacio' (de la lista `val`) del elemento de la iteración actual ahora será igual al 'valor' del siguiente elemento de la lista `val`; y el 'espacio' del elemento siguiente ahora será igual al 'valor' del elemento de la iteración actual.

       Este proceso se repetirá (por el bucle while) hasta que la lambda `sortV` retorne `False`; esto significa que todos los elementos están ordenados de mayor a menor y no hay ningún elemento menor a su vecino siguiente; por lo tanto, el código no entraría al cuerpo de if, y la variable de control no se encendería de nuevo lo que provocaría el final del bucle while.

11. Se extraen las claves de `noZeroDict` y se almacenan como una lista en la variable 'key': `key = list(noZeroDict.keys())`

12. Se crea una lista que almacenará las claves (las letras) de la lista `key` en función del orden de los valores de la lista 'val': `sortList = []`

13. Se itera en la lista 'val': `for v in val:`

    - Se itera en el rango de la longitud de la lista 'key': `for k in range(len(key)):`

      - Si el elemento de la iteración actual de `val` (el cual es un entero) es igual al valor especificado de `noZeroDict` (se ingresa un índice de la lista `key` en función de su iteración actual, lo que devuelve una letra (una cadena), que sirve como argumento para la 'clave' de `noZeroDict`, cuyo procesamiento devuelve un entero), el código ingresa al cuerpo de if.

        Dentro del if, se agrega a `sortList` el elemento de la lista `key` cuyo índice es igual al valor de `k` de la iteración actual, y se borra de la lista `key` el elemento cuyo índice es igual al valor de `k` de la misma iteración. Posteriormente, se rompe el bucle for interno:

        ```py
          if v == noZeroDict[key[k]]:
              sortList.append(key[k])
              del key[k]
              break
        ```

14. Una vez que el procesamiento de los dos bucles for anteriores haya finalizado, entonces la lista `sortList` estará completa y las claves (las cadenas que contienen a cada letra) estarán en el orden correcto, es decir, en el mismo orden (índice) en el que sus 'valores' (los elementos de la lista `val`) se encuentran. Por lo tanto, se procede a cerrar el stream del archivo que contiene los datos leídos, ya que ya no será necesario: `fileR.close()`

15. Ahora, es momento de escribir nuestros datos en un archivo nuevo, para ello, se abre el stream y se crea el archivo que contendrá los datos procesados y en orden correcto. El stream del archivo se almacena en `fileW`:

    ```py
      fileW = open(file_name + '.hist', 'wt', encoding='utf-8')
    ```

16. Se inicia un contador con un valor inicial de 0: `count = 0`

17. Se itera en `sortList` para escribir en cada iteración sobre el archivo destino; se escribe el valor actual de `d` (el cual es alguna cadena de alguna letra), seguido de una cadena que contiene una flecha `->`, y finalmente el elemento de `val` con un índice igual al valor actual de `count`, convertido en una cadena (ya que es un entero). Este mismo formato de escritura también se imprime en consola para mostrar al usuario los datos escritos con éxito.

    Posteriormente, el contador se incrementa en +1; al hacer esto, en cada bucle for se escribirá el elemento de `val` cuyo índice será en función de `count`, y, como tanto `sortList` (que contiene las letras) como `val` (que contiene las cantidades de aparición de cada letra) están ordenadas correctamente, de manera que el elemento con el índice 0 de `val` pertenece al elemento con el índice 0 de `sortList`, entonces todos los datos se escribirán de manera correcta.

    ```py
      for d in sortList:
          fileW.write(d + ' -> ' + str(val[count]) + '\n')
          print(d + ' -> ' + str(val[count]))
          count += 1
    ```

18. Finalmente, una vez terminado el bucle for, se cierra el stream del archivo de escritura: `fileW.close()`

19. Si se produce algún error en cuanto al procesamiento de los archivos dentro del cuerpo de `try`, entonces se imprimirá en consola el error arrojado:

    ```py
      except Exception as e:
          print('Error:', strerror(e.errno))
    ```
