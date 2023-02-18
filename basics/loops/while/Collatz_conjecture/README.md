# Collatz Conjecture

1. Se inicializa la variable 'pasos' en cero: `pasos = 0`

2. Inicia un bucle `while True:` para validar que se ingrese un número entero mayor que cero

3. Condiciona a `c0` (el número) a que sea mayor que cero, de lo contrario (else) pide que ingrese nuevamente el valor

4. Inicia un bucle condicionando a que `c0` sea diferente de `1` (aquí empieza la conjetura de Collatz)

5. Aumenta en `1` la variable `pasos` para mantener el control de las vueltas dadas en el ciclo while

6. Condiciona si el residuo de la división `c0` entre `2` es igual a cero (es decir, número par):

   - Si la condición se cumple, se ejecuta la conjetura de Collatz: `c0 = c0 // 2`

   - Si la condición no se cumple, significa que el número es impar, por lo tanto se ejecuta la otra parte de la conjetura de Collatz: `c0 = 3 * c0 + 1`

7. En cada vuelta que el ciclo da, se va imprimiendo el valor actual de la variable `c0`

8. Con `continue` se para la ejecución del ciclo y vuelve a iniciar

9. Cuando la condición de `c0 != 1` de `while` resulte `False`, termina el ciclo y se imprimen los pasos totales, además, finaliza la ejecución de `while True` con `break`
