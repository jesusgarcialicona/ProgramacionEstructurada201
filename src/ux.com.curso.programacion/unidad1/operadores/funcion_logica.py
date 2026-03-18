#ejercicio operadores logicos
def operadores():
    a = True
    b = False

    print(a and b)
    print(a or b)
    print(not a)

    numero_1 = 10
    numero_2 = 20

    if numero_1 > numero_2:
        print("El número 1 es mayor que el número 2")
    else:
        print("El número 2 es mayor que el número 1")

def main(): 
    operadores()

if __name__=="__main__":
    main()
