# Hundir la Flota

Proyecto de Python que implementa una versión sencilla del juego
**Hundir la Flota**. Está dividido en dos archivos para separar las
funciones del juego de la lógica que organiza la partida.

## Contenido del proyecto

-   `hundir_la_flota_main.py`: inicia y controla la partida.
-   `hundir_la_flota_funciones.py`: contiene las funciones para crear el
    tablero, colocar barcos, recibir disparos y comprobar si quedan
    barcos.

> **Importante:** el archivo principal importa las funciones con
> `import hundir_la_flota_funciones as hf`. Por eso, ambos archivos
> deben estar en la misma carpeta y conservar esos nombres, o habrá que
> actualizar el `import`.

## Requisitos

-   Python 3.
-   NumPy.

Instala NumPy desde una terminal:

``` bash
python -m pip install numpy
```

## Cómo ejecutar el juego

Abre una terminal en la carpeta donde están los dos archivos y ejecuta:

``` bash
python hundir_la_flota_main.py
```

El programa pide el tamaño del tablero y después coloca los barcos. En
el código actual, el tamaño debe introducirse como un número entero.

## Símbolos del tablero

  Símbolo   Significado
  --------- --------------------------------------------
  `_`       Casilla vacía o agua
  `O`       Parte de un barco sin tocar
  `X`       Parte de un barco alcanzada por un disparo

Cuando se dispara a una casilla con barco (`O`), se cambia a `X` y se
muestra `Tocado`. Si la casilla no contiene un barco, se muestra `Agua`.

## Archivo `hundir_la_flota_funciones.py`

Este archivo importa NumPy y `random`, y define las funciones que
utiliza la partida.

### `crear_tablero(size=10)`

Crea un tablero cuadrado de NumPy con el tamaño indicado. Si no se pasa
ningún argumento, crea un tablero de `10 × 10` lleno de guiones bajos
(`_`).

``` python
tablero = crear_tablero()
tablero_pequeno = crear_tablero(5)
```

-   `size`: número de filas y columnas.
-   `np.full((size, size), "_")`: genera una matriz del tamaño
    solicitado y rellena todas sus posiciones con `_`.
-   `return tablero`: devuelve la matriz creada.

### `crea_barco_aleatorio(tablero, eslora=4, num_intentos=100)`

Intenta colocar aleatoriamente un barco recto en el tablero.

1.  Obtiene el número de filas y columnas mediante `tablero.shape`.
2.  Elige una coordenada inicial al azar.
3.  Elige una orientación: norte (`N`), sur (`S`), oeste (`O`) o este
    (`E`).
4.  Construye una lista de coordenadas consecutivas según la eslora y la
    orientación.
5.  Llama a `coloca_barco_plus()` para comprobar si el barco cabe y si
    sus casillas están libres.
6.  Si la colocación no es válida, vuelve a intentarlo; si es válida,
    devuelve el tablero actualizado.

**Parámetros:** - `tablero`: matriz donde se colocará el barco. -
`eslora`: longitud del barco; por defecto, `4`. - `num_intentos`:
aparece en la firma de la función, pero actualmente no se utiliza para
limitar los intentos.

### `coloca_barco_plus(tablero, barco)`

Comprueba si se puede colocar un barco en las coordenadas recibidas.

-   Crea una copia del tablero con `tablero.copy()`.
-   Comprueba que cada coordenada esté dentro de los límites.
-   Comprueba que no haya ya un barco en la casilla (`O` o `X`).
-   Si encuentra un problema, muestra un mensaje y devuelve `False`.
-   Si todas las coordenadas son válidas, marca las casillas con `O` y
    devuelve la copia del tablero.

El barco se representa como una lista de tuplas, por ejemplo:

``` python
barco = [(2, 3), (2, 4), (2, 5)]
```

Cada tupla contiene `(fila, columna)`.

### `recibir_disparo(tablero, coordenada)`

Procesa un disparo en una coordenada concreta.

-   Si la casilla contiene `O`, la cambia a `X` y muestra `Tocado`.
-   Si ya contiene `X`, muestra que hay que disparar a otro sitio.
-   En cualquier otro caso, muestra `Agua` y deja la casilla como `_`.
-   Devuelve el tablero.

La coordenada se pasa como una tupla:

``` python
tablero = recibir_disparo(tablero, (2, 3))
```

### `quedan_barcos(tablero)`

Comprueba si el tablero todavía contiene alguna parte de barco sin tocar
(`O`).

``` python
if quedan_barcos(tablero):
    print("Todavía quedan barcos")
```

Utiliza `np.any(tablero == "O")`: devuelve `True` si existe al menos una
casilla con `O`; de lo contrario, devuelve `False`.

## Archivo `hundir_la_flota_main.py`

Este archivo importa `random` y las funciones del otro módulo con el
alias `hf`.

### Función `jugar()`

Organiza la partida en estos pasos:

1.  Muestra el título del juego.
2.  Pide el tamaño del tablero.
3.  Crea el tablero del jugador.
4.  Define la flota con `barcos = [2, 2, 2, 3, 3, 4]`: tres barcos de
    eslora 2, dos de eslora 3 y uno de eslora 4.
5.  Coloca esa flota en el tablero del jugador.
6.  Crea otro tablero y coloca la misma flota para el enemigo.
7.  Entra en un bucle de juego mientras se cumpla la condición escrita
    con `quedan_barcos()`.
8.  Pide al jugador una fila y una columna para disparar al tablero
    enemigo.
9.  Genera una coordenada aleatoria para el disparo de la máquina contra
    el tablero del jugador.
10. Muestra el tablero del jugador actualizado.

Al final del archivo se llama a `jugar()`, por lo que la partida empieza
cuando se ejecuta el script.

## Conceptos de Python utilizados

-   **Funciones (`def`)**: separan el programa en tareas más pequeñas.
-   **Parámetros**: permiten pasar el tablero, la eslora o las
    coordenadas a una función.
-   **Listas**: almacenan las longitudes de los barcos y las
    coordenadas.
-   **Tuplas**: representan una coordenada `(fila, columna)`.
-   **Bucles `while` y `for`**: repiten intentos de colocación y
    recorren las partes de los barcos.
-   **Condicionales `if`, `elif` y `else`**: deciden qué hacer según la
    orientación, los límites y el resultado del disparo.
-   **`random`**: elige coordenadas y orientaciones al azar.
-   **NumPy**: representa el tablero como una matriz de datos.
-   **Importaciones**: permiten reutilizar funciones de
    `hundir_la_flota_funciones.py` desde el archivo principal.

## Aspectos que conviene revisar

Este README describe el código tal como está escrito. Antes de
considerar el juego terminado, conviene revisar algunos detalles:

1.  **Entrada del tamaño:** el mensaje dice que se puede pulsar Enter
    para usar tamaño 10, pero `int(input(...))` no contempla una entrada
    vacía. Hay que escribir un número.
2.  **Límites del disparo de la máquina:**
    `random.randint(0, tablero.shape[0])` puede generar un índice igual
    al tamaño del tablero, que queda fuera de rango. Para un tablero de
    tamaño `N`, los índices válidos son de `0` a `N - 1`.
3.  **Condición del bucle:**
    `while quedan_barcos(tableroJug) or quedan_barcos(tablero_enemigo)`
    mantiene la partida mientras quede algún barco en cualquiera de los
    dos tableros. Esto significa que no termina hasta que ambos se
    queden sin barcos.
4.  **Disparos repetidos:** un disparo a una casilla `X` no cambia el
    tablero, pero el programa principal no impide que se vuelva a
    introducir esa coordenada. Los disparos al agua tampoco se registran
    con una marca distinta de `_`.
5.  **Intentos de colocación:** `num_intentos` está definido en
    `crea_barco_aleatorio()`, pero no se usa; el bucle puede seguir
    intentando colocar el barco indefinidamente si no encuentra una
    posición válida.
6.  **Fin de partida:** el programa actual no muestra un mensaje de
    victoria o derrota; solo sigue mostrando el tablero del jugador.

Estos puntos son mejoras pendientes, no funcionalidades que ya estén
implementadas.
