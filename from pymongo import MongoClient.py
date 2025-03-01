from pymongo import MongoClient

# Conectar con MongoDB utilizando la URI proporcionada
cliente = MongoClient("mongodb+srv://malaver6:xukBwQpxIQ2yk231@cluster0.svafc.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
base_datos = cliente["startup_log_db"]  # Reemplazar con el nombre real de la base de datos
coleccion = base_datos["startup_log"]  # Nombre de la colección corregido

# Función para consultar por hostname
def consultar_por_hostname(hostname):
    return list(coleccion.find({"hostname": hostname}))

# Función para ordenar la lista por clave
def ordenar_por_clave(clave):
    if clave == "cmdLine.pid":
        return list(coleccion.find({"cmdLine.pid": {"$exists": True}}).sort("cmdLine.pid", 1))
    return list(coleccion.find().sort(clave, 1))

# Función para anexar un nuevo registro
def anexar_registro():
    try:
        id_nuevo = input("Ingrese el _id: ").strip()
        if coleccion.find_one({"_id": id_nuevo}):
            print("Error: _id ya existe en la base de datos.")
            return
        
        hostname_nuevo = input("Ingrese el hostname: ").strip()
        start_time = input("Ingrese el startTime (YYYY-MM-DDTHH:MM:SS): ").strip()
        start_time_local = input("Ingrese el startTimeLocal: ").strip()
        
        try:
            pid_nuevo = int(input("Ingrese el pid: ").strip())
        except ValueError:
            print("Error: El PID debe ser un número entero.")
            return
        
        nuevo_registro = {
            "_id": id_nuevo,
            "hostname": hostname_nuevo,
            "startTime": start_time,
            "startTimeLocal": start_time_local,
            "cmdLine": {"pid": pid_nuevo},
            "buildinfo": {}
        }
        coleccion.insert_one(nuevo_registro)
        print("Registro agregado exitosamente.")
    except Exception as e:
        print(f"Error al agregar registro: {e}")

# Función para filtrar registros con un PID mayor o igual al especificado
def filtrar_por_pid(pid_minimo):
    return list(coleccion.find({"cmdLine.pid": {"$gte": pid_minimo}}))

# Función para mostrar registros
def mostrar_registros(registros):
    if not registros:
        print("No se encontraron registros.")
        return
    for registro in registros:
        print("\n--- Registro ---")
        for clave, valor in registro.items():
            print(f"{clave}: {valor}")

# Menú interactivo
def menu():
    while True:
        print("\n--- MENÚ ---")
        print("1. Consultar por hostname")
        print("2. Ordenar registros")
        print("3. Agregar nuevo registro")
        print("4. Filtrar por PID")
        print("5. Mostrar registros")
        print("6. Salir")
        
        opcion = input("Seleccione una opción: ").strip()
        
        if opcion == "1":
            hostname = input("Ingrese el hostname a consultar: ").strip()
            mostrar_registros(consultar_por_hostname(hostname))
        elif opcion == "2":
            clave = input("Ingrese la clave de ordenamiento (_id, hostname, startTime, cmdLine.pid): ").strip()
            if clave in ["_id", "hostname", "startTime", "cmdLine.pid"]:
                mostrar_registros(ordenar_por_clave(clave))
            else:
                print("Clave no válida. Intente nuevamente.")
        elif opcion == "3":
            anexar_registro()
        elif opcion == "4":
            try:
                pid = int(input("Ingrese el PID mínimo para filtrar: ").strip())
                mostrar_registros(filtrar_por_pid(pid))
            except ValueError:
                print("Error: El PID debe ser un número entero.")
        elif opcion == "5":
            mostrar_registros(list(coleccion.find()))
        elif opcion == "6":
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

# Ejecutar el menú
menu()
