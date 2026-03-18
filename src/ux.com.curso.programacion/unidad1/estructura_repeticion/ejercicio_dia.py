#ejercicio dia python
def dia():
    print("-que dia es hoy?-")
    dia_semana = input("Ingrese un día de la semana (1-7): ")
    match dia_semana.lower():
        case "1":
            print("Dia 1 seleccionado")
            nombre = input("Ingrese su nombre: ")
            print(f"Hola, {nombre}! hoy es lunes")
        case "2":
            print("Dia 2 seleccionado")
            nombre = input("Ingrese su nombre: ")
            print(f"Hola, {nombre}! hoy es martes")
        case "3":
            print("Dia 3 seleccionado")
            nombre = input("Ingrese su nombre: ")
            print(f"Hola, {nombre}! hoy es miércoles")
        case "4":
            print("Dia 4 seleccionado")
            nombre = input("Ingrese su nombre: ")
            print(f"Hola, {nombre}! hoy es jueves")
        case "5":
            print("Dia 5 seleccionado")
            nombre = input("Ingrese su nombre: ")
            print(f"Hola, {nombre}! hoy es viernes")
        case "6":
            print("Dia 6 seleccionado")
            nombre = input("Ingrese su nombre: ")
            print(f"Hola, {nombre}! hoy es sábado")
        case "7":
            print("Dia 7 seleccionado")
            nombre = input("Ingrese su nombre: ")
            print(f"Hola, {nombre}! hoy es domingo")
        case _:
            print("el dia solo tiene 7 dias, ingrese un numero del 1 al 7")


def main():
    dia()

if __name__=="__main__":
    main()