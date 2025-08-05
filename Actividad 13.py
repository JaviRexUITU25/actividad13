students = {'1': {'full_name': 'jaavi', 'major': 'sistemas'}}
courses = {"1":{'preca': 70, 'jiji': 90}}
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
            courses[idd] = {}
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
                            if "0" > course_note > "100":
                                print("Ingrese una nota valida")
                            print("-" * 10 + "¡Curso agregado correctamente!" + "-" * 10)
                            courses[idd][course_name] = int(course_note)
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
    print(students)
    print(courses)
def average():                               #promedio total de notas
    try:
        print("=" * 10 + "PROMEDIO DE ESTUDIANTE" + "=" * 10)
        average_search = input("Ingrese el ID del estudiante: ")
        if average_search not in students:
            print("El estudiante no existe")
        else:
            suma = 0
            longitud = 0
            for id3,values in students.items():
                if id3 == average_search:
                    print(f"PROMEDIO GENERAL DE: {values['full_name']}\n") #MUESTRA EL PROMEDIO DEL ESTUDIANTE
                    longitud = len(courses[id3])
                    for s in courses[id3].values():
                        suma += s
            print(f"{suma/longitud}") #PROMEDIO TOTAL
    except ValueError:
        print("Debe ser un numero.")
    except TypeError:
        print("El valor ingresado no es valido.")
    except Exception as e:
        print("Un error inesperado ha ocurrido",e)
def approved(): #VERIFICAR SI EL ESTUDIANTE APROBÓ
    try:
        print("=" * 10 + "VERIFICAR SI APRUEBA EL ESTUDIANTE" + "=" * 10)
        approved_search = input("Ingrese el ID del estudiante: ").upper()
        if approved_search not in students:
            print("El estudiante no existe")
        else:
            for id4,values in courses.items():
                if id4 == approved_search:
                    if id4 <"60":
                        print("El estudiante reprobó")
                    elif id4 > "61":
                        print("El estudiante aprobó")
    except ValueError:
        print("Debe ser un numero.")
    except TypeError:
        print("El valor ingresado no es valido.")
    except Exception as e:
        print("Un error inesperado ha ocurrido")
def student_list(): #LISTA DE TODOS LOS ESTUDIANTES
    try:
        print("-"*10 + "MOSTRAR LISTA DE ESTUDIANTES" + "-"*10)
        for id5, values in students.items():
            print(f"ID: {id5}\n"
                  f"Nombre del estudiante: {values['full_name']}\n"
                  f"Carrera: {values['major']}\n")
            print(f"{courses[id5]}")
    except ValueError:
        print("El valor ingresado no es valido.")
    except TypeError:
        print("El valor ingresado no es valido.")
    except Exception as e:
        print("Un error inesperado ha ocurrido")
while True: #DONDE SE EJECUTA EL PROGRAMA
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
                print("-"*10 + "Saliendo del programa." +"-"*10)
                break
            case _:
                print("El valor ingresado no es valido.")
    except ValueError:
        print("Debe ser un numero.")
    except TypeError:
        print("Ingrese un valor valido.")
    except Exception as e:
        print("Un error inesperado ha ocurrido.")