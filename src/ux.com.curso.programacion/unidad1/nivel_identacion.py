#ejemploo para visualizar la indentacion en python

def explicar_identantacion():
    #nivel 1
    mensaje="nivel 1 de indentacion" 
    print(mensaje)

    puntos=10
  
    if puntos > 9:
        #nivel 2
        print("entra el flujo de if")

        if puntos==10:
            #nivel 3
            print("puntos es igual a 10")

def main():
    explicar_identantacion()

if __name__=="__main__":
    main()
