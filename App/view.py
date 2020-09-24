"""
 * Copyright 2020, Departamento de sistemas y Computación
 * Universidad de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program.  If not, see <http://www.gnu.org/licenses/>.
 """

import sys
import config
from DISClib.ADT import list as lt
from DISClib.DataStructures import listiterator as it
assert config
from DISClib.ADT import queue as qe 


"""
La vista se encarga de la interacción con el usuario.
Presenta el menu de opciones y por cada seleccion
hace la solicitud al controlador para ejecutar la
operación seleccionada.
"""

# ___________________________________________________
#  Ruta a los archivos
# ___________________________________________________

from App import controller as c

# ___________________________________________________
#  Funciones para imprimir la inforamación de
#  respuesta.  La vista solo interactua con
#  el controlador.
# ___________________________________________________

def ImprimirEnConsola(cola, DatosAdicionales=None):
    if qe.isEmpty(cola)==False: 
        Centinela = True
        print("-"*100)
        while Centinela==True:
            print("", end=" "*10)
            print("•" + qe.dequeue(cola))
            if qe.isEmpty(cola)==True: Centinela=False
        print("-"*100)
    else: print("No se encontrar peliculas para el criterio")
    if DatosAdicionales!=None:
        if qe.isEmpty(DatosAdicionales)==False:
            CentinelaAdicionales = True
            while CentinelaAdicionales==True:
                dato = qe.dequeue(DatosAdicionales)
                print(str(dato[0])+str(dato[1]))
                if qe.isEmpty(DatosAdicionales)==True: CentinelaAdicionales=False

# ___________________________________________________
#  Menu principal
# ___________________________________________________

def printMenu():
    """
    Imprime el menu de opciones
    """
    print("\nBienvenido")
    print("1- Descubrir productoras de cine")
    print("2- Conocer a un director")
    print("3- Conocer a un actor")
    print("4- Entender un género cinematográfico")
    print("5- Encontrar películas por país")
    print("0- Salir")

c.fs()
print("\n"*2)

while True:
    try:
        printMenu()
        n = int(input())
        if n==0: break
        if n==1: 
            print("\n"*2+"="*100)
            productora=input("Por favor ingrese el nombre de la compañía de producción: ")
            tupla = c.f1(productora)
            print("\n" + "A continuacion información de la productora de cine")
            print("\n" + "Peliculas de la productora: ")
            ImprimirEnConsola(tupla[0],tupla[1])
        if n==2: 
            print("\n"*2+"="*100)
            director=input("Por favor ingrese el nombre del director: ")
            tupla = c.f2(director)
            print("\n" + "A continuacion información del trabajo del director")
            print("\n" + "Peliculas del director: ")
            ImprimirEnConsola(tupla[0],tupla[1])
        if n==3:
            print("\n"*2+"="*100)
            actor=input("Por favor ingrese el nombre del actor: ")
            tupla = c.f3(actor)
            print("\n" + "A continuacion información del trabajo del actor")
            print("\n" + "Peliculas del actor: ")         
            ImprimirEnConsola(tupla[0],tupla[1])
        if n==4: 
            print("\n"*2+"="*100)
            genero=input("Por favor ingrese el nombre del género: ")
            tupla = c.f4(genero)
            print("\n" + "A continuacion información del género ")
            print("\n" + "Peliculas del género: ")         
            ImprimirEnConsola(tupla[0],tupla[1])
        if n==5:
            print("\n"*2+"="*100)
            país=input("Por favor ingrese el nombre del país: ")
            tupla = c.f5(país)
            print("\n" + "A continuacion información de las peliculas del país, con su respectivo director")
            print("\n" + "Peliculas del director: ")
            ImprimirEnConsola(tupla[0],tupla[1])
    except: print("Hubo un error")
