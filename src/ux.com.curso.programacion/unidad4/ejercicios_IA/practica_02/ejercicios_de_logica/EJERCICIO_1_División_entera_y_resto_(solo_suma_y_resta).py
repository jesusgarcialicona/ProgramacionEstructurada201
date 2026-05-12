
def division_entera(a, b):
    if b == 0:
        print("Error: no se puede dividir entre cero.")
        return
    cociente = 0
    resto = a
    while resto >= b:
        resto = resto - b
        cociente = cociente + 1
    print(f"Cociente: {cociente}, Resto: {resto}")

print("--- Ejercicio 1: División entera ---")
division_entera(17, 5)   # Cociente: 3, Resto: 2
division_entera(100, 7)  # Cociente: 14, Resto: 2
