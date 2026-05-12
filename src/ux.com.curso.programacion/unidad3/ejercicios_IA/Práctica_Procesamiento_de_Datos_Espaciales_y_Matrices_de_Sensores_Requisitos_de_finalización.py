"""
Sistema de Visión y Proximidad para Robot IA
=============================================
Módulo de sensores vectoriales (1D) y cámara matricial (2D)
"""

def modulo_sensores():
    print("\n--- MÓDULO DE SENSORES (VECTORES) ---")
    sensores_distancia = []

    for i in range(5):
        while True:
            try:
                distancia = float(input(f"Ingrese distancia sensor {i + 1}: "))
                if distancia < 0:
                    print("  La distancia no puede ser negativa. Intente de nuevo.")
                else:
                    sensores_distancia.append(distancia)
                    break
            except ValueError:
                print("  Entrada inválida. Ingrese un número.")

    promedio = sum(sensores_distancia) / len(sensores_distancia)

    if promedio < 2.0:
        estado = "Aviso: Reduciendo velocidad global"
    else:
        estado = "Seguro"

    print(f"\nPromedio de proximidad: {promedio:.1f}m. Estado: {estado}.")
    return promedio, estado


def modulo_vision():
    print("\n--- MÓDULO DE VISIÓN (MATRICES) ---")
    print("Llenando matriz de cámara 3x3:\n")

    FILAS = 3
    COLS = 3
    camara_ia = []

    for f in range(FILAS):
        fila = []
        for c in range(COLS):
            while True:
                try:
                    brillo = int(input(f"Fila {f}, Col {c} (Brillo 0-255): "))
                    if brillo > 255:
                        print(f"  Valor {brillo} excede 255. Aplicando saturación → 255.")
                        brillo = 255
                    elif brillo < 0:
                        print("  El brillo no puede ser negativo. Asignando 0.")
                        brillo = 0
                    fila.append(brillo)
                    break
                except ValueError:
                    print("  Entrada inválida. Ingrese un número entero.")
        camara_ia.append(fila)

    print("\nVisualización de la imagen capturada:")
    for fila in camara_ia:
        valores = "  ".join(f"{v:>3}" for v in fila)
        print(f"[ {valores} ]")

    return camara_ia


def analisis_ia(camara_ia):
    print("\n Resultado de Análisis IA:")
    UMBRAL_BRILLO = 200
    pixeles_brillantes = sum(
        1 for fila in camara_ia for pixel in fila if pixel > UMBRAL_BRILLO
    )
    print(f"Se detectaron {pixeles_brillantes} píxeles de alta intensidad.")
    return pixeles_brillantes


def main():
    print("=" * 45)
    print("   SISTEMA DE VISIÓN Y PROXIMIDAD - ROBOT IA")
    print("=" * 45)

    promedio, estado = modulo_sensores()
    camara = modulo_vision()
    analisis_ia(camara)

    print("\n" + "=" * 45)
    print("Procesamiento finalizado.")
    print("=" * 45)


if __name__ == "__main__":
    main()