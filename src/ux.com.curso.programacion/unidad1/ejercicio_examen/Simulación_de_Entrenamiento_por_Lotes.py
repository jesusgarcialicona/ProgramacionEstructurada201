LIMITE_VRAM_MB = 2500
 
def main():
    print("=" * 55)
    print("   SIMULADOR DE ENTRENAMIENTO POR LOTES (VRAM)")
    print("=" * 55)
    print(f"   Límite de seguridad: {LIMITE_VRAM_MB} MB\n")
 
    total_vram = 0
    lote_num   = 0
 
    while True:
        lote_num += 1
        print(f"--- Lote #{lote_num} ---")
 
        # Entrada validada: el lote debe ser un número positivo
        while True:
            try:
                lote_mb = float(input("  Ingrese el tamaño del lote (MB): "))
                if lote_mb <= 0:
                    print("  [!] El tamaño debe ser mayor que 0. Intente de nuevo.")
                    continue
                break
            except ValueError:
                print("  [!] Entrada inválida. Ingrese un número.")
 
        # Acumular carga
        total_vram += lote_mb
 
        print(f"  Lote cargado   : {lote_mb:.2f} MB")
        print(f"  VRAM acumulada : {total_vram:.2f} MB")
 
        # Verificar límite de seguridad
        if total_vram > LIMITE_VRAM_MB:
            print()
            print(" [!] Límite de VRAM excedido.")
            print(f"Consumo {total_vram:.2f} MB supera {LIMITE_VRAM_MB} MB")
            print("Proceso detenido para proteger VRAM")
            break
 
        restante = LIMITE_VRAM_MB - total_vram
        print(f"  Memoria disponible: {restante:.2f} MB\n")
 
 
if __name__ == "__main__":
    main()