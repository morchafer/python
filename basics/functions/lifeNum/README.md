# lifeNum()

> lifeNum() recibe tres argumentos; day, month y year como enteros (en ese orden), y retorna el número de la vida (entero) según tu fecha de nacimiento.

## Después del manejo de errores de la función:

- `for d in str(day): total += int(d)` Itera sobre el argumento 'day' y suma a 'total' cada valor entero 'd' de 'day', lo mismo para 'month' `for m in str(month): total += int(m)` y para 'year' `for y in str(year): total += int(y)`

- Se crea una lista que guarda por separado cada caracter numérico en forma de cadena de 'total': `totalList = list(str(total))`

- Se inicia un bucle infinito `while True:`, hasta que la condición no se cumpla

- `if len(totalList) > 1:` Comprueba si la longitud de totalList es mayor a 1, de ser así:

  1. Se reinicia la variable 'total': `total = 0`
  2. Se itera sobre la misma: `for t in totalList:` repitiendo el proceso de suma con los caracteres numéricos actuales: `total += int(t)`
  3. Se reinicia la lista (borra su contenido actual): `del totalList[:]`
  4. Se itera sobre 'total' en forma de cadena: `for tt in str(total):` y en cada iteración se va añadiendo el caracter numérico actual a la lista totalList: `totalList.append(tt)`

El proceso se repite (por el bucle While) hasta que la longitud de `totalList` NO sea mayor a 1 (es decir, que sea 1), cuando esto pasa, se ejecuta el `else` y se rompe el bucle While con `break`

Finalmente, la función retorna el valor actual de la variable `total`, que es el dígito de la vida.
