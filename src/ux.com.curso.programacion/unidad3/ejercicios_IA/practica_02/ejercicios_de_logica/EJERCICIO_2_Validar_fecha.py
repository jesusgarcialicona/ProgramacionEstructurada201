# EJERCICIO 2: Validar fecha

def es_bisiesto(anio):
    return (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0)

def validar_fecha(dd, mm, aaaa):
    if mm < 1 or mm > 12:
        return False
    
    dias_por_mes = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    dias_max = dias_por_mes[mm - 1]
    
    if mm == 2 and es_bisiesto(aaaa):
        dias_max = 29
    
    return 1 <= dd <= dias_max

print("\n--- Ejercicio 2: Validar fecha ---")
for dd, mm, aaaa in [(29, 2, 2024), (29, 2, 2023), (31, 4, 2024), (15, 6, 2025)]:
    estado = "válida" if validar_fecha(dd, mm, aaaa) else "inválida"
    print(f"{dd:02d}/{mm:02d}/{aaaa} → {estado}")
