# Captura de datos (Paralelogramo de entrada)
N = int(input("Ingresa cuántos números impares deseas generar: "))

# Inicialización (Rectángulo de proceso)
contador = 0
numero = 1

# Ciclo de control (Rombo de decisión)
while contador < N:
    # Cuerpo del ciclo
    print(numero)           # Paralelogramo de salida
    numero = numero + 2     # Incrementar número al siguiente impar
    contador = contador + 1 # Registrar que un número fue procesado

# El programa finaliza automáticamente cuando contador == N