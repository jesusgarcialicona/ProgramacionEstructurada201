"""
Materia: Programación Estructurada
Laboratorio: Refactorización y Análisis de Código
Alumno: [Tu Nombre]
"""

import math    # CAMBIO: Se importa 'math' para usar math.hypot() y math.dist()
import random  # Se mantiene para random.choice()

# =====================================================================
# RETO 1: El Teorema de Fermat
# =====================================================================
def verificar_fermat(a, b, c):
    # CAMBIO: Se eliminó el 'if n > 2' anidado innecesario.
    # El valor n=4 es una constante que SIEMPRE es > 2, por lo que
    # esa comprobación nunca podría ser False. El condicional sobraba.
    # Se mantiene n como constante nombrada para mayor claridad.
    N = 4  # CAMBIO: Renombrada a mayúscula por convención de constante en Python (PEP 8)
    if a**N + b**N == c**N:
        print("¡Fermat se equivocó!")
    else:
        print("No, esa combinación no funciona.")


# =====================================================================
# RETO 2: Distancia Euclidiana entre dos puntos
# =====================================================================
def calcular_distancia(x1, y1, x2, y2):
    # CAMBIO: Se reemplazaron los 4 pasos manuales (diferencia_x,
    # diferencia_y, suma_cuadrados, ** 0.5) por una sola llamada a
    # math.hypot(). Esta función de la librería estándar hace exactamente
    # lo mismo pero de forma más legible, precisa y eficiente.
    # math.hypot(dx, dy) calcula sqrt(dx**2 + dy**2) internamente.
    return math.hypot(x2 - x1, y2 - y1)

    # ALTERNATIVA aún más semántica disponible desde Python 3.8:
    # return math.dist((x1, y1), (x2, y2))


# =====================================================================
# RETO 3: Selector Aleatorio de Respuestas para el Bot
# =====================================================================
def obtener_saludo_agente():
    # CAMBIO: Se eliminaron los 4 bloques if/elif que mapeaban un número
    # a una cadena de texto. Ese patrón es exactamente lo que hace
    # random.choice(): elige un elemento al azar de una lista.
    # Ahora agregar o quitar saludos solo requiere editar la lista,
    # sin tocar ninguna lógica condicional.
    saludos = [
        "Hola, soy el agente de IA. ¿En qué ayudo?",
        "¡Conexión establecida! Listo para operar.",
        "Sistemas en línea. Monitoreando el servidor.",
        "Hola humano, procesando tus peticiones.",
    ]
    return random.choice(saludos)


# =====================================================================
# RETO 4: Clasificador de Alertas Críticas
# =====================================================================
def evaluar_error_sistema(valor_loss):
    # CAMBIO: Se aplanaron los 5 niveles de anidación if/else en
    # cláusulas de guarda (early return). La técnica consiste en
    # comprobar primero los casos inválidos o extremos y salir
    # inmediatamente, en lugar de envolver toda la lógica en if anidados.
    # Ventajas: menos indentación, flujo lineal fácil de leer y de testear.

    # Guardas para valores fuera del rango válido [0.0, 1.0]
    if valor_loss < 0.0:
        return "Error: Valor negativo inválido"
    if valor_loss > 1.0:
        return "Error: Valor fuera de rango"

    # Clasificación lineal dentro del rango válido
    if valor_loss < 0.4:
        return "Estable"
    if valor_loss < 0.8:
        return "Advertencia: Gradiente inestable"
    return "CRÍTICO: Abortar entrenamiento"


# === PROGRAMA PRINCIPAL ===
if __name__ == "__main__":
    print("--- Probando Código Refactorizado ---")
    verificar_fermat(3, 4, 5)
    print("Distancia calculada:", calcular_distancia(0, 0, 3, 4))
    print("Respuesta bot:", obtener_saludo_agente())
    print("Estado del sistema:", evaluar_error_sistema(0.85))