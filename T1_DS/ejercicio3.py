#tp1 -3

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

#3a
def aplanarNotas(estudiantes):
    notas = []
    for estudiante in estudiantes:
        for nota in estudiante["notas"]:
            notas.append(nota)
    return notas
notas = aplanarNotas(estudiantes)
print(notas)

def contarFrecuencia(notas):
    frecuencia = {}
    for nota in notas:
        if nota in frecuencia:
            frecuencia[nota] += 1
        else:
            frecuencia[nota] = 1
    return frecuencia

frecuencia = contarFrecuencia(notas)
print(frecuencia)

def encontrarModa(frecuencia):
    moda = None
    max_frecuencia = 0
    for nota, freq in frecuencia.items():
        if freq > max_frecuencia:
            max_frecuencia = freq
            moda = nota
    return moda

moda = encontrarModa(frecuencia)
print(moda)

#3b
def generarHistograma(frecuencia, anchoMax=25):
    max_frecuencia = max(frecuencia.values())
    for nota in sorted(frecuencia.keys()):
        freq = frecuencia[nota]
        barra = '*' * int((freq / max_frecuencia) * anchoMax)
        print(f"{nota}: {barra} ({freq})")

generarHistograma(frecuencia)