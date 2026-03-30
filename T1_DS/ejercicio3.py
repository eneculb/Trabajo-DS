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
print(notas)

def contar_frecuencia(notas):
    frecuencia = {}
    for nota in notas:
        frecuencia[nota] = frecuencia.get(nota, 0) + 1
    return frecuencia

frecuencia = contar_frecuencia(notas)
print(dict(frecuencia))

def encontrar_moda(frecuencia):
    if not frecuencia:
        return None
    return max(frecuencia, key=frecuencia.get)

moda = encontrar_moda(frecuencia)
print(moda)

#3b Histograma de notas
def generar_histograma(frecuencia, ancho_max=25):
    if not frecuencia:
        return
    max_frecuencia = max(frecuencia.values())
    for nota in sorted(frecuencia.keys()):
        freq = frecuencia[nota]
        barra = '*' * int((freq / max_frecuencia) * ancho_max) if max_frecuencia > 0 else ''
        print(f"{nota}: {barra} ({freq})")

generar_histograma(frecuencia)

#3c Clasificacion por tramos
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
print(tramos)