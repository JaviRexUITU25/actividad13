students = {}
courses = {}
def hello():
    print("-" * 8 + "BIENVENIDO A GESTION ACADEMICA:" + "-" * 8 + "\n"
          "1. Agregar estudiante y agregar curso con nota:\n"
          "2. Consultar estudiante: \n"
          "3. Calcular promedio de estudiante: \n"
          "4. Verificar estudiante aprobado: \n"
          "5. Mostrar lista de estudiantes: \n"
          "6. Salir")
def option1():
    print("-" * 10 + "AGREGAR ESTUDIANTE" + "-" * 10)
    amount = int(input("Ingrese la cantidad de estudiantes que desea ingresar: "))
    for x in range(amount):
        print(f"Estudiante #{i + 1}")
        ID = input("Ingrese el ID del estudiante: ")
        full_name = input("Ingrese el nombre del estudiante: ")
        major = input("Ingrese la carrera o programa academico del estudiante: ")
        course_a = int(input("Ingrese cuantos cursos desea implementar: "))
        for y in range(course_a):
            print(f"curso #{y + 1}")
            course_name = input("Ingrese nombre de curso")
            course_note = input("Ingrese nota de curso")
            print("¡Estudiante(s) y curso(s) agregado(s) correctamente!")
            students[ID] = {
                "ID" : ID,
                "Nombre" : full_name,
                "Carrera" : major,
                "Courses" : {
                    "Curso" : course_name,
                    "Nota de curso" : course_note
                }
            }
def student_search():
    print("=" * 10 + "CONSULTAR ESTUDIANTE" + "="*10)
    searching = input("Ingrese ID del estudiante: ")
    if searching in students:
        student = students[searching]
        print("Estudiante encontrado!\n"
              f"Nombre: {student["full_name"]}\n"
              f"Carrera: {student["major"]}\n"
              f"CUrso y nota: {student["Curso"],["Nota de curso"]}")

    hello()
while True:
    option = int(input("Ingrese la opcion que desea ingresar: "))
    try:
        match option:
            case 1:
                option1()
    except ValueError:
        print("Ingrese un numero valido, intente de nuevo.")
    except Exception as e:
        print("Se produjo un error inesperado.")
    else:
            case 2:
                print("-"*10 + "AGREGAR CURSOS Y NOTA"+ "-"* 10)
                total_courses = int(input("Ingrese el total de cursos que desea ingresar: "))
                for i in range(total_courses):
                    print(f"Curso #{i + 1}")
                    ID = input("Ingrese el ID del estudiante: ")
                    if ID in students:
                        curse_name = input("Ingrese el nombre del curso: ")
                        final_note = input("Ingrese la nota final del curso: ")
                        print("Curso y nota agregados correctamente!")
                    else:
                        print("Estudiante no encontrado, intente de nuevo.")
            case 3:
              print("-" * 10 + "CONSULTAR ESTUDIANTE"+ "-"* 10)
              for ID, data in students.items():
                   print("Ingrese ID del estudiante: ")
                   students['ID'] = {
                       'ID': ID,
                   }
            case 4:
               print("-"*10 + "CALCULAR PROMEDIO DE ESTUDIANTE"+ "-"* 10)
            case 5:
               print("-"*10 + "VERIFICAR ESTUDIANTE APROBADO"+ "-"* 10)
            case 6:
               print("-"*10+"LISTA DE ESTUDIANTES"+ "-"* 10)
            case 7:
               print("-"*10 + "SALIR, GRACIAS POR USAR EL PROGRAMA"+ "-"* 10)
               break