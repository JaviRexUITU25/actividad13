students = {}
curses = {}
def hello():
    print("-" * 8 + "BIENVENIDO A GESTION ACADEMICA:" + "-" * 8 + "\n"
          "1. Agregar estudiante:\n"
          "2. Agregar curso con nota:  \n"
          "3. Consultar estudiante: \n"
          "4. Calcular promedio de estudiante: \n"
          "5. Verificar estudiante aprobado: \n"
          "6. Mostrar lista de estudiantes: \n"
          "7. Salir")

while True:
    hello()
    option = int(input("Ingrese la opcion que desea ingresar: "))
    try:
        if option == 1:
           print("-" * 10 + "AGREGAR ESTUDIANTE"+ "-"* 10)
           amount = int(input("Ingrese la cantidad de estudiantes que desea ingresar: "))
    except ValueError:
        print("Ingrese un numero valido, intente de nuevo.")
        for i in range(amount):
           print(f"Estudiante #{i + 1}")
           ID = input("Ingrese el ID del estudiante: ")
           full_name = input("Ingrese el nombre del estudiante: ")
           major = input("Ingrese la carrera o programa academico del estudiante: ")
           print("¡Estudiante agregado correctamente!")
        if option == 2:
           print("-"*10 + "AGREGAR CURSOS Y NOTA"+ "-"* 10)
           buscado = input("Ingrese el ID del estudiante: ")
           if buscado in students:
               curse_name = input("Ingrese el nombre del curso: ")
               final_note = input("Ingrese la nota del curso: ")
           else:
                print("Ingrese un ID valido, intente de nuevo.")


