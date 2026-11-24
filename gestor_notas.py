# gestor_notas.py - Versión con Menciones Cualitativas (Rama feature)

def calcular_promedio(nota_teoria, nota_practica):
    # Ponderación teoría/prácticas: 60% teoría, 40% laboratorio
    return (nota_teoria * 0.60) + (nota_practica * 0.40)

def obtener_mencion(nota):
    # Escala de calificaciones del sistema universitario español
    if nota < 5.0:
        return "Suspenso"
    elif nota < 7.0:
        return "Aprobado"
    elif nota < 9.0:
        return "Notable"
    else:
        return "Sobresaliente"

if __name__ == "__main__":
    print("--- Gestor de Notas (UJI) ---")
    teoria = float(input("Introduce nota de teoría (0-10): "))
    practica = float(input("Introduce nota de prácticas (0-10): "))
    
    final = calcular_promedio(teoria, practica)
    # Calculamos la mención cualitativa correspondiente
    mencion = obtener_mencion(final)
    print(f"Resultado final de la asignatura: {final:.2f} ({mencion})")
