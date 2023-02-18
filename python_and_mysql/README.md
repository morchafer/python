# Python and MySQL

_-\*- coding: utf-8 -\*-_

_Created on Fri Oct 9 22:56:18 2020_

_@author: Fernando Morales_

El código está escrito para un correcto funcionamiento sobre la db de una tienda de libros, esto significa que campos como el nombre de la db o el nombre de la tabla están personalizados; si se ingresa otro nombre de db o de tabla que no concuerde con los parámetros del código, este ejemplo no funcionará.

Objetivos de las funciones:

- **login()** registra los datos de conexión a MySql (usuario, contraseña, host y base de datos).

- **table\_()** registra el nombre de la tabla y muestra su contenido actual.

- **form()** registra los datos del libro que se ingresará.

- **rollbackEval()** ingresa el libro a la tabla y evalúa sus datos:
  - si ya se encuentra en la tabla, se ejecuta rollback,
  - si no, no pasa nada, y el libro se queda en la tabla.
