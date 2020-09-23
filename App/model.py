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
import config
from DISClib.ADT import queue as qe 
from DISClib.ADT import map as mp
from DISClib.DataStructures import mapentry 
assert config
import sys
import csv
import copy
from scipy import stats as statistics
from DISClib.ADT import list as lt
from DISClib.DataStructures import listiterator as it
import copy

"""
En este archivo definimos los TADs que vamos a usar,
es decir contiene los modelos con los datos en memoria

"""

# -----------------------------------------------------
# API del TAD Catalogo de Libros
# -----------------------------------------------------

def CrearDirectorioLista(lstmoviescasting,lstmoviesdetails):
    DirectorioLista = lt.newList()
    IteradorCasting = it.newIterator(lstmoviescasting)
    IteradorDetails = it.newIterator(lstmoviesdetails)
    while it.hasNext(IteradorCasting)==True:
        PeliculaCasting=it.next(IteradorCasting)
        PeliculaDetails=it.next(IteradorDetails)
        del PeliculaDetails["id"]
        PeliculaCasting.update(PeliculaDetails)
        NuevaPelicula = PeliculaCasting
        lt.addLast(DirectorioLista,NuevaPelicula)
    return DirectorioLista

def CrearDirectorioMapa(parametros,CriterioLlaves,Directorio_TAD_Lista):
    DirectorioMapa = {'PsXComDePro': mp.newMap(parametros[0]*1,parametros[1],parametros[2],parametros[3],CompararCriterios), 
                      'PsXNomDeDir': mp.newMap(parametros[0]*1,parametros[1],parametros[2],parametros[3],CompararCriterios),
                      'PsXNomDeAct': mp.newMap(parametros[0]*5,parametros[1],parametros[2],parametros[3],CompararCriterios),
                      'PsXGenCinem': mp.newMap(parametros[0]*2,parametros[1],parametros[2],parametros[3],CompararCriterios),
                      'PsXPais____': mp.newMap(parametros[0]*1,parametros[1],parametros[2],parametros[3],CompararCriterios)}
    DirectorioLlavesDirectorioMapa = {'PsXComDePro': mp.newMap(2011,100999001,'CHAINING',2,CompararCriterios ), #aprox 2011 productoras
                                      'PsXNomDeDir': mp.newMap(10007,100999001,'CHAINING',2,CompararCriterios), #aprox 10007 directores
                                      'PsXNomDeAct': mp.newMap(32233,100999001,'CHAINING',2,CompararCriterios), #aprox 32233 actores
                                      'PsXGenCinem': mp.newMap(101,100999001,'CHAINING',2,CompararCriterios  ), #aprox 101 generos
                                      'PsXPais____': mp.newMap(239,100999001,'CHAINING',2,CompararCriterios  )} #aprox 239 paises
    iterable=it.newIterator(Directorio_TAD_Lista)
    ####################################################################################################################################
    k=0######## se puede quitar
    while it.hasNext(iterable):
        pelicula=it.next(iterable)
        #PsXComDePro
        if not mp.contains(DirectorioLlavesDirectorioMapa['PsXComDePro'],pelicula[CriterioLlaves[0]]):
            mp.put(DirectorioMapa['PsXComDePro'],pelicula[CriterioLlaves[0]]+"0" ,pelicula)
            mp.put(DirectorioLlavesDirectorioMapa['PsXComDePro'],pelicula[CriterioLlaves[0]],0)
        else: 
            ValorNuevo = mp.get(DirectorioLlavesDirectorioMapa['PsXComDePro'],pelicula[CriterioLlaves[0]])['value'] + 1
            mp.put(DirectorioLlavesDirectorioMapa['PsXComDePro'],pelicula[CriterioLlaves[0]],ValorNuevo)
            mp.put(DirectorioMapa['PsXComDePro'],pelicula[CriterioLlaves[0]]+str(ValorNuevo),pelicula)
        #PsXNomDeDir
        if not mp.contains(DirectorioLlavesDirectorioMapa['PsXNomDeDir'],pelicula[CriterioLlaves[1]]):
            mp.put(DirectorioMapa['PsXNomDeDir'],pelicula[CriterioLlaves[1]]+"0" ,pelicula)
            mp.put(DirectorioLlavesDirectorioMapa['PsXNomDeDir'],pelicula[CriterioLlaves[1]],0)
        else: 
            ValorNuevo = mp.get(DirectorioLlavesDirectorioMapa['PsXNomDeDir'],pelicula[CriterioLlaves[1]])['value'] + 1
            mp.put(DirectorioLlavesDirectorioMapa['PsXNomDeDir'],pelicula[CriterioLlaves[1]],ValorNuevo)
            mp.put(DirectorioMapa['PsXNomDeDir'],pelicula[CriterioLlaves[1]]+str(ValorNuevo),pelicula)
        CriterioLlavesInceptionActores = ["actor1_name","actor2_name","actor3_name","actor4_name","actor5_name"]
        for i in CriterioLlavesInceptionActores:
            if not mp.contains(DirectorioLlavesDirectorioMapa['PsXNomDeAct'],pelicula[i]):
                mp.put(DirectorioMapa['PsXNomDeAct'],pelicula[i]+"0" ,pelicula)
                mp.put(DirectorioLlavesDirectorioMapa['PsXNomDeAct'],pelicula[i],0)
            else: 
                ValorNuevo = mp.get(DirectorioLlavesDirectorioMapa['PsXNomDeAct'],pelicula[i])['value'] + 1
                mp.put(DirectorioLlavesDirectorioMapa['PsXNomDeAct'],pelicula[i],ValorNuevo)
                mp.put(DirectorioMapa['PsXNomDeAct'],pelicula[i]+str(ValorNuevo),pelicula)
        #PsXGenCinem
        CriterioLlavesInceptionGeneros = pelicula[CriterioLlaves[3]].split("|")
        for i in CriterioLlavesInceptionGeneros:
            if not mp.contains(DirectorioLlavesDirectorioMapa['PsXGenCinem'],i):
                mp.put(DirectorioMapa['PsXGenCinem'],i+"0" ,pelicula)
                mp.put(DirectorioLlavesDirectorioMapa['PsXGenCinem'],i,0)
            else: 
                ValorNuevo = mp.get(DirectorioLlavesDirectorioMapa['PsXGenCinem'],i)['value'] + 1
                mp.put(DirectorioLlavesDirectorioMapa['PsXGenCinem'],i,ValorNuevo)
                mp.put(DirectorioMapa['PsXGenCinem'],i+str(ValorNuevo),pelicula)
        #PsXPais____
        if not mp.contains(DirectorioLlavesDirectorioMapa['PsXPais____'],pelicula[CriterioLlaves[4]]):
            mp.put(DirectorioMapa['PsXPais____'],pelicula[CriterioLlaves[4]]+"0" ,pelicula)
            mp.put(DirectorioLlavesDirectorioMapa['PsXPais____'],pelicula[CriterioLlaves[4]],0)
        else: 
            ValorNuevo = mp.get(DirectorioLlavesDirectorioMapa['PsXPais____'],pelicula[CriterioLlaves[4]])['value'] + 1
            mp.put(DirectorioLlavesDirectorioMapa['PsXPais____'],pelicula[CriterioLlaves[4]],ValorNuevo)
            mp.put(DirectorioMapa['PsXPais____'],pelicula[CriterioLlaves[4]]+str(ValorNuevo),pelicula)
        if k%10000==0 and k!=0: print(k)##### se puede quitar
        k+=1##### se puede quitar
    return DirectorioMapa

# ==============================================
# Funciones para agregar informacion al catalogo
# ==============================================

def loadCSVFile (file, cmpfunction):
    lst=lt.newList("ARRAY_LIST", cmpfunction)
    dialect = csv.excel()
    dialect.delimiter=";"
    try:
        with open(  config.data_dir + file, encoding="utf-8-sig") as csvfile:
            row = csv.DictReader(csvfile, dialect=dialect)
            for elemento in row: 
                lt.addLast(lst,elemento)
    except:
        print("Hubo un error con la carga del archivo")
    return lst

def loadMovies (indicador,MUTE=False):
    if indicador=="details":
        lst = loadCSVFile("themoviesdb/SmallMoviesDetailsCleaned.csv",compareRecordIds)
    elif indicador=="casting": 
        lst = loadCSVFile("themoviesdb/MoviesCastingRaw-small.csv",compareRecordIds)
    if MUTE==False:
        print("Datos cargados, " + str(lt.size(lst)) + " elementos cargados")
    return [lst,lt.size(lst)]

# ==============================
# Funciones de consulta
# ==============================
def efe12(productora,PsXComDePro,LlavesCriteriosAdicionales):
    n = 0
    ColaPeliculas = qe.newQueue()
    ColaAdicionales = qe.newQueue()
    Puntajes = []
    Centinela=True
    while Centinela==True:
        if mp.contains(PsXComDePro,productora+str(n)):
            pelicula = mp.get(PsXComDePro,productora+str(n))["value"]
            qe.enqueue(ColaPeliculas,pelicula["title"]+ " (" +pelicula["release_date"][-4:] + ")")
            Puntajes.append(float(pelicula["vote_average"]))
            n=n+1
        else: 
            Centinela = False
    if len(Puntajes)!=0:
        qe.enqueue(ColaAdicionales,[LlavesCriteriosAdicionales[0],qe.size(ColaPeliculas)])
        qe.enqueue(ColaAdicionales,[LlavesCriteriosAdicionales[1],sum(Puntajes)/len(Puntajes)])
        return (ColaPeliculas   , ColaAdicionales)
    else: 
        qe.enqueue(ColaAdicionales,qe.size(ColaPeliculas))
        qe.enqueue(ColaAdicionales,0)
        return (ColaPeliculas   , ColaAdicionales)

def efe5(país,PsXPais____):
    n = 0
    ColaPeliculas = qe.newQueue()
    Centinela=True
    while Centinela==True:
        if mp.contains(PsXPais____,país+str(n)):
            pelicula = mp.get(PsXPais____,país+str(n))["value"]
            qe.enqueue(ColaPeliculas,pelicula["title"]+ " (" +pelicula["release_date"][-4:] + ") " + "Dirigida por: " + pelicula["director_name"])
            n=n+1
        else: 
            Centinela = False
    return (ColaPeliculas   , None)

# ==============================
# Funciones de Comparacion
# ==============================

def compareRecordIds (recordA, recordB):
    if int(recordA['id']) == int(recordB['id']):
        return 0
    elif int(recordA['id']) > int(recordB['id']):
        return 1
    return -1

def CompararCriterios(keyname, criterio):
    authentry = mapentry.getKey(criterio)
    if (keyname == authentry):
        return 0
    elif (keyname > authentry):
        return 1
    else:
        return -1