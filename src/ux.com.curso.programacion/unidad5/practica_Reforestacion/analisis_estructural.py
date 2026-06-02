"""
Materia: Programación Estructurada
Laboratorio: Refactorización y Análisis de Código
Alumno: [Tu Nombre]
"""
import random  # Única librería importada por el novato

# =====================================================================
# RETO 1: El Teorema de Fermat
# Sentido: Validar la famosa conjetura matemática.
# Problema: Usa un exponente fijo y potencia manual de Python (**).
# =====================================================================
def verificar_fermat(a, b, c):
    n = 4
    if n > 2:
        if a**n + b**n == c**n:
            print("¡Fermat se equivocó!")
        else:
            print("No, esa combinación no funciona.")

# =====================================================================
# RETO 2: Distancia Euclidiana entre dos puntos (Agente e IA)
# Sentido: Saber qué tan lejos está un robot (x1, y1) de su objetivo (x2, y2).
# Problema: Cálculo manual tosco de raíz cuadrada y potencias.
# =====================================================================
def calcular_distancia(x1, y1, x2, y2):
    # Fórmula: raíz de ((x2-x1)^2 + (y2-y1)^2)
    diferencia_x = x2 - x1
    diferencia_y = y2 - y1
    
    suma_cuadrados = (diferencia_x * diferencia_x) + (diferencia_y * diferencia_y)
    
    # Intento manual de sacar raíz cuadrada elevando a la 0.5
    distancia = suma_cuadrados ** 0.5 
    return distancia

# =====================================================================
# RETO 3: Selector Aleatorio de Respuestas para el Bot
# Sentido: Que el agente Discord responda con un saludo al azar.
# Problema: Usa condicionales masivos basados en un número aleatorio entero.
# =====================================================================
def obtener_saludo_agente():
    opcion = random.randint(1, 4)
    
    # Estructura condicional redundante e ineficiente para listas
    if opcion == 1:
        return "Hola, soy el agente de IA. ¿En qué ayudo?"
    elif opcion == 2:
        return "¡Conexión establecida! Listo para operar."
    elif opcion == 3:
        return "Sistemas en línea. Monitoreando el servidor."
    elif opcion == 4:
        return "Hola humano, procesando tus peticiones."

# =====================================================================
# RETO 4: Clasificador de Alertas Críticas (Validación de Rangos)
# Sentido: Evaluar si el error (Loss) de la IA requiere apagar el sistema.
# Problema: Anidación excesiva de "if-else" que oscurece el flujo lógico.
# =====================================================================
def evaluar_error_sistema(valor_loss):
    if valor_loss >= 0.0:
        if valor_loss < 0.4:
            return "Estable"
        else:
            if valor_loss < 0.8:
                return "Advertencia: Gradiente inestable"
            else:
                if valor_loss <= 1.0:
                    return "CRÍTICO: Abortar entrenamiento"
                else:
                    return "Error: Valor fuera de rango"
    else:
        return "Error: Valor negativo inválido"


# === PROGRAMA PRINCIPAL (Punto de entrada para probar) ===
if __name__ == "__main__":
    print("--- Probando Código Inicial ---")
    verificar_fermat(3, 4, 5)
    print("Distancia calculada:", calcular_distancia(0, 0, 3, 4))
    print("Respuesta bot:", obtener_saludo_agente())
    print("Estado del log:", evaluar_error_sistema(0.85))