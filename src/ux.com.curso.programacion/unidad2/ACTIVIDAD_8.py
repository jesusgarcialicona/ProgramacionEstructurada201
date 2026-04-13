# Simulador de inicio de sesión
# Lógica basada estrictamente en el diagrama de flujo

intentos = 0
clave_correcta = "1234"

while intentos < 3:
    contrasena = input("Ingrese su clave: ")
    
    if contrasena == clave_correcta:
        print("✅ Acceso Concedido")
        break
    else:
        intentos = intentos + 1
        print(f"❌ Contraseña incorrecta. Intentos restantes: {3 - intentos}")

else:
    print("🔒 Cuenta bloqueada. Ha superado el número máximo de intentos.")