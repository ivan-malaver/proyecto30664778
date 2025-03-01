# Lista inicial con varios datos
# Se define una lista de diccionarios, donde cada diccionario representa un registro con id, nombre y edad.
registros = [
    {"id": 1, "nombre": "Ana", "edad": 25},
    {"id": 2, "nombre": "Luis", "edad": 30},
    {"id": 3, "nombre": "Carlos", "edad": 22}
]

# Función para consultar por nombre
def consultar(nombre):
    """
    Busca registros en la lista cuyo nombre coincida con el parámetro dado (sin distinguir mayúsculas/minúsculas).
    :param nombre: Nombre a buscar.
    :return: Lista con los registros que coinciden.
    """
    return [registro for registro in registros if registro["nombre"].lower() == nombre.lower()]

# Función para ordenar la lista por clave
def ordenar_por_clave(clave):
    """
    Ordena la lista de registros según la clave especificada (por ejemplo, "edad" o "nombre").
    :param clave: Clave por la cual ordenar.
    :return: Lista ordenada.
    """
    return sorted(registros, key=lambda x: x[clave])

# Función para anexar un nuevo registro
def anexar_registro():
    """
    Permite al usuario ingresar un nuevo registro mediante la entrada de datos por teclado.
    """
    id_nuevo = int(input("Ingrese el ID: "))
    nombre_nuevo = input("Ingrese el nombre: ")
    edad_nueva = int(input("Ingrese la edad: "))
    registros.append({"id": id_nuevo, "nombre": nombre_nuevo, "edad": edad_nueva})
    print("Registro agregado exitosamente.")

# Función para almacenar en otra lista los registros mayores a una edad
def filtrar_por_edad(edad_minima):
    """
    Filtra los registros cuya edad sea mayor o igual a la edad mínima especificada.
    :param edad_minima: Edad mínima para filtrar.
    :return: Lista de registros filtrados.
    """
    return [registro for registro in registros if registro["edad"] >= edad_minima]

# Menú interactivo para el usuario
def menu():
    while True:
        print("\n--- MENÚ ---")
        print("1. Consultar por nombre")
        print("2. Ordenar lista")
        print("3. Agregar nuevo registro")
        print("4. Filtrar por edad")
        print("5. Mostrar registros")
        print("6. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            nombre = input("Ingrese el nombre a consultar: ")
            print("Resultados:", consultar(nombre))
        elif opcion == "2":
            clave = input("Ingrese la clave de ordenamiento (id, nombre, edad): ")
            print("Lista ordenada:", ordenar_por_clave(clave))
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