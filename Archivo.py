
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
        for i in range(cantidadMaterias):
            nombreMateria = input(f"Nombre de la materia {i+1}: ")
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

        usuarioEcontrado = None
        
        for usuario in usuarios:
            if usuario["email"] == correoUsuario and usuario["password"] == contraseñaUsuario:
                usuarioEcontrado = usuario
        
        if usuarioEcontrado:
            print(f"\n¡Hola de nuevo, {usuarioEcontrado['nombre']}!")
            
            while True:
                print("\n¿Qué deseas hacer?")
                print("1. Cargar notas (3 por materia)")
                print("2. Ver promedios y reporte")
                print("3. Cerrar sesión")
                
                opcionEstudiante = input("Selecciona una opción: ")
                
                if opcionEstudiante == "1":

                    for nombreMateria in usuarioEcontrado["materias"]:
                        print(f"\nNotas para: {nombreMateria}")
                        listaDeNotas = []

                        for n in range(3):
                            nota = float(input(f"  Ingresa la nota {n+1}: "))
                            listaDeNotas.append(nota)

                        usuarioEcontrado["materias"][nombreMateria] = listaDeNotas
                    print("\n¡Todas las notas han sido cargadas!")