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
def anexar_registro(nuevo_registro):
    """
    Agrega un nuevo registro a la lista de registros.
    :param nuevo_registro: Diccionario con los datos del nuevo registro.
    """
    registros.append(nuevo_registro)

# Función para almacenar en otra lista los registros mayores a una edad
def filtrar_por_edad(edad_minima):
    """
    Filtra los registros cuya edad sea mayor o igual a la edad mínima especificada.
    :param edad_minima: Edad mínima para filtrar.
    :return: Lista de registros filtrados.
    """
    return [registro for registro in registros if registro["edad"] >= edad_minima]

# Ejemplo de uso
# Consultar por nombre "Ana" e imprimir el resultado
print("Consulta por nombre 'Ana':", consultar("Ana"))

# Ordenar la lista por la clave "edad" e imprimir el resultado
print("Lista ordenada por edad:", ordenar_por_clave("edad"))

# Anexar un nuevo registro con id 4 y nombre "Elena"
anexar_registro({"id": 4, "nombre": "Elena", "edad": 28})

# Imprimir la lista con el nuevo registro
print("Lista con nuevo registro:", registros)

# Filtrar registros con edad mayor o igual a 25 e imprimir el resultado
lista_filtrada = filtrar_por_edad(25)
print("Lista con edad mayor o igual a 25:", lista_filtrada)