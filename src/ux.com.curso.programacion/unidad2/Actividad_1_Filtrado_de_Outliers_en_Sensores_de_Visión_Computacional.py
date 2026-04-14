TOTAL_LECTURAS = 10
RANGO_MIN      = 65.0   # % minimo valido (inclusive)
RANGO_MAX      = 85.0   # % maximo valido (inclusive)
 
 
def solicitar_lectura(numero):
    """Pide al usuario una lectura de confianza (0-100) y la valida."""
    while True:
        try:
            valor = float(input(f"  Lectura [{numero}/{TOTAL_LECTURAS}] - precision (%): "))
            if 0.0 <= valor <= 100.0:
                return valor
            print("  [!] El valor debe estar entre 0 y 100. Intente de nuevo.")
        except ValueError:
            print("  [!] Entrada invalida. Ingrese un numero.")
 
 
def clasificar_lectura(valor):
    """Devuelve True si la lectura esta dentro del rango valido."""
    return RANGO_MIN <= valor <= RANGO_MAX
 
 
def main():
    print("=" * 52)
    print("   FILTRADO DE OUTLIERS - SENSOR DE PROFUNDIDAD")
    print("=" * 52)
    print(f"   Rango de Inferencia Valido : {RANGO_MIN}% - {RANGO_MAX}%")
    print(f"   Total de lecturas          : {TOTAL_LECTURAS}")
    print()
 
    lecturas_validas = []
    outliers         = []
 
    for i in range(1, TOTAL_LECTURAS + 1):
        valor = solicitar_lectura(i)
 
        if clasificar_lectura(valor):
            lecturas_validas.append(valor)
            print(f"  -> VALIDA   {valor:.1f}%  (dentro del rango)\n")
        else:
            outliers.append(valor)
            print(f"  -> OUTLIER  {valor:.1f}%  (ruido - descartada)\n")
 
    # -- Resultados --
    print("-" * 14)
    print("  RESULTADOS")
    print("-" * 14)
    print(f"  Lecturas validas : {[f'{v:.1f}' for v in lecturas_validas]}")
    print(f"  Outliers (ruido) : {[f'{v:.1f}' for v in outliers]}")
    print()
 
    if lecturas_validas:
        promedio = sum(lecturas_validas) / len(lecturas_validas)
        print(f"  Promedio de precision (lecturas validas): {promedio:.2f}%")
        print(f"  Lecturas usadas  : {len(lecturas_validas)} de {TOTAL_LECTURAS}")
        print(f"  Outliers omitidos: {len(outliers)}")
    else:
        print("  Ninguna lectura cayo dentro del rango valido.")
        print("  No es posible calcular un promedio confiable.")
 
    print("-" * 58)
 
 
if __name__ == "__main__":
    main()