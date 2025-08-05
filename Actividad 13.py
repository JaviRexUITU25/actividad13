students = {}
courses = {}
def hello(): #SALUDO GENERAL
    print("-" * 8 + "BIENVENIDO A GESTION ACADEMICA:" + "-" * 8 + "\n"
          "1. Agregar estudiante.\n"
          "2. Consultar estudiante. \n"
          "3. Calcular promedio de estudiante. \n"
          "4. Verificar estudiante aprobado. \n"
          "5. Mostrar lista de estudiantes. \n"
          "6. Salir.")
def option1(): #SI EL USUARIO QUIERE AGREGAR UN ESTUDIANTE
    print("-" * 10 + "AGREGAR ESTUDIANTE" + "-" * 10)
    try:
        amount = int(input("Ingrese la cantidad de estudiantes que desea ingresar: "))
        for x in range(amount):
            print("=" * 10 + f"Estudiante #{x + 1}"+ "=" * 10)
            idd = input("Ingrese el ID del estudiante: ").upper()
            full_name = input("Ingrese el nombre del estudiante: ")
            major = input("Ingrese la carrera o programa academico del estudiante: ")
            students[idd] = {
                "full_name": full_name,
                "major": major
            }
            print("-"*10 + "¡Estudiante agregado correctamente!"+ "-"*10)
            option2 =input("1. Si\n"                                        #SI EL USUARIO QUIERE AGREGAR EL CURSO Y SU NOTA
                           "2. No\n"
                           "¿Desea agregar un curso y su nota?: ")
            try:
                if option2 == "1":
                    search_id = int(input("Ingrese el ID del estudiante: "))
                    if idd not in students: #por si el estudiante no ha sido registrado
                        print("El estudiante no existe")
                    else:
                        course_a = int(input("Ingrese cuantos cursos desea implementar: ")) #Verificar el numero de cursos
                        for y in range(course_a):
                            print(f"curso #{y + 1}")
                            course_name = input("Ingrese nombre de curso: ")
                            course_note = input("Ingrese nota de curso: ")
                            if course_note <"0":
                                print("La nota debe ser positiva")
                            elif course_note > "100":
                                print("La nota debe ser menor a 100")
                            print("-" * 10 + "¡Curso agregado correctamente!" + "-" * 10)
                            courses[course_name] = {
                                "course_name": course_name,
                                "course_note": course_note
                            }
                elif option2 == "2":  #Por si el usuario no quiere agregar nota
                    continue
            except ValueError:
                print("El valor ingresado no es valido.")
            except TypeError:
                print("El valor ingresado no es valido.")
            except Exception as e:
                print("Un error inesperado ha ocurrido")
    except ValueError:
        print("El valor ingresado no es valido.")
    except TypeError:
        print("El valor ingresado no es valido.")
    except Exception as e:
        print("Un error inesperado ha ocurrido")
def option2(): #CONSULTAR ESTUDIANTE POR CURSO Y ID
    try:
        print("=" * 10 + "CONSULTAR ESTUDIANTE" + "=" * 10)
        search_id2 = input("Ingrese el ID del estudiante: ").upper()
        if search_id2 not in students:
            print("El estudiante no existe")
        else:
            for id2,values in students.items():
                if id2 == search_id2:
                    print(f"ID: {id2}\n"
                          f"Nombre del el estudiante: {values['full_name']}\n"
                          f"Carrera: {values['major']}\n")
                    if not courses:
                        print("Sin cursos asignados")
                    else:
                        for id3, values2 in courses.items():
                            if id3 == search_id2:
                                print(f"Nombre del curso: {values2['course_name']}\n"
                                      f"Nota del curso: {values2['course_note']}\n")
    except ValueError:
        print("El valor ingresado no es valido.")
    except TypeError:
        print("El valor ingresado no es valido.")
    except Exception as e:
        print("Un error inesperado ha ocurrido")
def average():
    try:
        print("=" * 10 + "PROMEDIO DE ESTUDIANTE" + "=" * 10)
        average_search = input("Ingrese el ID del estudiante: ")
        if average_search not in students:
            print("El estudiante no existe")
        else:
            for id3,values in courses.items():
                if id3 == average_search:
                    average_total = courses/len(courses)
    except ValueError:
        print("El valor ingresado no es valido.")
    except TypeError:
        print("El valor ingresado no es valido.")
    except Exception as e:
        print("Un error inesperado ha ocurrido")
def approved():
    try:
        print("=" * 10 + "VERIFICAR SI APRUEBA EL ESTUDIANTE" + "=" * 10)
        approved_search = input("Ingrese el ID del estudiante: ")
        if approved_search not in students:
            print("El estudiante no existe")
        else:
            for id4,values in courses.items():
                if id4 == approved_search:
                    if id4 <"60":
                        print("El estudiante reprobó")
                    elif id4 > "60":
                        print("El estudiante aprobó")
    except ValueError:
        print("El valor ingresado no es valido.")
    except TypeError:
        print("El valor ingresado no es valido.")
    except Exception as e:
        print("Un error inesperado ha ocurrido")
def student_list():
    try:
        print("-"*10 + "MOSTRAR LISTA DE ESTUDIANTES" + "-"*10)
        for id5, values in students.items():
            for id6,values2 in courses.items():
                if id6 == id5:
                    print("Lista de estudiantes: ")


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
                average()
            case 4:
                approved()
            case 5:
                student_list()
            case 6:
                break
            case _:
                print("El valor ingresado no es valido.")
    except ValueError:
        print("El valor ingresado no es valido.")
    except TypeError:
        print("El valor ingresado no es valido.")
    except Exception as e:
        print("Un error inesperado ha ocurrido")