    #impelementacion de match en python
def demostacion():
    print("-ejemplo de match__")
    opcion = input("Ingrese una opción (1-3): ")
    match opcion:
        case "1":
            print("Opción 1 seleccionada")
            nombre = input("Ingrese su nombre: ")
            print(f"Hola, {nombre}!")
        case "2":
            print("Opción 2 seleccionada")
            numero = int(input("Ingrese un matricula: "))
            print(f"su matricula es: {numero}")
        case "3":
            print("Opción 3 seleccionada")
            semestre = input("Ingrese su semestre: ")
            print(f"usted esta en el semestre: {semestre}")
        case _:
            print("Opción no válida")

def main():
    demostacion()

if __name__=="__main__":
    main()