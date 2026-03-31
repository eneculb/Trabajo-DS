estudiantes = [
{"nombre": "Ana", "notas": [6.5, 7.0, 5.8]},
{"nombre": "Luis", "notas": [4.2, 5.1, 6.0]},
{"nombre": "Sofía", "notas": [3.9, 4.0, 4.5]},
{"nombre": "Pedro", "notas": [5.5, 6.1, 5.9]},
{"nombre": "Valentina", "notas": [7.0, 6.8, 6.9]},
{"nombre": "Javier", "notas": [4.0, 4.2, 4.1]},
{"nombre": "Camila", "notas": [5.0, 5.5, 5.8]},
{"nombre": "Martín", "notas": [3.5, 4.0, 4.2]},
{"nombre": "Fernanda", "notas": [6.2, 6.5, 6.0]},
{"nombre": "Tomás", "notas": [4.8, 5.0, 5.2]},
{"nombre": "Josefa", "notas": [5.9, 6.0, 6.1]},
{"nombre": "Matías", "notas": [3.8, 4.1, 4.0]},
{"nombre": "Ignacio", "notas": [6.7, 6.9, 7.0]},
{"nombre": "Daniela", "notas": [5.2, 5.4, 5.6]},
{"nombre": "Sebastián", "notas": [4.3, 4.5, 4.7]},
{"nombre": "Gabriela", "notas": [6.0, 6.2, 6.1]},
{"nombre": "Felipe", "notas": [5.7, 5.8, 5.9]},
{"nombre": "Antonia", "notas": [4.9, 5.0, 5.1]},
{"nombre": "Vicente", "notas": [3.7, 4.0, 4.3]},
{"nombre": "Paula", "notas": [6.3, 6.4, 6.5]}
]

def calcular_suma(datos):
    suma=0
    for numero in datos:
        suma+=numero
    return suma

def calcular_largo(datos):
    largo=0
    for numero in datos:
        largo+=1
    return largo

def calcular_promedio(datos):
    suma=calcular_suma(datos)
    largo=calcular_largo(datos)
    if largo>0:
        return suma/largo
    else:
        return 0

def calcular_minimo(datos):
    minimo=datos[0] #se asume que el primero es el menor
    for numero in datos:
        if numero<minimo:
            minimo=numero
    return minimo

def calcular_maximo(datos):
    maximo = datos[0]
    for numero in datos:
        if numero>maximo:
            maximo=numero
    return maximo

# 2.A
# Reporte de rendimiento

#Recibe un dict con clave 'notas' y retorna su promedio
def promedio_estudiante(estudiante):
    return calcular_promedio(estudiante["notas"])

#Retorna: Reprobado (<4.0), Suficiente (4.0-4.9), Aprobado (5.0-5.9), Destacado (>=6.0)
def clasificar_rendimiento(promedio):
    if promedio<4.0:
        return "Reprobado"
    elif promedio<5.0:
        return "Suficiente"
    elif promedio<6.0:
        return "Aprobado"
    else:
        return "Destacado"

#Retorna lista de dicts: nombre, promedio, estado, nota_max, nota_min, rango
def generar_reporte(estudiantes):
    reporte=[]
    for estudiante in estudiantes:
        nombre=estudiante["nombre"]
        notas=estudiante["notas"]
        promedio=promedio_estudiante(estudiante)
        estado=clasificar_rendimiento(promedio)
        nota_max=calcular_maximo(notas)
        nota_min=calcular_minimo(notas)
        rango=nota_max-nota_min
        
        reporte.append({
            "nombre":nombre,
            "promedio":promedio,
            "estado":estado,
            "nota_max":nota_max,
            "nota_min":nota_min,
            "rango":rango
        })
    return reporte

# 2.B
# Conteo y filtrado

#Dict con cantidad por estado
def contar_por_estado(reporte):
    conteo={
        "Reprobado":0,
        "Suficiente":0,
        "Aprobado":0,
        "Destacado":0
    }
    for estudiante in reporte:
        estado=estudiante["estado"]
        conteo[estado]+=1
    return conteo

#Lista de estudiantes con el estado dado
def filtrar_por_estado(reporte, estado):
    filtrados=[]
    for estudiante in reporte:
        if estudiante["estado"]==estado:
            filtrados.append(estudiante)
    return filtrados

# 2.C
# Ordenamiento del reporte

#Ordena por cualquier clave numérica con Bubble Sort
def ordenar_reporte(reporte, clave='promedio', descendente=True):
    copia = []
    for item in reporte:
        copia.append(item)
    n=len(copia)

    for iteracion in range(n):
        for posicion in range(0, n-1-iteracion):
            if descendente:
                if copia[posicion][clave]<copia[posicion+1][clave]:
                    aux = copia[posicion]
                    copia[posicion] = copia[posicion+1]
                    copia[posicion+1] = aux
            else:
                if copia[posicion][clave]>copia[posicion+1][clave]:
                    aux = copia[posicion]
                    copia[posicion] = copia[posicion+1]
                    copia[posicion+1] = aux

    return copia

# "2.D BUSQUEDA POR ESTUDIANTES":
#busca un estudiante por su nombre

#Búsqueda case-insensitive. Retorna dict o None
def buscar_estudiante(reporte, nombre):
    nombre = nombre.lower()
    for estudiante in reporte:
        if estudiante["nombre"].lower() == nombre:
            return estudiante
    return None

#Estudiantes con promedio en [minimo, maximo].
def buscar_por_rango_promedio(reporte, minimo, maximo):
    encontrados=[]
    for estudiante in reporte:
        if minimo<=estudiante["promedio"]<=maximo:
            encontrados.append(estudiante)
    return encontrados

#2.E
#Análisis de consistencia

#Identifica al estudiante más consistente (menor rango entre nota máxima y mínima) y al más
#inconsistente (mayor rango). Imprime el reporte completo con formato de tabla.

def analizar_consistencia(reporte):
    if len(reporte)==0:
        print("No hay estudiantes en el reporte.")
        return

    mas_consistente=reporte[0]
    mas_inconsistente=reporte[0]

    for estudiante in reporte:
        if estudiante["rango"]<mas_consistente["rango"]:
            mas_consistente = estudiante
        if estudiante["rango"]>mas_inconsistente["rango"]:
            mas_inconsistente=estudiante

    print("Estudiante más consistente:")
    print(mas_consistente)
    print("\nEstudiante más inconsistente:")
    print(mas_inconsistente)


#profe aqui le edimos ayuda a la ia pa que quedara mas bonito :D
def imprimir_titulo(texto):
    """Imprime un título decorado."""
    print("\n" + "=" * 60)
    print(texto)
    print("=" * 60)


def imprimir_reporte_tabla(reporte):
    """Imprime el reporte completo en formato de tabla."""
    print(f"{'Nombre':<12} {'Promedio':<10} {'Estado':<12} {'Máx':<6} {'Mín':<6} {'Rango':<6}")
    print("-" * 60)

    for estudiante in reporte:
        print(f"{estudiante['nombre']:<12} "
              f"{estudiante['promedio']:<10.2f} "
              f"{estudiante['estado']:<12} "
              f"{estudiante['nota_max']:<6.1f} "
              f"{estudiante['nota_min']:<6.1f} "
              f"{estudiante['rango']:<6.1f}")


def imprimir_lista_reporte(lista):
    """Imprime una lista de estudiantes del reporte en formato resumido."""
    if len(lista) == 0:
        print("No se encontraron estudiantes.")
        return

    for estudiante in lista:
        print(f"- {estudiante['nombre']} | Promedio: {estudiante['promedio']:.2f} | "
              f"Estado: {estudiante['estado']} | Rango: {estudiante['rango']:.1f}")


def imprimir_estudiante_original(estudiante):
    """Imprime un estudiante del listado original."""
    if estudiante is None:
        print("No se encontró el estudiante.")
    else:
        print(f"Nombre: {estudiante['nombre']} | Notas: {estudiante['notas']}")


# menu
reporte = generar_reporte(estudiantes)

imprimir_titulo("2.A REPORTE DE RENDIMIENTO")
imprimir_reporte_tabla(reporte)

imprimir_titulo("PROMEDIO Y CLASIFICACION DE ANA")
print("Promedio de Ana:", round(promedio_estudiante(estudiantes[0]), 2))
print("Clasificación de Ana:", clasificar_rendimiento(promedio_estudiante(estudiantes[0])))

imprimir_titulo("2.B CONTEO POR ESTADO")
conteo = contar_por_estado(reporte)
for estado in conteo:
    print(f"{estado}: {conteo[estado]}")

imprimir_titulo("2.B FILTRAR POR ESTADO: DESTACADO")
destacados = filtrar_por_estado(reporte, "Destacado")
imprimir_lista_reporte(destacados)

imprimir_titulo("2.C ORDENAR REPORTE POR PROMEDIO DESCENDENTE")
ordenado_promedio = ordenar_reporte(reporte, clave="promedio", descendente=True)
imprimir_reporte_tabla(ordenado_promedio)

imprimir_titulo("2.D BUSQUEDA DE ESTUDIANTE")
print("Buscar 'ana':")
imprimir_estudiante_original(buscar_estudiante(estudiantes, "ana"))

print("\nBuscar 'ANA':")
imprimir_estudiante_original(buscar_estudiante(estudiantes, "ANA"))

print("\nBuscar 'no existe':")
imprimir_estudiante_original(buscar_estudiante(estudiantes, "no existe"))

imprimir_titulo("2.D BUSQUEDA POR RANGO DE PROMEDIO [5.0 - 6.0]")
en_rango = buscar_por_rango_promedio(reporte, 5.0, 6.0)
imprimir_lista_reporte(en_rango)

imprimir_titulo("2.E ANALISIS DE CONSISTENCIA")
analizar_consistencia(reporte)
