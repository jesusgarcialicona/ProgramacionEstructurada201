def print_funciones_externas():
    print("funciones externas (bibliotecas)")
# 1. IMPORTACIÓN
# Importamos la biblioteca externa y le asignamos un alias 'np' para facilitar su uso
import numpy as np
def procesar_estadisticas(lista_mensajes):
 """
 Función que recibe datos y utiliza funciones externas de
 la biblioteca NumPy para procesarlos.
 """
 # Invocación de función externa para el promedio
 promedio = np.mean(lista_mensajes)

 # Invocación de función externa para encontrar el valor máximo
 pico_maximo = np.max(lista_mensajes)

 #calculo de la media
 media = np.median(lista_mensajes)

 # Invocación de función externa para la desviación estándar
 desviacion = np.std(lista_mensajes)

 return promedio, pico_maximo, media, desviacion
# --- Programa Principal ---
# Datos: Mensajes enviados cada hora durante un turno de 8 horas
datos_servidor = [15, 42, 88, 30, 120, 55, 72, 20]
# Llamada a nuestra función enviando los parámetros de entrada
prom, maximo, media, ds = procesar_estadisticas(datos_servidor)
print("=== REPORTE DE ACTIVIDAD DEL SERVIDOR ===")
print(f"Promedio de mensajes por hora: {prom:.2f}")
print(f"Pico de actividad registrado: {maximo} mensajes")
print(f"Variabilidad del tráfico (Desviación): {ds:.2f}")
print(f"Media de mensajes por hora: {media:.2f}")


def __main__():
    print("Análisis de mensajes completado.")
    

#Qué sucede si intentas usar np.mean() sin haber hecho elimport al principio del archivo?
# Respuesta: Si intentas usar np.mean() sin haber importado la biblioteca NumPy al principio del archivo, obtendrás un error de NameError indicando que 'np' no está definido. Esto se debe a que 'np' es el alias que asignamos a la biblioteca NumPy durante la importación, y sin esa importación, el programa no reconoce qué es 'np'.