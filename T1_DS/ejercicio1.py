# 1.A
# Funciones básicas

#retorna la suma sin usar sum()
def calcular_suma(datos):
    suma=0
    for numero in datos:
        suma+=numero
    return suma

notas=[5.0, 6.5, 7.0, 5.5, 4.0]

#retorna la cantidad sin usar len()
def calcular_largo(datos):
    largo=0
    for numero in datos:
        largo+=1
    return largo

#usa calcular_suma y calcular_largo
def calcular_promedio(datos):
    suma=calcular_suma(datos)
    largo=calcular_largo(datos)
    if largo>0:
        promedio=suma/largo
        return promedio
    else:
        return 0

#recorre la lista para encontrar el mínimo
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

# 1.B
# Ordenamiento Bubble Sort

#Implementa una función de ordenamiento sin usar sorted() ni .sort():
#Ordena con Bubble sort . No modifica la original. Soporta orden ascendente y descendente

def bubble_sort(datos, descendente=False):
    copia = datos.copy()
    n = calcular_largo(copia)

    for iteracion in range(n):
        for posicion in range(0, n-1-iteracion):
            if descendente:
                if copia[posicion]<copia[posicion+1]:
                    aux=copia[posicion]
                    copia[posicion]=copia[posicion+1]
                    copia[posicion+1]=aux
                else:
                    if copia[posicion]>copia[posicion+1]:
                        aux=copia[posicion]
                        copia[posicion]=copia[posicion+1]
                        copia[posicion+1]=aux

    return copia

# 1.C 
# Mediana y Desviación Estándar

#Usando las funciones anteriores, implementa:
#Usa bubble_sort para ordenar, luego calcula la mediana.
def calcular_mediana(datos):
    datos_ordenados=bubble_sort(datos)
    n=calcular_largo(datos_ordenados)
    if n%2==1:
        return datos_ordenados[n//2]
    else:
        return (datos_ordenados[n//2-1]+datos_ordenados[n//2])/2

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

# 1.D
# Conversión de Temperaturas

# Usando las funciones anteriores, implementa:
# Convierte lista de Celsius a Fahrenheit. Retorna nueva lista
# Datos: grados_c = [0, 15, 25, 30, 100]

def celsius_a_fahrenheit(grados_c):
    grados_f=[]
    for celsius in grados_c:
        f=celsius*9/5+32
        grados_f.append(f)
    return grados_f

grados_c = [0, 15, 25, 30, 100]

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


def imprimir_titulo(texto):
    """Imprime un título decorado."""
    print("\n" + "=" * 60)
    print(texto)
    print("=" * 60)


def imprimir_lista(datos):
    """Imprime una lista en una sola línea."""
    print(datos)


def imprimir_reporte_ciudades(ciudades):
    """Imprime reporte estadístico por ciudad."""
    print(f"{'Ciudad':<15} {'Promedio':<12} {'Mínimo':<12} {'Máximo':<12}")
    print("-" * 55)

    for ciudad in ciudades:
        temperaturas = ciudad["temperaturas"]
        promedio = calcular_promedio(temperaturas)
        minimo = calcular_minimo(temperaturas)
        maximo = calcular_maximo(temperaturas)

        print(f"{ciudad['ciudad']:<15} "
              f"{promedio:<12.2f} "
              f"{minimo:<12.2f} "
              f"{maximo:<12.2f}")

#################################################################
#menu
#################################################################

imprimir_titulo("1.A Funciones basicas")
print("Lista de notas:", notas)
print("Suma:", calcular_suma(notas))
print("Largo:", calcular_largo(notas))
print("Promedio:", round(calcular_promedio(notas), 2))
print("Mínimo:", calcular_minimo(notas))
print("Máximo:", calcular_maximo(notas))

imprimir_titulo("1.B Ordenamiento Bubble Sort")
print("Orden ascendente:")
imprimir_lista(bubble_sort(notas))

print("Orden descendente:")
imprimir_lista(bubble_sort(notas, descendente=True))

print("Lista original (sin modificar):")
imprimir_lista(notas)

imprimir_titulo("1.C Mediana y Desviación Estándar")
print("Mediana:", calcular_mediana(notas))
print("Desviación estándar:", round(calcular_desviacion_estandar(notas), 4))

imprimir_titulo("1.D Conversión de Temperaturas")
print("Grados Celsius:", grados_c)
print("Grados Fahrenheit:", celsius_a_fahrenheit(grados_c))

imprimir_titulo("1.E Reporte Estadístico Integrado")
imprimir_reporte_ciudades(ciudades)
