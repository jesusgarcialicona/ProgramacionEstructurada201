import datetime

# 1. Configuración de Variables
nombre_asistente = "IA-UX"
print(f"¡Bienvenido! Soy {nombre_asistente}, tu asistente virtual.")
print("-" * 45)

# 2. Entrada de Datos
frase = input("¿En qué puedo ayudarte hoy?: ").lower()

# 3. Lógica de Clasificación
if "hola" in frase or "buenos días" in frase:
    # Intención: Saludo
    print("¡Hola! Soy tu asistente. Es un gusto saludarte.")

elif "clima" in frase or "temperatura" in frase:
    # Intención: Clima
    print("Consultando el servicio meteorológico... Hoy en Xalapa tendremos un día nublado.")

elif "hora" in frase or "tiempo" in frase:
    # Intención: Hora
    hora_actual = datetime.datetime.now().strftime("%H:%M:%S")
    print(f"La hora actual del sistema es: {hora_actual}.")

else:
    # Intención: Desconocida
    print("Lo siento, todavía no entiendo ese comando. ¿Podrías intentar con otra palabra?")

# 4. Despedida
print("-" * 45)
print(f"Proceso finalizado. Gracias por usar {nombre_asistente}.")