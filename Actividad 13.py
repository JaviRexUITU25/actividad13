students = {}
courses = {}
def hello():
    print("-" * 8 + "BIENVENIDO A GESTION ACADEMICA:" + "-" * 8 + "\n"
          "1. Agregar estudiante.\n"
          "2. Agregar curso con nota.\n"
          "3. Consultar estudiante. \n"
          "4. Calcular promedio de estudiante. \n"
          "5. Verificar estudiante aprobado. \n"
          "6. Mostrar lista de estudiantes. \n"
          "7. Salir.")
def option1():
    print("-" * 10 + "AGREGAR ESTUDIANTE" + "-" * 10)
    try:
        amount = int(input("Ingrese la cantidad de estudiantes que desea ingresar: "))
        for x in range(amount):
            print("=" * 10 + f"Estudiante #{x + 1}"+ "=" * 10)
            ID = input("Ingrese el ID del estudiante: ").upper()
            full_name = input("Ingrese el nombre del estudiante: ")
            major = input("Ingrese la carrera o programa academico del estudiante: ")
            print("¡Estudiante agregado correctamente!")
    except ValueError:
        print("El valor ingresado no es valido.")
    except TypeError:
        print("El valor ingresado no es valido.")
    except Exception as e:
        print("Un error inesperado ha ocurrido")
def option2():
    try:
        course_a = int(input("Ingrese cuantos cursos desea implementar: "))
        for y in range(course_a):
            print(f"curso #{y + 1}")
            course_name = input("Ingrese nombre de curso: ")
            course_note = input("Ingrese nota de curso: ")
            print("-"*10 + "¡Curso agregado correctamente!" + "-"*10)
    except ValueError:
        print("El valor ingresado no es valido.")
    except TypeError:
        print("El valor ingresado no es valido.")
    except Exception as e:
        print("Un error inesperado ha ocurrido")
def student_search():
    print("=" * 10 + "CONSULTAR ESTUDIANTE" + "="*10)
    searching = input("Ingrese ID del estudiante: ")
    if searching in students:
        student = students[searching]
        print("Estudiante encontrado!\n"
              f"Nombre: {student["full_name"]}\n"
              f"Carrera: {student["major"]}\n"
              f"CUrso y nota: {student["Curso"],["Nota de curso"]}")
    else:
        print("Estudiante no encontrado")
while True:
    hello()
    option = int(input("Ingrese la opcion que desea ingresar: "))
    try:
        match option:
            case 1:
                option1()
            case 2:
                option2()
            case 3:
                student_search()
            case _:
                print("Opcion incorrecta")
    except ValueError:
        print("El valor ingresado no es valido.")

'''def student_average():
    print("="*10 + "PROMEDIO DE NOTAS" + "="*10)
    average_search = input("Ingrese ID de estudiande: ")
    if average_search in students:
        average = course_notes// len(courses)
    hello()
def aprove_student():'''