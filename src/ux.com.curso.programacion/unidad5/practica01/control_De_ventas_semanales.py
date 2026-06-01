"""
Creamos un ciclo que solicite al usuario las ventas diarias de la semana,
el programa debe preguntar especificamente por el nombre del producto y 
dia. 
"""

# Declaración de estructuras

productos = ["Laptop", "Smartphone", "Tablet"]

ventas = [[0] * 3 for _ in range(3)]


total_por_producto = [0] * 3

# Lectura de datos
def leer_ventas():
    for i in range(3):

        print(f"--- Registro para {productos[i]} ---")

        for j in range(3):

            ventas[i][j] = int(input(f"Ventas del día {j+1}: "))

 
def reporte_ventas():
    total_general = 0

    for i in range(3):

        suma_producto = sum(ventas[i])
        total_por_producto[i] = suma_producto
        total_general += suma_producto

        print(f"{productos[i]}: {ventas[i]} | Total: {suma_producto}")

 

    print(f"\nEl total de ventas de la semana es: {total_general}")

    print(f"El promedio de ventas es: {total_general / 9:.2f}")

    # Producto mas vendido

    index_max = total_por_producto.index(max(total_por_producto))
    print(f"El producto más vendido es: {productos[index_max]} con {total_por_producto[index_max]} ventas.")       


def main():
    leer_ventas()
    reporte_ventas()

 

if __name__ == "__main__":
    main()