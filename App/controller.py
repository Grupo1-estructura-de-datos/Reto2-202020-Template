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

import config as cf
from App import model as m
import csv
from DISClib.ADT import list as lt
from DISClib.DataStructures import listiterator as it
from DISClib.ADT import map as mp
from DISClib.DataStructures import mapentry 
import bisect
import copy

"""
El controlador se encarga de mediar entre la vista y el modelo.
Existen algunas operaciones en las que se necesita invocar
el modelo varias veces o integrar varias de las respuestas
del modelo en una sola respuesta. Esta responsabilidad
recae sobre el controlador.
"""

# ___________________________________________________
#  Inicializacion del catalogo
# ___________________________________________________
def f1(productora):
    if ndatos>1:
        LlavesCriteriosAdicionales = ["Número de peliculas: ","Promedio de peliculas: "]
        tupla=m.efe12(productora,DirectorioMapa["PsXComDePro"],LlavesCriteriosAdicionales)
        return tupla
    else: print("No se pudo hacer la operación, asegurese de cargar los datos primero")

def f2(director):
    if ndatos>1:
        LlavesCriteriosAdicionales = ["Número de peliculas: ","Promedio de peliculas: "]
        tupla=m.efe12(director,DirectorioMapa["PsXNomDeDir"],LlavesCriteriosAdicionales)
        return tupla
    else: print("No se pudo hacer la operación, asegurese de cargar los datos primero")

def f3(actor):
    if ndatos>1:
        LlavesCriteriosAdicionales = ["Número de peliculas: ","Promedio de peliculas: ", "Director con más colaboraciones: "]
        tupla=m.efe3(actor,DirectorioMapa['PsXNomDeAct'],LlavesCriteriosAdicionales)
        return tupla
    else: print("No se pudo hacer la operación, asegurese de cargar los datos primero")

def f4(genero):
    if ndatos>1:
        LlavesCriteriosAdicionales = ["Número de peliculas: ","Promedio de peliculas: "]
        tupla=m.efe12(genero,DirectorioMapa["PsXGenCinem"],LlavesCriteriosAdicionales)
        return tupla
    else: print("No se pudo hacer la operación, asegurese de cargar los datos primero")

def f5(país):
    if ndatos>1:
        tupla=m.efe5(país,DirectorioMapa["PsXPais____"])
        return tupla
    else: print("No se pudo hacer la operación, asegurese de cargar los datos primero")

# ___________________________________________________
#  Funciones para la carga de datos y almacenamiento
#  de datos en los modelos
# ___________________________________________________


Lprimos=[17,47,101,347,743,919,1009,2011,4001,8101,10453,20051,40009,80021,160507,350983,642211,10000019,1299499] #algunos primos para elegir el tamaño del map
ndatos = 0
CriterioLlaves = ["production_companies","director_name","ACTORES","genres","production_countries"]
PsXComDePro = {}
DirectorioMapa = {}

def fs():
    global ndatos
    global DirectorioMapa
    CASTING=m.loadMovies("casting")
    ndatos=CASTING[1]
    lstmoviescasting = CASTING[0]
    lstmoviesdetails = m.loadMovies("details",True)[0]
    Directorio_TAD_Lista = m.CrearDirectorioLista(lstmoviescasting,lstmoviesdetails)
    primo=Lprimos[bisect.bisect_right(Lprimos, ndatos)]
    parametros=[primo,100999001,'CHAINING',2]
    DirectorioMapa = m.CrearDirectorioMapa(parametros,CriterioLlaves,Directorio_TAD_Lista)
