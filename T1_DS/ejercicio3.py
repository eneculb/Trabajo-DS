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

#3a Frecuencia de notas
def aplanar_notas(estudiantes):
    return [nota for estudiante in estudiantes for nota in estudiante["notas"]]

notas = aplanar_notas(estudiantes)
print("\n TODAS LAS NOTAS:")
print(notas)

def contar_frecuencia(notas):
    frecuencia = {}
    for nota in notas:
        frecuencia[nota] = frecuencia.get(nota, 0) + 1
    return frecuencia

frecuencia = contar_frecuencia(notas)
print("\n Frecuencia de notas:")
for nota in sorted(frecuencia.keys()):
    print(f"  Nota {nota}: aparece {frecuencia[nota]} veces")

def encontrar_moda(frecuencia):
    if not frecuencia:
        return None
    return max(frecuencia, key=frecuencia.get)

moda = encontrar_moda(frecuencia)
print(f"\n Nota mas frecuente: {moda}\n")

# 3b: Histograma visual de notas
def generar_histograma(frecuencia, ancho_max=25):
    if not frecuencia:
        return
    max_frecuencia = max(frecuencia.values())
    print(" Histograma de notas:")
    for nota in sorted(frecuencia.keys()):
        freq = frecuencia[nota]
        barra = '█' * int((freq / max_frecuencia) * ancho_max) 
        print(f"  {nota}  | {barra} ({freq})")

generar_histograma(frecuencia)

# 3c: Clasificación de desempeño por tramos
def clasificar_tramos(estudiantes):
    tramos = {"1.0-3.9": 0, "4.0-5.9": 0, "6.0-7.0": 0}
    for estudiante in estudiantes:
        for nota in estudiante["notas"]:
            if 1.0 <= nota <= 3.9:
                tramos["1.0-3.9"] += 1
            elif 4.0 <= nota <= 5.9:
                tramos["4.0-5.9"] += 1
            elif 6.0 <= nota <= 7.0:
                tramos["6.0-7.0"] += 1
    return tramos

tramos = clasificar_tramos(estudiantes)
print(f"\n Clasificacion por tramos:\n")
for tramo, cantidad in tramos.items():
    print(f"  {tramo}: {cantidad} notas")


#3.D: 
def limpiar_texto(texto):
    texto = texto.lower()
    texto_limpio = ""
    for caracter in texto:
        if caracter not in ".,;:¿?¡!\n":
            texto_limpio += caracter
        else:
            texto limpio += ""

return texto_limpio

def frecuencia_palabras(texto_limpio):
    palabras = texto_limpio.split()
    frecuencias = {}

    for palabra in palabras:
        if palabra in frecuencias:
            frecuencias[palabras] += 1
        if palabra not in conteo:
            conteo[palabra] = 0
        conteo[palabra] += 1
    return frecuencias

def top_n_palabras(frecuencias, n=10):
    lista = []
    for palabras in frecuencias:
        lista.append((palabra, frecuencia[palabra]))

    for i in range(len(lista)):
        for j in range(i + 1, len(lista)):
        if lista[j][1] > lista[i][1]:
            lista[i], lista[j] = lista[j], lista[i]
     
    return lista[:n]

def diversidad_lexica(texto_limpio):
    palabras = texto_limpio.split()

    total = len(palabras)

   unicas = []

for p in palabras:
    if p not in unicas:
        unicas.append(p)

cantidad_unicas = len(unicas)

return cantidad_ unicas / total

def main():
    texto_limpio = limpiar_texto(texto)
    frec = frecuencia_palabra(texto_limpio)
    top = top_n_palabras(frec, 5)
    diversidad = diversidad_lexica(texto_limpio)

print("Top palabras:")
for palabra, cantidad in top:
    print(palabra, "->", cantidad)

print("\nDiversidad:", round(div, 3))

main()

#3.E : Biagramas
def calcular_bigramas(texto_limpio):
    """Saca las palabras consecutivas y cuenta cuantas veces sale cada par."""
    palabras = texto_limpio.split()
    bigramas = {}

       # Le resto 1 al largo para que el ciclo no se caiga al buscar la 'palabra siguiente' en la ultima vuelta
         for i in range(len(palabras) - 1):
        
        # Junto la palabra actual con la que viene despues
        par = palabras[i] + " " + palabras[i + 1]

    if par not in bigramas:
        bigramas[par] = 0
            
        bigramas[par] += 1

    return bigramas
