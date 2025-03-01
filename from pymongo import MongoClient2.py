from pymongo import MongoClient

# URI de conexión
uri = "mongodb+srv://malaver6:xukBwQpxIQ2yk231@cluster0.svafc.mongodb.net/?retryWrites=true&w=majority"

try:
    # Conectar al cliente de MongoDB
    cliente = MongoClient(uri)
    
    # Listar las bases de datos disponibles
    bases_datos = cliente.list_database_names()
    
    print("✅ Conexión exitosa. Bases de datos disponibles:")
    print(bases_datos)

except Exception as e:
    print(f"❌ Error de conexión: {e}")
