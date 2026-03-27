import sqlite3
import json

def configurar_base_datos():
    conexion = sqlite3.connect("clientes.db")
    cursor = conexion.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS clientes (
            id_cliente INTEGER PRIMARY KEY,
            nombre TEXT,
            email TEXT,
            telefono TEXT
        )
    ''')
    conexion.commit()
    conexion.close()

def guardar_cliente_bd(cliente):
    conexion = sqlite3.connect("clientes.db")
    cursor = conexion.cursor()
    cursor.execute(
        "INSERT INTO clientes (id_cliente, nombre, email, telefono) VALUES (?, ?, ?, ?)",
        (cliente.id_cliente, cliente.nombre, cliente.email, cliente.telefono)
    )
    conexion.commit()
    conexion.close()
    print(f"El cliente {cliente.nombre} ha sido guardado en la base de datos satisfactoriamente.")

def guardar_en_json(cliente):
    datos_cliente = {
        "id_cliente": cliente.id_cliente,
        "nombre": cliente.nombre,
        "email": cliente.email,
        "telefono": cliente.telefono
    }
    with open("clientes.json", "a") as archivo:
        texto_json = json.dumps(datos_cliente)
        archivo.write(texto_json + "\n")
    print(f" Respaldo ha sido guardado con éxito para: {cliente.nombre}")