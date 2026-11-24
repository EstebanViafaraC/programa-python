# Problema 5 - Horas trabajadas en la semana

horas = [
    ["Ana", 8, 9, 8, 8, 9],
    ["Carlos", 8, 8, 8, 8, 8],
    ["Laura", 10, 9, 9, 10, 8],
    ["Pedro", 7, 8, 6, 8, 7]
]

def calcular_jornada(fila):
    total = fila[1] + fila[2] + fila[3] + fila[4] + fila[5]
    if total > 40:
        tipo = "Sobretiempo"
    else:
        tipo = "Horario estandar"
    return total, tipo

print("Reporte de horas semanales")

for fila in horas:
    total, tipo = calcular_jornada(fila)
    print(fila[0], "-", total, "horas -", tipo)
