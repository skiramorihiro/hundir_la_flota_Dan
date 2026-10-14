import numpy as np
import random

#Crea la función `crear_tablero(tamaño)`, un tablero por defecto de 10x10 relleno del carácter "_" con numpy.

def crear_tablero(size=10):
    tablero = np.full((size,size),"_")
    #print(tablero)
    return tablero

#def coloca_barco(tablero, barco):
#    for pieza in barco:
#        tablero[pieza] = "O"
#    return tablero

def crea_barco_aleatorio(tablero,eslora = 4, num_intentos = 100):
    num_max_filas = tablero.shape[0]
    num_max_columnas = tablero.shape[1]
    while True:   # mientras sea cierto lo de debajo
        barco = []    
        # Construimos el hipotetico barco
        pieza_original = (random.randint(0,num_max_filas-1),random.randint(0, num_max_columnas -1))
        print("Pieza original:", pieza_original)
        barco.append(pieza_original)
        orientacion = random.choice(["N","S","O","E"])
        print("Con orientacion", orientacion)
        fila = pieza_original[0]
        columna = pieza_original[1]   #
        for i in range(eslora -1):
            if orientacion == "N":
                fila -= 1
            elif orientacion  == "S":
                fila += 1
            elif orientacion == "E":
                columna += 1
            else:
                columna -= 1
            pieza = (fila,columna)
            barco.append(pieza)
        tablero_temp = coloca_barco_plus(tablero, barco)   
        if type(tablero_temp) == np.ndarray:
            return tablero_temp  # te devuelve el tablero con el barco colocado
        print("Tengo que intentar colocar otro barco")

def coloca_barco_plus(tablero, barco):
    # Nos devuelve el tablero si puede colocar el barco, si no devuelve False, y avise por pantalla
    tablero_temp = tablero.copy()
    num_max_filas = tablero.shape[0] #accede a filas que es 10 porque el indice 0 corresponde a filas, y el 1  a columnas
    num_max_columnas = tablero.shape[1]#indica el numero maximo de columnas que hay en el tablero
    for pieza in barco:    #barco es una lista de tuplas  # barco = [(2,3), (2,4), (2,5), (2,6)]
        fila = pieza[0]
        columna = pieza[1]
        if fila < 0  or fila >= num_max_filas:
            print(f"No puedo poner la pieza {pieza} porque se sale del tablero")
            return False
        if columna <0 or columna>= num_max_columnas:
            print(f"No puedo poner la pieza {pieza} porque se sale del tablero")
            return False
        if tablero[pieza] == "O" or tablero[pieza] == "X":
            print(f"No puedo poner la pieza {pieza} porque hay otro barco")
            return False
        tablero_temp[pieza] = "O"
    return tablero_temp

def recibir_disparo(tablero, coordenada):
    if tablero[coordenada] == "O":
        tablero[coordenada] = "X"
        print("Tocado")
    elif tablero[coordenada] == "X":
        print("dispara a otro sitio")
    else:
        tablero[coordenada] = "_"
        print("Agua")

    return tablero


#mira si quedan barcos en el tablero
def quedan_barcos(tablero):
    """Devuelve True si todavía quedan partes de barcos sin tocar."""
    return np.any(tablero == "O")


#def colocar_barco(barco, tablero)