# Tabla de multiplicar (filas del 1 al 4, columnas del 1 al 15)

# Encabezado
print("     ", end="")
for j in range(1, 16):
    print(f"{j:4}", end="")
print()

print("     ", end="")
for j in range(1, 16):
    print(f"{'**':4}", end="")
print()

# Filas de la tabla
for i in range(1, 5):
    print(f"{i}*  ", end="")
    for j in range(1, 16):
        print(f"{i * j:4}", end="")
    print()