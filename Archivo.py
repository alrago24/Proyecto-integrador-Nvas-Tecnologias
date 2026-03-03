
usuarios = []

print("--- BIENVENIDO A EDUPERFORMANCE ---")


while True:
    print("\nMenú Inicial:")
    print("1- Registrarse")
    print("2- Iniciar Sesión")
    print("3- Salir")
    
    opcion = input("Elija una opción: ")

    if opcion == "1":
        print("\n--- Registro ---")
        nombre = input("Ingresa tu nombre: ")
        correo = input("Ingresa tu correo electrónico: ")
        contraseña = input("Ingresa una contraseña: ")
        

        cantidadMaterias = int(input("¿Cuántas materias vas a ver?: "))
        
        materiasUsuario = {}
        for int in range(cantidadMaterias):
            nombreMateria = input(f"Nombre de la materia {int+1}: ")
            materiasUsuario[nombreMateria] = []
            
        nuevoUsuario = {
            "nombre": nombre,
            "email": correo,
            "password": contraseña,
            "materias": materiasUsuario
        }
        usuarios.append(nuevoUsuario)
        print("¡Registro completado con éxito!")

    elif opcion == "2":
        print("\nIniciar de sesión")
        correoUsuario = input("Ingresa tu correo registrado: ")
        contraseñaUsuario = input("Ingresa tu contraseña: ")

