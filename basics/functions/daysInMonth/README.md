# daysInMonth()

> daysInMonth() recibe dos argumentos de tipo entero; year y month, y retorna un entero; la cantidad de días que tuvo el mes ingresado en función del año ingresado. Los argumentos se deben ingresar con la estructura yyyy para year y mm o m para month. El argumento year debe estar dentro de la era Gregoriana: year >= 1582

Se inicia el código con la función `isLeapYear()`, la cual toma un argumento (year) y determina si el año es bisiesto (retorna True) o no (retorna False), en dado caso de que el año no sea válido, se imprime en consola que no está dentro de la era Gregoriana (retorna None implicitamente, es decir, sin ser definido en el código).

Posteriormente, se define la función `daysInMonth()`, la cual toma dos argumentos (year, month)... esta función comienza asignando el valor `True` a la variable `bisiesto` con el objetivo de compararla más adelante con la invocación de la función `isLeapYear()`.

Después se declaran dos listas, una que contiene los meses de 30 días y otra los de 31 días, posteriormente, un condicional if compara la variable `bisiesto` con la invocación de `isLeapYear()`, otorgandole como argumento la variable `year`, la cual al mismo tiempo es argumento de la función `daysInMonth()`.

Si el condicional se ejecuta, el cuerpo de if verifica con las siguientes subcondiciones si la variable `month` (la cual es argumento también, recordemos que se pueden usar argumentos como variables siempre y cuando estén dentro de la función) se encuentra en las listas declaradas anteriormente, si no está en `meses30` ni `meses31`, se compara con el número 2 (mes de febrero) si se ejecuta esta última, retorna 29 (el numero de días de febrero en año bisiesto), si ninguna de las subcondiciones anteriores se ejecuta entonces retorna `None` (como ningún valor). Si la condicional if de `bisiesto == isLeapYear(year)` no se ejecuta, entonces pasa a `else` y repite el proceso con las subcondiciones, pero cambiando la línea de los días que tiene febrero (28) cuando no es bisiesto.

Después que Python lee las dos funciones y las aprende, ahora pasa a ejecutar el código posterior (de prueba):

Se declaran tres listas; `testYears`, `testMonths`, `testResults`, donde cada una de ellas contiene un valor que el `for` siguiente leerá: para `i` en el rango de la longitud de la lista `testYears`, se asigna el indice `i` de `testYears` de la iteración actual del `for` a la variable `yr`, lo mismo sucede con `testMonths` a la variable `mo` (la variable de control `i` se puede utilizar varias veces para controlar el código dentro del `for`, no está limitada a un solo uso).

Después de esto, se manda a imprimir el valor de `yr` y `mo` actual, seguido de una flecha `->` y un `end=""` (aquí el argumento de palabra clave `end`, permite unir el inmediato próximo `print` sin saltar una línea). Después, se asigna a la variable `result` el valor que retorna la función `daysInMonth()` con los argumentos de `yr` y `mo`, sobre sus valores actuales, dependiendo su iteración.

Finalmente, el condicional if realiza una comparación: si `result` (el valor que retornó `daysInMonth()`) es igual a `testResults[i]` (la lista de los resultados que deberían darse en funcion al año y mes de las otras listas) (aquí nuevamente se utiliza la variable de control), entonces se imprime `OK` (en la misma línea después de la flecha anterior `->`), si esta última condición no se cumple, entonces se imprime `Error` (igual, en la misma línea después de la flecha `->`).

El ciclo for se repite hasta la última iteración, y si el código es correcto, todos los datos de prueba en la salida de consola deberían ser `OK`.
