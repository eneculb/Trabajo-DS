#Ejercicio 3 Analisis de Frecuencias y Texto

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

texto = """La ciencia de datos es un campo interdisciplinario que utiliza
métodos científicos y algoritmos para extraer conocimiento de
los datos. La estadística y la programación son herramientas
fundamentales para un científico de datos. Los datos pueden
ser estructurados o no estructurados. El análisis de datos
permite tomar decisiones basadas en evidencia."""

def calcular_largo(datos):
    largo=0
    for numero in datos:
        largo+=1
    return largo

def bubble_sort_lista_tuplas(datos, descendente=True):
    copia=[]
    for elemento in datos:
        copia.append(elemento)

    n = calcular_largo(copia)

    for iteracion in range(n):
        for posicion in range(0, n-1-iteracion):
            actual=copia[posicion][1]
            siguiente=copia[posicion + 1][1]

            if descendente:
                if actual<siguiente:
                    aux=copia[posicion]
                    copia[posicion]=copia[posicion+1]
                    copia[posicion+1]=aux
            else:
                if actual>siguiente:
                    aux=copia[posicion]
                    copia[posicion]=copia[posicion+1]
                    copia[posicion+1]=aux
    return copia

#3.A
#Frecuencia de notas
#Aplana todas las notas de los 20 estudiantes en una sola lista y analiza sus frecuencias:

#Lista plana con todas las notas
def aplanar_notas(estudiantes):
    return [nota for estudiante in estudiantes for nota in estudiante["notas"]]
notas = aplanar_notas(estudiantes)

def contar_frecuencia(notas):
    frecuencias = {}

    for nota in notas:
        if nota in frecuencias:
            frecuencias[nota] += 1
        else:
            frecuencias[nota] = 1

    return frecuencias

def encontrar_moda(frecuencia):
    valor_mas_frecuente=None
    cantidad_maxima=0

    for valor in frecuencia:
        if frecuencia[valor]>cantidad_maxima:
            valor_mas_frecuente=valor
            cantidad_maxima=frecuencia[valor]

    return valor_mas_frecuente, cantidad_maxima

# 3b: Histograma visual de notas
def generar_histograma(frecuencia, ancho_max=25):
    max_frecuencia = 0

    for valor in frecuencia:
        if frecuencia[valor]>max_frecuencia:
            max_frecuencia=frecuencia[valor]

    pares=[]
    for valor in frecuencia:
        pares.append((valor, frecuencia[valor]))

    pares=bubble_sort_lista_tuplas(pares, descendente=False)

    for valor, frecuencia in pares:
        largo_barra=int((frecuencia / max_frecuencia) * ancho_max)
        barra="█"*largo_barra
        print(f"{valor:<4}|{barra}({frecuencia})")

# 3c: Clasificación de desempeño por tramos
def clasificar_tramos(datos, tramos):
    resultado = {}

    for nombre_tramo in tramos:
            resultado[nombre_tramo]=0

    for valor in datos:
            for nombre_tramo in tramos:
                minimo, maximo=tramos[nombre_tramo]

                if valor>=minimo and valor<=maximo:
                    resultado[nombre_tramo]+=1
                    break
    return resultado
#3.D:
#Analiza el siguiente texto y extrae estadísticas:
def limpiar_texto(texto):
    texto = texto.lower()
    texto_limpio = ""
    signos=".,;:¿?¡!\n"
    for caracter in texto:
        if caracter in signos:
            if caracter=="\n":
                texto_limpio += " "
            else:
                texto_limpio += " "
        else:
            texto_limpio += caracter
    texto_final=""
    espacio_anterior=False

    for caracter in texto_limpio:
        if caracter==" ":
            if not espacio_anterior:
                texto_final+=" "
                espacio_anterior=True
        else:
            texto_final += caracter
            espacio_anterior=False
    return texto_final.strip()

def frecuencia_palabras(texto_limpio):
    palabras = texto_limpio.split()
    frecuencias = {}

    for palabra in palabras:
        if palabra in frecuencias:
            frecuencias[palabra]+=1
        else:
            frecuencias[palabra]=1
    return frecuencias

def top_n_palabras(frecuencias, n=10):
    lista=[]
    for palabra in frecuencias:
        lista.append((palabra, frecuencias[palabra]))
        
    lista_ordenada=bubble_sort_lista_tuplas(lista, descendente=True)
    top=[]
    contador=0
    for palabra, frecuencia in lista_ordenada:
        if contador<n:
            top.append((palabra, frecuencia))
            contador+=1
    return top

def diversidad_lexica(texto_limpio):
    palabras = texto_limpio.split()
    total_palabras = calcular_largo(palabras)
    frecuencia=frecuencia_palabras(texto_limpio)
    palabras_unicas = calcular_largo(frecuencia)

    if total_palabras>0:
        return palabras_unicas / total_palabras
    else:
        return 0

#3.E : Biagramas
def calcular_bigramas(texto_limpio):

    palabras = texto_limpio.split()
    bigramas = {}
    
    for posicion in range(calcular_largo(palabras) - 1):
        bigrama = palabras[posicion] + " " + palabras[posicion + 1]

        if bigrama in bigramas:
            bigramas[bigrama] += 1
        else:
            bigramas[bigrama] = 1

    return bigramas


# Funciones para mejorar la presentación
def imprimir_titulo(texto):
    """Imprime un título decorado."""
    print("\n" + "=" * 60)
    print(texto)
    print("=" * 60)


def imprimir_diccionario(diccionario):
    """Imprime un diccionario clave: valor."""
    for clave in diccionario:
        print(f"{clave}: {diccionario[clave]}")


def imprimir_top(lista_tuplas):
    """Imprime una lista de tuplas (elemento, frecuencia)."""
    for elemento, frecuencia in lista_tuplas:
        print(f"- {elemento}: {frecuencia}")


#menu

# 3.A
notas_planas = aplanar_notas(estudiantes)
frecuencias_notas = contar_frecuencia(notas_planas)
moda, cantidad_moda = encontrar_moda(frecuencias_notas)

imprimir_titulo("3.A FRECUENCIAS DE NOTAS")
print("Notas aplanadas:")
print(notas_planas)

print("\nFrecuencias de notas:")
imprimir_diccionario(frecuencias_notas)

print(f"\nModa: {moda} (aparece {cantidad_moda} veces)")

# 3.B
imprimir_titulo("3.B HISTOGRAMA DE FRECUENCIAS")
generar_histograma(frecuencias_notas)

# 3.C
tramos = {
    "1.0-3.9": (1.0, 3.9),
    "4.0-5.9": (4.0, 5.9),
    "6.0-7.0": (6.0, 7.0)
}

clasificacion_tramos = clasificar_tramos(notas_planas, tramos)

imprimir_titulo("3.C CLASIFICACION EN TRAMOS")
imprimir_diccionario(clasificacion_tramos)

# 3.D
texto_limpio = limpiar_texto(texto)
frecuencias_palabras = frecuencia_palabras(texto_limpio)
top_palabras = top_n_palabras(frecuencias_palabras, 10)
diversidad = diversidad_lexica(texto_limpio)

imprimir_titulo("3.D ANALISIS DE TEXTO")
print("Texto limpio:")
print(texto_limpio)

print("\nFrecuencia de palabras:")
imprimir_diccionario(frecuencias_palabras)

print("\nTop 10 palabras:")
imprimir_top(top_palabras)

print(f"\nDiversidad léxica: {diversidad:.4f}")

# 3.E
bigramas = calcular_bigramas(texto_limpio)
top_bigramas = top_n_palabras(bigramas, 10)

imprimir_titulo("3.E BIGRAMAS")
print("Frecuencia de bigramas:")
imprimir_diccionario(bigramas)

print("\nTop 10 bigramas:")
imprimir_top(top_bigramas)
