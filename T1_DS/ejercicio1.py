# 1.A
# Funciones básicas

#retorna la suma sin usar sum()
def calcular_suma(datos):
    suma=0
    for numero in datos:
        suma+=numero
    return suma

notas=[5.0, 6.5, 7.0, 5.5, 4.0]
print(calcular_suma(notas))

#retorna la cantidad sin usar len()
def calcular_largo(datos):
    largo=0
    for numero in datos:
        largo+=1
    return largo
print(calcular_largo(notas))

#usa calcular_suma y calcular_largo
def calcular_promedio(datos):
    suma=calcular_suma(datos)
    largo=calcular_largo(datos)
    if largo>0:
        promedio=suma/largo
        return promedio
    else:
        return 0
print(calcular_promedio(notas))

#recorre la lista para encontrar el mínimo
def calcular_minimo(datos):
    minimo=datos[0] #se asume que el primero es el menor
    for numero in datos:
        if numero<minimo:
            minimo=numero
    return minimo
print(calcular_minimo(notas))

def calcular_maximo(datos):
    maximo = datos[0]
    for numero in datos:
        if numero>maximo:
            maximo=numero
    return maximo
print(calcular_maximo(notas))

# 1.B
# Ordenamiento Bubble Sort

#Ordena con Bubble sort . No modifica la original. Soporta orden ascendente y descendente

def bubble_Sort(datos, descendente=False):
    datos=datos.copy()
    n=calcular_largo(datos)
    for i in range(n):
        for j in range(0, n-i-1):
            if (descendente and datos[j]<datos[j+1]) or (not descendente and datos[j]>datos[j+1]):
                # Intercambiar
                datos[j], datos[j+1] = datos[j+1], datos[j]
    return datos

print("Orden ascendente:")
print(bubble_Sort(notas))
print("Orden descendente:")
print(bubble_Sort(notas, descendente=True))

# 1.C
# Mediana y Desviación Estándar

#Usa bubble_sort para ordenar, luego calcula la mediana.
def calcular_mediana(datos):
    datos_ordenados=bubble_Sort(datos)
    n=calcular_largo(datos_ordenados)
    if n%2==1:
        return datos_ordenados[n//2]
    else:
        return (datos_ordenados[n//2 - 1] + datos_ordenados[n//2]) / 2
    
print(calcular_mediana(notas))

#Desviación estándar poblacional: sqrt(sum((x-prom)²)/n)
def calcular_desviacion_estandar(datos):
    promedio=calcular_promedio(datos)
    suma_cuadrados=0
    n=calcular_largo(datos)
    for numero in datos:
        suma_cuadrados+=(numero-promedio)**2
    if n>0:
        return (suma_cuadrados/n)**0.5
    else:
        return 0
    
print(calcular_desviacion_estandar(notas))

# 1.D
# Conversión de Temperaturas

# Convierte lista de Celsius a Fahrenheit. Retorna nueva lista
# Datos: grados_c = [0, 15, 25, 30, 100]

def celsius_a_fahrenheit(grados_c):
    grados_f=[]
    for c in grados_c:
        f=c*9/5+32
        grados_f.append(f)
    return grados_f

grados_c = [0, 15, 25, 30, 100]
print(celsius_a_fahrenheit(grados_c))

# 1.E
# Reporte Estadístico Integrado

#Aplica todas tus funciones al siguiente dataset de temperaturas mensuales de ciudades chilenas e imprime un reporte por ciudad con promedio, mínima y máxima:

ciudades = [
{"ciudad": "Santiago", "temperaturas": [30.2, 28.5, 25.1, 18.3, 12.7, 9.5, 8.8, 10.1, 14.6, 19.3, 24.8, 28.9]},
{"ciudad": "Valparaíso", "temperaturas": [22.1, 21.8, 20.5, 17.2, 14.3, 12.1, 11.5, 12.0, 13.8, 16.5, 19.2, 21.0]},
{"ciudad": "Concepción", "temperaturas": [20.5, 19.8, 17.2, 13.5, 10.8, 8.5, 7.9, 9.2, 11.5, 14.8, 17.5, 19.8]},
{"ciudad": "Temuco", "temperaturas": [22.3, 21.5, 18.0, 13.2, 9.5, 7.0, 6.5, 8.0, 10.5, 14.0, 17.8, 20.5]},
{"ciudad": "Punta Arenas", "temperaturas": [14.2, 13.5, 11.0, 7.5, 4.2, 2.0, 1.5, 3.0, 6.5, 9.8, 12.0, 13.8]},
]


for ciudad in ciudades:
    temp=ciudad["temperaturas"]
    print(f"Reporte para {ciudad['ciudad']}:")
    print(f"  Promedio: {calcular_promedio(temp):.2f}°C")
    print(f"  Mínimo: {calcular_minimo(temp):.2f}°C")
    print(f"  Máximo: {calcular_maximo(temp):.2f}°C")
    print()




