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

#Recibe un dict con clave 'notas' y retorna su promedio
def promedio_estudiantes(estudiantes):
    return calcular_promedio(estudiantes["notas"])

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

# 2.A
# Reporte de rendimiento
#Retorna lista de dicts: nombre, promedio, estado, nota_max, nota_min, rango
def generar_reporte(estudiantes):
    reporte=[]
    for estudiante in estudiantes:
        nombre=estudiante["nombre"]
        notas=estudiante["notas"]
        promedio=calcular_promedio(notas)
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

print(promedio_estudiantes(estudiantes[0]))

print(clasificar_rendimiento(promedio_estudiantes(estudiantes[0])))

reporte = generar_reporte(estudiantes)

for item in reporte:
    print(item)

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
    for item in reporte:
        estado=item["estado"]
        conteo[estado]+=1
    return conteo
print(contar_por_estado(reporte))

#Lista de estudiantes con el estado dado

def filtrar_por_estado(reporte, estado):
    filtrados=[]
    for item in reporte:
        if item["estado"]==estado:
            filtrados.append(item)
    return filtrados
print(filtrar_por_estado(reporte, "Destacado"))

# 2.C
# Ordenamiento del reporte

#Ordena por cualquier clave numérica con Bubble Sort
def ordenar_reporte(reporte,clave="promedio", descendente=True):
    copia=[]
    for item in reporte:
        copia.append(item)

    n=len(copia)

    for i in range(n):
        for j in range(0, n-i-1):
            if descendente:
                if copia[j][clave]<copia[j+1][clave]:
                    aux=copia[j]
                    copia[j]=copia[j+1]
                    copia[j+1]=aux
            else:
                if copia[j][clave]>copia[j+1][clave]:
                    aux=copia[j]
                    copia[j]=copia[j+1]
                    copia[j+1]=aux
    return copia
print(ordenar_reporte(reporte, clave="promedio", descendente=True))


# "2.D BUSQUEDA POR ESTUDIANTES":
#busca un estudiante por su nombre (sin importar que hayan mayúsculas o minúsculas)
def buscar_estudiante(estudiantes, nombre):
    for estudiante in estudiantes:
        
        # comparo los nombres en minúscula
        if estudiante["nombre"].lower() == nombre.lower():
            return estudiante
    
    # si no lo encuentra, despliega en pantalla el siguiente mensaje al usuario
    return "El nombre del estudiante ingresado no existe, por favor ingrese uno válido"
    

# "2.E ANÁLISIS DE CONSISTENCIA":
# busca al estudiante con notas "más parecidas" (estables)
# y el con notas "muy distintas entre si" (menos estable)
def analizar_consistencia(reporte):
    
    # primero tomo el primero como referencia
    mas_estable = reporte[0]
    menos_estable = reporte[0]
    
    # recorro toda la lista de estudiantes
    for estudiante in reporte:
        
        # saco el rango (diferencia entre nota max y min)
        rango = estudiante["rango"]
        
        # si encuentra uno con menor rango, se guarda
        if rango < mas_estable["rango"]:
            mas_estable = estudiante
        
        # si encuentra uno con mayor rango, se guarda
        if rango > menos_estable["rango"]:
            menos_estable = estudiante
    
    # se retornan ambos resultados
    return mas_estable, menos_estable


# finalmente se utiliza la función y despliega en pantalla los resultados
estable, inestable = analizar_consistencia(reporte)

print("El estudiante con mayor estabilidad es:", estable["nombre"])
print("El estudiante con menor estabilidad es:", inestable["nombre"])

