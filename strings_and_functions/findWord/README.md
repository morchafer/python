# findWord()

> findWord() recibe dos cadenas como argumentos; word y text. Retorna True si word se encuentra en text o False si no se encuentra.

Inicia la lógica de la función:

- Convierte los caracteres de ambas cadenas (`word` y `text`) en minúsculas, para evitar problemas de lectura.

  ```py
    word = word.lower()
    text = text.lower()
  ```

- Se crea una lista vacía, que después será llenada por valores de índices: `indexList = []`

- Se usará la variable `index` para guardar cada indice (irá cambiando de valor en cada iteración): `index = 0`

- Se inicia un bucle for que itera en la cadena `word`, de esta manera el método `find()` busca en la cadena `text` el caracter actual de `w` comenzando a buscar desde el índice `index` (0 inicialmente) y devuelve el índice de `w` en `text`, el cual se guarda en la misma variable `index`, para después agregar a la lista `indexList` el índice actual `index`.

  ```py
    for w in word:
        index = text.find(w, index)
        indexList.append(index)
  ```

- Si hay un -1 en `indexList` significa que el método `find()` no encontró algún o algunos caracteres, por lo que se retornará `False`; pero hay dos posibilidades. Es posible que los caracteres de `word` sí se encuentren dentro de `text`, pero no en el orden adecuado para formar la palabra. Para resolver esta pregunta se inicia un bucle for iterando `k` en `word` y se verifica que `k` se encuentre en `text`, de ser así, el contador aumenta en +1, y si el contador llega al mismo valor que la longitud de `word`, significa que los caracteres de `word` sí se encuentran en `text`, pero no en el orden correcto, por lo que se imprime un mensaje para notificar al usuario, y finalmente se retorna `False`.

  ```py
    if -1 in indexList:
        count = 0
        for k in word:
            if k in text:
                count += 1
                if count == len(word):
                    print("La palabra '" + word + "' no se encuentra dentro del texto '" + text + "'.")
                    print("Es posible que las letras de '" + word + "' se encuentren dentro de '" + text + "'")
                    print("pero no en el orden correcto para formar la palabra.")
                    return False
  ```

- Si `k` definitivamente no se encuentra en `text`, inmediatamente se retorna `False`:

  ```py
    if k in text:
        count += 1
        if count == len(word):
            print("La palabra '" + word + "' no se encuentra dentro del texto '" + text + "'.")
            print("Es posible que las letras de '" + word + "' se encuentren dentro de '" + text + "'")
            print("pero no en el orden correcto para formar la palabra.")
            return False
    else:
        return False
  ```

Si -1 no se encuentra en `indexList`, significa que el método `find()` sí encontró todos los caracteres de `word` en `text` y en el orden correcto para ser formada.
