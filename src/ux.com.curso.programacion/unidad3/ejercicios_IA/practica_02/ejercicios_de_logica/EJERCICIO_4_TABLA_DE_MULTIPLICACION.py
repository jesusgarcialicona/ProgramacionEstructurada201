# Definimos el límite de columnas (según la imagen es 15)
columnas = 15
# Definimos el límite de filas (usaremos 10 como estándar)
filas = 10

# 1. IMPRIMIR ENCABEZADO
# Dejamos un espacio inicial de 4 caracteres para la esquina superior izquierda
print(f"{'':<4}", end="")
for j in range(1, columnas + 1):
    print(f"{j:>4}", end="")
print() # Salto de línea

# 2. IMPRIMIR SEPARADOR (**)
print(f"{'**':<4}", end="")
for j in range(1, columnas + 1):
    print(f"{'**':>4}", end="")
print()

# 3. GENERAR EL CUERPO DE LA TABLA
for i in range(1, filas + 1):
    # Imprimimos la etiqueta de la fila (ej. 1*, 2*)
    etiqueta = f"{i}*"
    print(f"{etiqueta:<4}", end="")
    
    # Bucle interno para los resultados
    for j in range(1, columnas + 1):
        producto = i * j
        # Imprimimos el resultado alineado a la derecha en 4 espacios
        print(f"{producto:>4}", end="")
    
    # Al terminar una fila, hacemos un salto de línea
    print()