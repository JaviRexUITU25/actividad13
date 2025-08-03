students = {}
curses = {}
while True:
    print("-"*8 + "BIENVENIDO A GESTION ACADEMICA:" + "-" *8 + "\n"
          "1. Agregar estudiante:\n"
          "2. Agregar curso con nota:  \n"
          "3. Consultar estudiante: \n"
          "4. Calcular promedio de estudiante: \n"
          "5. Verificar estudiante aprobado: \n"
          "6. Mostrar lista de estudiantes: \n"
          "7. Salir")
    option = int(input("Ingrese la opcion que desea ingresar: "))
    if option == 1:
       print("-" * 8 + "AGREGAR ESTUDIANTE"+ "-"*8)
       amount = int(input("Ingrese la cantidad de estudiantes que desea ingresar: "))
       for i in range(amount):
           print(f"Estudiante #{i + 1}")
           ID = input("Ingrese el ID del estudiante: ")
           full_name = input("Ingrese el nombre del estudiante: ")
           major = input("Ingrese la carrera o programa academico del estudiante: ")
           print("¡Estudiante agregado correctamente!")

