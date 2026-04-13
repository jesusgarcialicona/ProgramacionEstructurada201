
# Sistema de Piloto Automático - Procesamiento de Sensores de Vehículo Autónomo

# ─────────────────────────────────────────────
# 2. CONFIGURACIÓN DE VARIABLES (Simulación de Sensores)
# ─────────────────────────────────────────────

distancia = float(input("¿A qué distancia está el objeto más cercano (en metros)?: "))
semaforo = input("¿De qué color está el semáforo? (verde/amarillo/rojo): ").lower()
peaton = input("¿Hay un peatón cruzando? (si/no): ").lower()

print()  # Línea en blanco para mejor legibilidad

# ─────────────────────────────────────────────
# 3. LÓGICA DE NAVEGACIÓN (Estructuras Condicionales)
# ─────────────────────────────────────────────

# PRIORIDAD MÁXIMA: Frenado de Emergencia
if distancia < 5 or peaton == "si":
    print("¡FRENO DE EMERGENCIA ACTIVADO! Deteniendo el vehículo inmediatamente.")

# REGLA DEL SEMÁFORO
elif semaforo == "rojo":
    print("Estado: Detenido. Esperando luz verde.")

elif semaforo == "amarillo":
    print("Estado: Precaución. Reduciendo velocidad para detenerse.")

elif semaforo == "verde" and distancia >= 5:
    print("Estado: En movimiento. Todo despejado para avanzar.")

# CASO DE ERROR EN SENSORES
else:
    print("Error de lectura en sensores: Color de semáforo no reconocido.")

# ─────────────────────────────────────────────
# 4. RESUMEN DE SEGURIDAD
# ─────────────────────────────────────────────

print()
print("Monitoreo de sensores constante... Sistema activo.")