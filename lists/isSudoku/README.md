# isSudoku()

> isSudoku() no recibe argumentos; pregunta por un conjunto de números y comprueba si su combinación es apta para ser Sudoku o no (retorna True o False).

## Verificando los datos de las filas:

Se crea una tupla con los dígitos de las filas ingresadas por el usuario (en realidad es una tupla de nueve cadenas), y se inicia un contador:

```py
  rows = (r1, r2, r3, r4, r5, r6, r7, r8, r9)
  count = 0
```

la variable `r` itera sobre la tupla `rows` que contiene a las cadenas, mientras tanto, en cada iteración se ejecuta un sub-bucle for, donde la variable `i` itera sobre el valor actual de la variable `r` (una cadena), donde a su vez, por cada iteración se ejecuta un tercer bucle, siendo el sub-bucle del sub-bucle, donde la variable `j` hace lo mismo que la variable `i`, pero se anida así porque es necesario comparar cada valor de `i` con `j`; si resultan iguales, el contador se actualiza en +1:

```py
  for r in rows:
      for i in r:
          for j in r:
              if i == j:
                  count += 1
```

Claramente `count` siempre tendrá el valor de `1` porque al comparar `i` con `j`, en una determinada iteración se comparará consigo mismo, por lo tanto, esta comparación debe ignorarse, por lo que se condiciona que el valor de count sea mayor a 1 para que no sea un sudoku, y retorne `False`. Si la condición anterior no se cumple, entonces se reinicia `count` y se siguen verificando los datos. El código quedaría de esta forma:

```py
  for r in rows:
      for i in r:
          for j in r:
              if i == j:
                  count += 1
          if count > 1:
              print("No es un Sudoku.")
              return False
          else:
              count = 0
```

## Verificando los datos de las columnas:

Se inicia la variable `x` que se utilizará como índice más adelante: `x = 0`

Se crean nueve cadenas para las nueve columnas, y se guardan en una tupla llamada `columns`:

```py
  c1, c2, c3, c4, c5, c6, c7, c8, c9 = '', '', '', '', '', '', '', '', ''
  columns = (c1, c2, c3, c4, c5, c6, c7, c8, c9)
```

Se itera `col` en la tupla columns para guardar el respectivo valor de cada columna. Inicialmente `x` vale 0, por lo que el indice es 0, por lo tanto en la primera iteración `col` se refiere a `c1` y guardará el valor con el índice cero de cada fila, y así sucesivamente con las nueve columnas. **Nota:** `x` se actualiza en cada iteración en +1.

```py
  for col in columns:
      col = r1[x] + r2[x] + r3[x] + r4[x] + r5[x] + r6[x] + r7[x] + r8[x] + r9[x]
      x += 1
```

Se crea un nuevo contador: `count_2 = 0`

Se itera `c` en `columns` (ya con las cadenas actualizadas), donde a su vez, en un sub-bucle, se itera `i` en el valor actual de `c` (una cadena que se refiere a una columna), donde a su vez, en otro bucle, siendo el sub-bucle del sub-bucle, se itera `j` en el valor actual de `c`, del mismo modo que con `i`. Se comparan los valores de `i` y `j` para verificar que no sean iguales; en dado caso de que lo sean, la variable `count_2` se actualiza en +1.

```py
  for c in columns:
      for i in c:
          for j in c:
              if i == j:
                  count_2 += 1
```

Se condiciona que `count_2` sea mayor a 1 (porque seguro será 1), si esto se cumple, entonces no es un sudoku (porque hay un dígito repetido) y retorna `False`. Si `count_2` no es mayor a 1, entonces no hay un dígito repetido, por lo tanto se reinicia `count_2` y se siguen verificando los datos. El código quedaría de esta forma:

```py
  for c in columns:
      for i in c:
          for j in c:
              if i == j:
                  count_2 += 1
          if count_2 > 1:
              print("No es un Sudoku.")
              return False
          else:
              count_2 = 0
```

## Verificando los datos de los campos 3x3s:

Una vez que se verificaron los datos de las filas y las columnas, y estos resultaron aptos para un posible Sudoku, finalmente se verifican los datos de los campos 3x3s, para dar un veredicto final.

Para esto se crean 9 variables nuevas (f1-f9) con rodajas de datos de sus respectivas filas:

```py
  f1 = r1[0:3] + r2[0:3] + r3[0:3]
  f2 = r1[3:6] + r2[3:6] + r3[3:6]
  f3 = r1[6:] + r2[6:] + r3[6:]
  f4 = r4[0:3] + r5[0:3] + r6[0:3]
  f5 = r4[3:6] + r5[3:6] + r6[3:6]
  f6 = r4[6:] + r5[6:] + r6[6:]
  f7 = r7[0:3] + r8[0:3] + r9[0:3]
  f8 = r7[3:6] + r8[3:6] + r9[3:6]
  f9 = r7[6:] + r8[6:] + r9[6:]
```

Estas variables (f1-f9) se guardan en una tupla llamada `fields`, y después se inicia un nuevo contador `count_3`.

```py
  fields = (f1, f2, f3, f4, f5, f6, f7, f8, f9)
  count_3 = 0
```

Posteriormente, se itera `f` en la tupla `fields`, y dentro de este for se itera `i` en el valor actual de `f`, nuevamente dentro de este último for se vuelve a iterar en `f` pero ahora con `j`, esto se hace para comparar los valores de `i` con `j` y determinar si hay algún dígito repetido en el campo que actualmente se itera, si `i` y `j` sí son iguales, entonces `count_3` se actualiza en +1, al finalizar el for de `j`, se presenta un condicional que pregunta si `count_3` es mayor a 1, si esto se cumple entonces no sería un sudoku, porque hay un dígito repetido y retornaría `False`. En caso de que `count_3` no sea mayor a 1 (es decir, que `count_3` sea 1) entonces pasa al else y se reinicia el contador a 0, después sigue iterando el bucle for para seguir con la verificación de los dígitos.

```py
  for f in fields:
      for i in f:
          for j in f:
              if i == j:
                  count_3 += 1
          if count_3 > 1:
              print("No es un Sudoku.")
              return False
          else:
              count_3 = 0
```

**Nota:** debe ser mayor a 1, porque `count_3` siempre tendrá por defecto el valor de 1, puesto que al momento de iterar dos variables (`i` y `j`) en una misma secuencia y compararlas después, claramente serán iguales en alguna determinada iteración, por lo tanto `count_3` tendrá el valor de 1 y es garantía; sin embargo si en posteriores iteraciones las variables vuelven a ser iguales, significa que hay un dígito dos veces en la misma secuencia.

Finalmente, si el bucle for termina con exito de iterar sobre `fields`, significa que los datos ingresados inicialmente sí cumplen la característica de ser un Sudoku, por lo tanto se terminan las verificaciones (se podrían decir filtros) e imprime que `Sí es un Sudoku`, y retorna `True`.

```py
  print("Sí es un Sudoku.")
  return True
```
