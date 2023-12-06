from  nombres import*

def test_leer_frecuencias_nombres(datos_fichero):
    print("test leer frecuencias nombres")
    print(f"\n{len(datos_fichero)} registros leidos")
    print("\nmostrando los 3 primeros:", datos_fichero[:3])
    print("\nmostrando los 3 ultimos:", datos_fichero[-3:])

def test_filtrar_por_genero(datos_fichero):
    print("\n###test filtrar por genero###")
    res1=filtrar_por_genero(datos_fichero, "Mujer")
    res2=filtrar_por_genero(datos_fichero, "Hombre")
    print(f"\nNumero de registros para mujer: {len(res1)}")
    print(f"\nNumero de registros para hombre: {len(res2)}")
    #print(filtrar_por_genero(datos_fichero, "Mujer"))
    #print(filtrar_por_genero(datos_fichero, "Hombre"))

def test_calcular_nombres(datos_fichero):
    print("\n###test calcular nombres###")
    print(calcular_nombres(datos_fichero, None))
    print("\nMujeres son:",calcular_nombres(datos_fichero, "Mujer"))
    print("\nHombres son:",calcular_nombres(datos_fichero, "Hombre"))

def test_calcualar_top_nombres_de_ano(datos_fichero):
    print("\n###test calcular top nombres de ano###")
    numero_ano = 2008
    numero_limite = 11
    print(f"\n{numero_limite} Mujeres primeros de ano {numero_ano} son:",calcualar_top_nombres_de_ano(datos_fichero, numero_ano, numero_limite, "Mujer"))
    print(f"\n{numero_limite} Hombres primeros de ano {numero_ano} son:",calcualar_top_nombres_de_ano(datos_fichero, numero_ano, numero_limite, "Hombre"))

def test_calcular_nombres_ambos_generos(datos_fichero):
    print("\n###test calcular nombres ambos generos###")
    print(calcular_nombres_ambos_generos(datos_fichero))

def test_calcular_nombres_compuestos(datos_fichero):
    print("\n###test calcular nombres compuestos###")
    print("\nMujer:",calcular_nombres_compuestos(datos_fichero, "Mujer"))
    print("\nHombre:",calcular_nombres_compuestos(datos_fichero, "Hombre"))

def test_calcular_nombre_mas_frecuente_por_ano(datos_fichero):
    print("\n###test calcular nombre mas frecuente por ano###")
    print("\nMujer:",calcular_nombre_mas_frecuente_por_ano(datos_fichero, "Mujer"))
    print("\nHombre:",calcular_nombre_mas_frecuente_por_ano(datos_fichero, "Hombre"))

def test_calcular_frecuencia_por_ano(datos_fichero):
    print("\n###test calcular frecuencia por ano###")
    nom="IKER"
    print(f"{nom}:",calcular_frecuencia_por_ano(datos_fichero, nom))

def test_mostrar_evolucion_por_ano(datos_fichero):
    print("\n###test mostrar evolucion por ano###")
    print(mostrar_evolucion_por_ano(datos_fichero, "PABLO"))

def test_calcular_frecuencia_acumulada(datos_fichero):
    print("\n###test calcular frecuencia acumulada###")
    nom="IKER"
    print(f"{nom}:",calcular_frecuencia_acumulada(datos_fichero, nom))

def test_calcular_frecuencias_por_nombre(datos_fichero):
    print("\n###test calcular frecuencias por nombre###")
    print(calcular_frecuencias_por_nombre(datos_fichero))

def test_mostrar_frecuencias_nombres(datos_fichero):
    print("\n###test mostrar frecuencias nombres###")
    print(mostrar_frecuencias_nombres(datos_fichero, 11))

def test_calcular_frecuencia_media_nombre_anos(datos_fichero):
    print("\ntest_calcular_frecuencia_media_nombre_anos")
    nombre = "NEREA"
    ano1 = 2005
    ano2 = 2010
    res = calcular_frecuencia_media_nombre_anos(datos_fichero, nombre, ano1, ano2)
    print(f"La frecuencia media del nombre NEREA entre {ano1} y {ano2} es: {res}")

def test_calcular_nombre_mas_frecuente_ano_genero(datos_fichero):
    print("\ntest_calcular_nombre_mas_frecuente_ano_genero")
    ano = 2017
    genero = "Mujer"
    res = calcular_nombre_mas_frecuente_ano_genero(datos_fichero, ano, genero)
    print(f"El nombre más frecuente del año {ano} y género {genero} es {res}")

def test_calcular_ano_mas_frecuencia_nombre(datos_fichero):
    print("test_calcular_ano_mas_frecuencia_nombre")
    nombre = "VERA"
    res = calcular_ano_mas_frecuencia_nombre(datos_fichero, nombre)
    print(f"El año con mayor frecuencia del nombre {nombre} es {res}")

def test_calcular_ano_frecuencia_por_nombre(datos_fichero):
    print("test_calcular_ano_frecuencia_por_nombre")
    genero = "Mujer"
    print(f"Frecuencias de nombres de género {genero} son: \
          {calcular_ano_frecuencia_por_nombre(datos_fichero, genero)}")
    
def test_calcular_nombres_mas_frecuentes(datos_fichero):
    print("test_calcular_nombres_mas_frecuentes")
    genero = "Hombre"
    decada = 2010
    numero = 5
    print(f"Los {numero} nombres más frecuentes del género {genero} y década {decada} son: \
          {calcular_nombres_mas_frecuentes(datos_fichero, genero, decada, numero)}")

if __name__=="__main__":
    datos=leer_frecuencias_nombres("Proyectos Python\WSPython\git\lp05-nombres-hadiminou-main\data/frecuencias_nombres.csv")
    #test_leer_frecuencias_nombres(datos)
    #test_filtrar_por_genero(datos)
    #test_calcular_nombres(datos)
    #test_calcualar_top_nombres_de_ano(datos)
    #test_calcular_nombres_ambos_generos(datos)
    #test_calcular_nombres_compuestos(datos)
    #test_calcular_nombre_mas_frecuente_por_ano(datos)
    #test_calcular_frecuencia_por_ano(datos)
    #test_mostrar_evolucion_por_ano(datos)
    #test_calcular_frecuencia_acumulada(datos)
    #test_calcular_frecuencias_por_nombre(datos)
    #test_mostrar_frecuencias_nombres(datos)
    #test_calcular_frecuencia_media_nombre_anos(datos)
    #test_calcular_nombre_mas_frecuente_ano_genero(datos)
    #test_calcular_ano_mas_frecuencia_nombre(datos)
    #test_calcular_ano_frecuencia_por_nombre(datos)
    test_calcular_nombres_mas_frecuentes(datos)