import datetime

def registrar_actividad(mensaje):
    # 1. Obtenemos la fecha y hora actual de tu computador
    ahora = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # 2. Abrimos (o creamos) un archivo de texto llamado historial.txt
    # La 'a' significa "append" (agregar al final sin borrar lo anterior)
    with open("historial.txt", "a", encoding="utf-8") as archivo:
        archivo.write(f"[{ahora}] {mensaje}\n")