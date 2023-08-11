# Parte 1: Cargar los datos
def cargar_datos(lineas_archivo):
    # Completar
    generos_peliculas = []
    peliculas_por_genero = []
    info_peliculas = []

    for linea in lineas_archivo:
        datos_pelicula = linea.strip().split(",")
        titulo = datos_pelicula[0]
        popularidad = float(datos_pelicula[1]) 
        voto_promedio = float(datos_pelicula[2])
        cantidad_votos = int(datos_pelicula[3])
        generos = datos_pelicula[4].split(";")

        # Actualizar generos_peliculas
        for genero in generos:
            if genero not in generos_peliculas:
                generos_peliculas.append(genero)

        # Actualizar peliculas_por_genero
        for genero in generos:
            pelicula = titulo
            for elemento in peliculas_por_genero:
                if elemento[0] == genero:
                    elemento[1].append(pelicula)
                    break
            else:
                peliculas_por_genero.append((genero, [pelicula]))

        # Actualizar info_peliculas
        info_peliculas.append((titulo, popularidad, voto_promedio, cantidad_votos, generos))

    return generos_peliculas, peliculas_por_genero, info_peliculas
    pass


# Parte 2: Completar las consultas
def obtener_puntaje_y_votos(nombre_pelicula):

    
    # Completar con lo que falta aquí
    lineas_archivo = leer_archivo()
    for linea in lineas_archivo:
        datos_pelicula = linea.strip().split(",")
        if datos_pelicula[0] == nombre_pelicula:
            puntaje_promedio = float(datos_pelicula[2])
            cantidad_votos = int(datos_pelicula[3])
            return puntaje_promedio, cantidad_votos
    return None, None
    pass


def filtrar_y_ordenar(genero_pelicula):
    # Cargar las lineas con la data del archivo
    lineas_archivo = leer_archivo()
    # Completar con lo que falta aquí
    peliculas_filtradas = []
    for linea in lineas_archivo:
        datos_pelicula = linea.strip().split(",")
        titulo = datos_pelicula[0]
        generos = datos_pelicula[4].split(";")
        if genero_pelicula in generos:
            peliculas_filtradas.append(titulo)
    peliculas_filtradas.sort(reverse=True)
    return peliculas_filtradas
    pass


def obtener_estadisticas(genero_pelicula, criterio):
    # Cargar las lineas con la data del archivo
    lineas_archivo = leer_archivo()
    # Completar con lo que falta aquí
    valores_criterio = []
    for linea in lineas_archivo:
        datos_pelicula = linea.strip().split(",")
        generos = datos_pelicula[4].split(";")
        if genero_pelicula in generos:
            valor = None
            if criterio == "popularidad":
                valor = float(datos_pelicula[1])
            elif criterio == "voto promedio":
                valor = float(datos_pelicula[2])
            elif criterio == "cantidad votos":
                valor = int(datos_pelicula[3])
            if valor is not None:
                valores_criterio.append(valor)
    if valores_criterio:
        maximo = max(valores_criterio)
        minimo = min(valores_criterio)
        promedio = sum(valores_criterio) / len(valores_criterio)
        return maximo, minimo, promedio
    return None, None, None
    pass


# NO ES NECESARIO MODIFICAR DESDE AQUI HACIA ABAJO

def solicitar_accion():
    print("\n¿Qué desea hacer?\n")
    print("[0] Revisar estructuras de datos")
    print("[1] Obtener puntaje y votos de una película")
    print("[2] Filtrar y ordenar películas")
    print("[3] Obtener estadísticas de películas")
    print("[4] Salir")

    eleccion = input("\nIndique su elección (0, 1, 2, 3, 4): ")
    while eleccion not in "01234":
        eleccion = input("\nElección no válida.\nIndique su elección (0, 1, 2, 3, 4): ")
    eleccion = int(eleccion)
    return eleccion


def leer_archivo():
    lineas_peliculas = []
    with open("peliculas.csv", "r", encoding="utf-8") as datos:
        for linea in datos.readlines()[1:]:
            lineas_peliculas.append(linea.strip())
    return lineas_peliculas


def revisar_estructuras(generos_peliculas, peliculas_por_genero, info_peliculas):
    print("\nGéneros de películas:")
    for genero in generos_peliculas:
        print(f"    - {genero}")

    print("\nTítulos de películas por genero:")
    for genero in peliculas_por_genero:
        print(f"    genero: {genero[0]}")
        for titulo in genero[1]:
            print(f"        - {titulo}")

    print("\nInformación de cada película:")
    for pelicula in info_peliculas:
        print(f"    Nombre: {pelicula[0]}")
        print(f"        - Popularidad: {pelicula[1]}")
        print(f"        - Puntaje Promedio: {pelicula[2]}")
        print(f"        - Votos: {pelicula[3]}")
        print(f"        - Géneros: {pelicula[4]}")


def solicitar_nombre():
    nombre = input("\nIngrese el nombre de la película: ")
    return nombre


def solicitar_genero():
    genero = input("\nIndique el género de película: ")
    return genero


def solicitar_genero_y_criterio():
    genero = input("\nIndique el género de película: ")
    criterio = input(
        "\nIndique el criterio (popularidad, voto promedio, cantidad votos): "
    )
    return genero, criterio


def main():
    lineas_archivo = leer_archivo()
    datos_cargados = True
    try:
        generos_peliculas, peliculas_por_genero, info_peliculas = cargar_datos(
            lineas_archivo
        )
    except TypeError as error:
        if "cannot unpack non-iterable NoneType object" in repr(error):
            print(
                "\nTodavía no puedes ejecutar el programa ya que no has cargado los datos\n"
            )
            datos_cargados = False
    if datos_cargados:
        salir = False
        print("\n********** ¡Bienvenid@! **********")
        while not salir:
            accion = solicitar_accion()

            if accion == 0:
                revisar_estructuras(
                    generos_peliculas, peliculas_por_genero, info_peliculas
                )

            elif accion == 1:
                nombre_pelicula = solicitar_nombre()
                ptje, votos = obtener_puntaje_y_votos(nombre_pelicula)
                print(f"\nObteniendo puntaje promedio y votos de {nombre_pelicula}")
                print(f"    - Puntaje promedio: {ptje}")
                print(f"    - Votos: {votos}")

            elif accion == 2:
                genero = solicitar_genero()
                nombres_peliculas = filtrar_y_ordenar(genero)
                print(f"\nNombres de películas del género {genero} ordenados:")
                for nombre in nombres_peliculas:
                    print(f"    - {nombre}")

            elif accion == 3:
                genero, criterio = solicitar_genero_y_criterio()
                estadisticas = obtener_estadisticas(genero, criterio)
                print(f"\nEstadísticas de {criterio} de películas del género {genero}:")
                print(f"    - Máximo: {estadisticas[0]}")
                print(f"    - Mínimo: {estadisticas[1]}")
                print(f"    - Promedio: {estadisticas[2]}")

            else:
                salir = True
        print("\n********** ¡Adiós! **********\n")


if __name__ == "__main__":
    main()
