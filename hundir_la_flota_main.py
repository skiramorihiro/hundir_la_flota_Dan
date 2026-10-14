import numpy as np
import random
import hundir_la_flota_funciones as hf

def jugar():
    print("============================================")
    print("==============Hundir La Flota===============")
    print("============================================")

    tamano_tablero = int(input("Tamaño de tu tablero (enter para tamaño 10):"))
    
    tableroJug = hf.crear_tablero(tamano_tablero)

    barcos = [2,2,2,3,3,4]

    for eslora in barcos:
      tableroJug = hf.crea_barco_aleatorio(tableroJug,eslora)


    print("============================================")
    print(tableroJug)
    print("============================================")

    tablero_enemigo = hf.crear_tablero(tamano_tablero)
    for eslora in barcos:
       tablero_enemigo = hf.crea_barco_aleatorio(tablero_enemigo,eslora)

    #print("============================================")
    #print(tablero_enemigo)
    #print("============================================")
    
    #en éste bucle se empieza a jugar, nosotros ponemos unas coordenadas que preguntas primero fila y luego columna y en funcion de si acierto o no sigo yo u el ordenador. 
    #A parte si sale tocado me devuelve un tablero con la coordenada marcada en "x"
        
    #el bucle funciona mientras sea True el valor, de quedan barcos, porque la funcion np.any mira si quedan barcos
    #cuando deje de haber barcos en alguno de los tableros "O" me devolverá mi tablero
    
    
    while hf.quedan_barcos(tableroJug) or hf.quedan_barcos(tablero_enemigo):
       
       #Turno de jugador
       fila = int(input("introducir numero de la fila"))
       columna = int(input("introducir numero de la columna"))
       tablero_enemigo = hf.recibir_disparo(tablero_enemigo,(fila,columna))

       #Turno de maquina
       fila = random.randint(0,tableroJug.shape[0])
       columna = random.randint(0,tableroJug.shape[1])
       tableroJug = hf.recibir_disparo(tableroJug,(fila,columna))

       print(tableroJug)



jugar()