# Lista inicial con varios datos en tuplas
# Se define una lista de tuplas donde cada tupla contiene (ID, Nombre, Edad)
registros = [
    (1, "Ana", 25),
    (2, "Luis", 30),
    (3, "Carlos", 22)
]

# Función para consultar por nombre
def consultar(nombre):
    """
    Busca registros en la lista cuya persona tenga el nombre dado (sin distinguir mayúsculas/minúsculas).
    :param nombre: Nombre a buscar.
    :return: Lista de tuplas con los registros que coinciden.
    """
    return [registro for registro in registros if registro[1].lower() == nombre.lower()]

# Función para ordenar la lista por clave
def ordenar_por_clave(indice):
    """
    Ordena la lista de registros según el índice de la clave especificada (0: ID, 1: Nombre, 2: Edad).
    :param indice: Índice de la clave por la cual ordenar.
    :return: Lista de tuplas ordenadas.
    """
    return sorted(registros, key=lambda x: x[indice])

# Función para anexar un nuevo registro
def anexar_registro():
    """
    Permite al usuario ingresar un nuevo registro mediante la entrada de datos por teclado.
    """
    id_nuevo = int(input("Ingrese el ID: "))
    nombre_nuevo = input("Ingrese el nombre: ")
    edad_nueva = int(input("Ingrese la edad: "))
    registros.append((id_nuevo, nombre_nuevo, edad_nueva))
    print("Registro agregado exitosamente.")

# Función para almacenar en otra lista los registros mayores a una edad
def filtrar_por_edad(edad_minima):
    """
    Filtra los registros cuya edad sea mayor o igual a la edad mínima especificada.
    :param edad_minima: Edad mínima para filtrar.
    :return: Lista de tuplas con los registros filtrados.
    """
    return [registro for registro in registros if registro[2] >= edad_minima]

# Menú interactivo para el usuario
def menu():
    while True:
        print("\n--- MENÚ ---")
        print("1. Consultar por nombre")
        print("2. Ordenar registros")
        print("3. Agregar nuevo registro")
        print("4. Filtrar por edad")
        print("5. Mostrar registros")
        print("6. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            nombre = input("Ingrese el nombre a consultar: ")
            print("Resultados:", consultar(nombre))
        elif opcion == "2":
            clave = input("Ingrese la clave de ordenamiento (id, nombre, edad): ").lower()
            indice = {"id": 0, "nombre": 1, "edad": 2}.get(clave, -1)
            if indice != -1:
                print("Registros ordenados:", ordenar_por_clave(indice))
            else:
                print("Clave no válida. Intente nuevamente.")
        elif opcion == "3":
            anexar_registro()
        elif opcion == "4":
            edad = int(input("Ingrese la edad mínima para filtrar: "))
            print("Registros filtrados:", filtrar_por_edad(edad))
        elif opcion == "5":
            print("Lista completa de registros:", registros)
        elif opcion == "6":
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

# Ejecutar el menú interactivo
menu()
