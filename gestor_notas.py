# gestor_notas.py - Versión 1.0
# Calculador simple de promedio para la universidad

def calcular_promedio(nota_teoria, nota_practica):
    # Promedio simple inicial
    return (nota_teoria + nota_practica) / 2

if __name__ == "__main__":
    print("--- Gestor de Notas v1.0 ---")
    teoria = float(input("Introduce nota de teoría (0-10): "))
    practica = float(input("Introduce nota de prácticas (0-10): "))
    
    final = calcular_promedio(teoria, practica)
    print(f"Nota final calculada: {final:.2f}")
