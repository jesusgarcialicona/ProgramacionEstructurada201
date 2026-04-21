# EJERCICIO 3: Decimal a romano (1 – 3000)

def decimal_a_romano(n):
    if not (1 <= n <= 3000):
        return "Error: el número debe estar entre 1 y 3000."
    
    tabla = [
        (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
        (100,  "C"), (90,  "XC"), (50,  "L"), (40,  "XL"),
        (10,   "X"), (9,   "IX"), (5,   "V"), (4,   "IV"),
        (1,    "I")
    ]
    
    resultado = ""
    for valor, simbolo in tabla:
        while n >= valor:
            resultado += simbolo
            n -= valor
    return resultado

print("\n--- Ejercicio 3: Decimal a romano ---")
for num in [1, 4, 9, 14, 40, 90, 399, 1994, 2024, 3000]:
    print(f"{num:4d} → {decimal_a_romano(num)}")