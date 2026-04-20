# Definición de la base de datos (Diccionario)
# Usamos los nombres exactos como los escribió tu profesor en la imagen
notas = {
    "Harry": [3.8, 4.0, 4.2],
    "Ron": [3.2, 3.8, 2.8],
    "Hemione": [5.0, 5.0, 5.0],
    "Daco": [4.5, 4.2, 5.0],
    "Nevil": [2.5, 3.0, 3.2]
}

# Funciones del Sistema de Notas

def promedio_simple(diccionario_notas):
    """1) Calcula el promedio simple (suma de notas / cantidad de notas)."""
    resultados = {}
    for estudiante, lista_notas in diccionario_notas.items():
        # Sumamos las 3 notas y dividimos entre 3
        prom = sum(lista_notas) / len(lista_notas)
        resultados[estudiante] = prom
    return resultados

def promedio_ponderado(diccionario_notas):
    """2) Calcula el promedio ponderado (30%, 30%, 40%)."""
    resultados = {}
    for estudiante, n in diccionario_notas.items():
        # n[0] es la nota 1 (30%), n[1] es la nota 2 (30%), n[2] es la nota 3 (40%)
        prom = (n[0] * 0.30) + (n[1] * 0.30) + (n[2] * 0.40)
        resultados[estudiante] = prom
    return resultados

def mejor_promedio(diccionario_promedios):
    """3) Determina quién tiene el mayor promedio final."""
    # max() puede buscar el valor más alto en un diccionario usando 'key=diccionario.get'
    mejor_estudiante = max(diccionario_promedios, key=diccionario_promedios.get)
    mejor_nota = diccionario_promedios[mejor_estudiante]
    return mejor_estudiante, mejor_nota

def reporte_mcgonagall(diccionario_promedios):
    """Bonus) Muestra los aprobados y el mensaje de la profesora McGonagall."""
    aprobados = []
    
    print("\n--- REPORTE FINAL DE LA PROFESORA MCGONAGALL ---")
    for estudiante, nota_final in diccionario_promedios.items():
        if nota_final >= 3.0:
            aprobados.append(estudiante)
            print(f"¡10 puntos para Gryffindor (o Slytherin)! {estudiante} APROBÓ con {nota_final:.2f}.")
        else:
            print(f"Un mago ha reprobado... {estudiante} REPROBÓ con {nota_final:.2f}.")
            
    print("\n Lista estricta de estudiantes aprobados:", aprobados)

# Programa Principal

print("--- SISTEMA DE CALIFICACIONES HOGWARTS ---")

# 1. Promedio simple
promedios_simp = promedio_simple(notas)
print("\n1) Promedios Simples:")
for est, nota in promedios_simp.items():
    print(f"   {est}: {nota:.2f}")

# 2. Promedio ponderado (Usaremos este como la nota definitiva)
promedios_pond = promedio_ponderado(notas)
print("\n2) Promedios Ponderados (Definitivas):")
for est, nota in promedios_pond.items():
    print(f"   {est}: {nota:.2f}")

# 3. Determinar el mejor de la clase
mejor_alumno, nota_maxima = mejor_promedio(promedios_pond)
print(f"\n3) El estudiante con el mayor promedio final es {mejor_alumno} con {nota_maxima:.2f}")

# 4 y Bonus. Mostrar aprobados y mensajes personalizados
reporte_mcgonagall(promedios_pond)