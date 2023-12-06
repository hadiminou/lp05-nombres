from matplotlib import pyplot as plt
from collections import namedtuple
import csv
FrecuenciaNombre = namedtuple('FrecuenciaNombre', 'ano,nombre,frecuencia,genero')

def leer_frecuencias_nombres(ruta:str)->list[FrecuenciaNombre]:
    res = []
    with open (ruta,encoding='utf-8') as f:
        lector = csv.reader(f)
        next(lector)
#        for ano,nombre,frecuencia,genero in lector:
#            res.append(FrecuenciaNombre(int(ano),nombre,int(frecuencia),genero))
        res = [FrecuenciaNombre(int(ano),nombre,int(frecuencia),genero)\
            for ano,nombre,frecuencia,genero in lector]
    return res

def filtrar_por_genero(lista_personas:list[FrecuenciaNombre], gen:str)->list[FrecuenciaNombre]:
    res = []
#    for elemento in lista_personas:
#        if gen == elemento.genero:
#            res.append(elemento)
    res = [elemento for elemento in lista_personas if gen == elemento.genero]
    return res

def calcular_nombres(lista_personas:list[FrecuenciaNombre], gen:str=None)->set[str]:
    res = set()
#    for elemento in lista_personas:
#        if gen == elemento.genero or gen == None:
#            res.add(elemento.nombre)
    res = {elemento.nombre for elemento in lista_personas if gen == elemento.genero or gen == None}
    return (res)

def calcualar_top_nombres_de_ano(lista_personas:list[FrecuenciaNombre],\
                                  numero_ano:int, numero_limite:int=10, gen:str=None)->list[tuple[str, int]]:
    res = []
#    for elemento in lista_personas:
#        if (gen == elemento.genero or gen == None) and numero_ano == elemento.ano:
#            res.append((elemento.nombre,elemento.frecuencia))
    res = [(elemento.nombre, elemento.frecuencia) for elemento in lista_personas\
            if (gen == elemento.genero or gen == None)and numero_ano == elemento.ano]
    res = sorted(res, key = lambda e:e[1], reverse=True)
    return res[:numero_limite]
    
def calcular_nombres_ambos_generos(lista_personas:list[FrecuenciaNombre])->set[str]:
    # res = set()
    # lista_Hombres = set()
    # for elemento in lista_personas:
    #     if elemento.genero == "Hombre":
    #         lista_Hombres.add(elemento.nombre)
    #     if elemento.genero == "Mujer" and elemento.nombre in lista_Hombres:
    #         res.add(elemento.nombre)
    nom_hombres = calcular_nombres(lista_personas, "Hombre")
    nom_mujeres = calcular_nombres(lista_personas, "Mujer")
    return nom_hombres.intersection(nom_mujeres) #nom_hombres&nom_mujeres

def calcular_nombres_compuestos(lista_personas:list[FrecuenciaNombre], gen:str=None)->set[str]:
    res = set()
    # res = {elemento.nombre for elemento in lista_personas if gen == elemento.genero and " " in elemento.nombre}
    # return sorted(res)
    for i in lista_personas:
        if (gen == None or i.genero.upper() == gen.upper()) \
        and len(i.nombre.strip().split()) > 1: #and " " in i.nombre.strip():
            res.add(i.nombre)
    return res

def calcular_frecuencia_media_nombre_anos(lista_personas:list[FrecuenciaNombre], nom:str,\
                                           anoi:int , anof:int)->float:
    res = 0
    contador = anof - anoi
    for i in lista_personas:
        if anoi <= i.ano and i.ano < anof and i.nombre.upper() == nom.upper():
            res+=i.frecuencia
    if contador > 0 :
        res = res/contador
    return res
            
def calcular_nombre_mas_frecuente_ano_genero(lista_personas:list[FrecuenciaNombre], ano:int, gen:str)->str:
    nombre_del_genero = calcular_nombre_mas_frecuente_por_ano(lista_personas, gen)
    for ano_aux, nombre, frecuencia in nombre_del_genero:
        if ano == ano_aux:
            res = nombre
            break
    lista = []
    for f in lista_personas:
        if f.genero == gen and f.ano == ano:
            lista.append((f))
    maximo_lista = max(lista, key = lambda f:f.frecuencia)
    return maximo_lista.nombre

def calcular_ano_mas_frecuencia_nombre(lista_personas:list[FrecuenciaNombre], nom:str)->int:
    res = calcular_frecuencia_por_ano(lista_personas, nom)
    a = max(res, key = lambda e:e[1])
    return a[0]

def calcular_nombres_mas_frecuentes(lista_personas:list[FrecuenciaNombre], gen:str, decada:int, \
                                    num_nombres:int=5)->list[str]:
    aux = calcular_nombre_mas_frecuente_por_ano(lista_personas, gen)
    dict_aux = dict()
    res = []
    nombres_resultados = []
    for ano_aux, nombre, frecuencia in aux:
        if ano_aux >= decada and ano_aux < (decada+10):
            if nombre not in dict_aux:
                dict_aux[nombre] = frecuencia 
            elif frecuencia > dict_aux[nombre] and nombre in dict_aux:
                dict_aux[nombre] += frecuencia 
    for clave, valor in sorted(dict_aux.items(), key = lambda e:e[1], reverse = True):
        res.append(clave)
    #for i in res[:num_nombres]:
    #    nombres_resultados.append(i)
    return res[:num_nombres]

def calcular_ano_frecuencia_por_nombre(lista_personas:list[FrecuenciaNombre], \
                                       gen:str)->dict[str, list[tuple[int, int]]]:
    res = dict()
    for i in lista_personas:
        if gen == i.genero:
            if i.nombre not in res:
                res[i.nombre] = []
            res[i.nombre].append((i.ano, i.frecuencia))
    return res

def calcular_nombre_mas_frecuente_por_ano(lista_personas:list[FrecuenciaNombre],\
                                           gen:str=None)->list[tuple[int, str, int]]:
    res = []
    dict_aux = agrupar_frecuencias_por_ano(lista_personas, gen)
    for ano in dict_aux:
        tupla = max(dict_aux[ano], key = lambda e:e[1])
        res.append((ano, tupla[0], tupla[1]))
    res.sort(key = lambda e:e[0])
    return res

#funcion auxiliar
def agrupar_frecuencias_por_ano(lista_personas:list[FrecuenciaNombre], gen:str=None)->\
                                    dict[int, list[FrecuenciaNombre]]:
    dict_aux = dict()
    for i in lista_personas:
        if gen == None or gen == i.genero:
            if i.ano not in dict_aux:
                dict_aux[i.ano] = []
            dict_aux[i.ano].append((i.nombre, i.frecuencia))
    return dict_aux

def calcular_frecuencia_por_ano(lista_personas:list[FrecuenciaNombre], nom:str)->list[int, int]:
    res = []
    dict_aux = dict()
    for i in lista_personas:
        if i.nombre.upper() == nom.upper():
            if i.ano not in dict_aux:
                dict_aux[i.ano] = 0
            dict_aux[i.ano] += i.frecuencia
    for clave, frecuencia_acum in dict_aux.items():
        res.append((clave, frecuencia_acum))
    return res
    # for elemento in lista_personas:
    #     if nom == elemento.nombre:
    #         res.append((elemento.ano, elemento.frecuencia))
    #res = [(elemento.ano, elemento.frecuencia) for elemento in lista_personas if nom == elemento.nombre]
    #return sorted(res, key = lambda e:e[0])

def mostrar_evolucion_por_ano(lista_personas:list[FrecuenciaNombre], nom:str)->None:
    anos=[]
    frecuencias=[]
    for ano, frecuencia in calcular_frecuencia_por_ano(lista_personas, nom):
            anos.append(ano)
            frecuencias.append(frecuencia)
    plt.plot(anos, frecuencias)
    plt.title("Evolución del nombre '{}'".format(nom))
    plt.show()

def calcular_frecuencia_acumulada(lista_personas:list[FrecuenciaNombre], nom:str)->int:
    res = 0
    for elemento in lista_personas:
        if nom.upper() == elemento.nombre.upper():
            res += elemento.frecuencia
    return res

def calcular_frecuencias_por_nombre(lista_personas:list[FrecuenciaNombre])->dict:
    res = dict()
    for elemento in lista_personas:
        if elemento.nombre not in res:
            res[elemento.nombre] = calcular_frecuencia_acumulada(lista_personas, elemento.nombre)
    return res

def mostrar_frecuencias_nombres(lista_personas:list[FrecuenciaNombre], numero_limite:int=10)->None:
    nombres=[]
    frecuencias=[]
    res = sorted(calcular_frecuencias_por_nombre(lista_personas).items(),\
                  key = lambda item:item[1], reverse = True)[:numero_limite]
    for nombre, frecuencia in res:
        nombres.append(nombre)
        frecuencias.append(frecuencia)
    plt.bar(nombres, frecuencias)
    plt.xticks(rotation=80)
    plt.title("Frecuencia de los {} nombres más comunes".format(numero_limite))
    plt.show()