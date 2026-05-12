# --- SISTEMA DE MONITOREO INDUSTRIAL ---
 
def limpiar_dato(lectura_cruda):
	"""
	FUNCIÓN 1: Recibe un string del archivo, lo convierte a float.
	Si el dato es > 100 o < 0, devuelve None (Ruido detectado).
	"""
	try:
		valor = float(lectura_cruda)
		if valor > 100 or valor < 0:
			return None
		return valor
	except ValueError:
		return None
 
 
def calcular_alerta(valor_normalizado):
	"""
	FUNCIÓN 2: Recibe el valor (0.0 a 1.0).
	Devuelve 'CRÍTICO' si es > 0.8, 'PRECAUCIÓN' si es > 0.5,
	y 'NORMAL' en cualquier otro caso.
	"""
	if valor_normalizado > 0.8:
		return 'CRÍTICO'
	elif valor_normalizado > 0.5:
		return 'PRECAUCIÓN'
	else:
		return 'NORMAL'
 
 
def obtener_estadisticas(lista_datos):
	if not lista_datos:
		return (0, 0, 0) 
	
	maximo = max(lista_datos)
	minimo = min(lista_datos)
	promedio = sum(lista_datos) / len(lista_datos)
	return (maximo, minimo, promedio)
 
def generar_reporte(total_datos, validos, estadisticas):
	v_max, v_min, v_prom = estadisticas
	descartados = total_datos - validos
	#implementar aqui
	print("*" * 30)
	print("REPORTE DE ANILISIS PREDECTIVO")
	print("*" * 30)
	print(f"Total de lecturas prcesadas: {total_datos}")
	print(f"Lecturas válidas: {validos}")
	print(f"Lecturas descartadas: {descartados}")
	print(f"Valor máximo: {v_max}")
	print(f"Valor mínimo: {v_min}")
	print(f"Promedio: {v_prom}")
	print("*" * 30)
	print(f"Total de datos: {total_datos}")
	print(f"Datos válidos: {validos}")
	print(f"Máximo: {estadisticas[0]:.2f}")
	print(f"Mínimo: {estadisticas[1]:.2f}")
	print(f"Promedio: {estadisticas[2]:.2f}")
	
import os 
# --- LÓGICA PRINCIPAL (NO MODIFICAR ESTA PARTE) ---
def ejecutar_pipeline():
	datos_finales = []
	cuenta_total = 0

	with open("lecturas_sensores.txt", "r") as f:
		for linea in f:
			cuenta_total += 1
			valor = limpiar_dato(linea.strip())
			if valor is not None:
				# Normalizar para la IA (0-1)
				datos_finales.append(valor / 100)
	if datos_finales:
		stats = obtener_estadisticas(datos_finales)
		generar_reporte(cuenta_total, len(datos_finales), stats)
 
if __name__ == "__main__":
	ejecutar_pipeline()