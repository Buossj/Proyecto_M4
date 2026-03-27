import tkinter as tk
from tkinter import messagebox # Para mostrar ventanitas de alerta o éxito

from cliente import Cliente, ErrorValidacion
from base_datos import configurar_base_datos, guardar_cliente_bd, guardar_en_json
from registro import registrar_actividad

configurar_base_datos()

# Esta función se ejecuta cuando el usuario hace clic en el botón "Guardar"
def guardar_desde_interfaz():
    # 1. Obtenemos el texto de las cajas de la pantalla
    id_texto = entrada_id.get()
    nombre = entrada_nombre.get()
    email = entrada_email.get()
    telefono = entrada_telefono.get()

    try:
        # 2. Convertimos el ID a número entero
        id_num = int(id_texto)
        
        # 3. Creamos el objeto Cliente 
        nuevo_cliente = Cliente(id_num, nombre, email, telefono)
        
        # 4. Guardamos en SQLite y en JSON
        guardar_cliente_bd(nuevo_cliente)
        guardar_en_json(nuevo_cliente)
        
        # 5. Anotamos en el historial
        registrar_actividad(f"Guardado desde GUI: {nombre} (ID: {id_num})")
        
        # 6. mensaje de confirmación del guardado
        messagebox.showinfo(f"Cliente {nombre} guardado correctamente!")
        
        # 7. Limpiamos las cajas para el siguiente cliente
        entrada_id.delete(0, tk.END)
        entrada_nombre.delete(0, tk.END)
        entrada_email.delete(0, tk.END)
        entrada_telefono.delete(0, tk.END)

    except ValueError:
        messagebox.showerror("Error", "El ID debe ser un número entero.")
    except ErrorValidacion as e:
        messagebox.showerror("Error de Email", str(e))
    except Exception as e:
        messagebox.showerror("Error de Base de Datos", "Ese ID ya existe o hubo un error.")


# --- Diseño ventana visual ---

ventana = tk.Tk()
ventana.title("Gestor Inteligente de Clientes (GIC)")
ventana.geometry("300x400") # Tamaño de la ventana


tk.Label(ventana, text="Nuevo Cliente", font=("Arial", 14, "bold")).pack(pady=10)
# Cajas de texto
tk.Label(ventana, text="ID del Cliente (Número):").pack()
entrada_id = tk.Entry(ventana)
entrada_id.pack(pady=5)

tk.Label(ventana, text="Nombre:").pack()
entrada_nombre = tk.Entry(ventana)
entrada_nombre.pack(pady=5)

tk.Label(ventana, text="Email (Debe contener @):").pack()
entrada_email = tk.Entry(ventana)
entrada_email.pack(pady=5)

tk.Label(ventana, text="Teléfono:").pack()
entrada_telefono = tk.Entry(ventana)
entrada_telefono.pack(pady=5)

boton_guardar = tk.Button(ventana, text="Guardar Cliente", command=guardar_desde_interfaz)
boton_guardar.pack(pady=20)

# Mantiene la ventana abierta y funcionando
ventana.mainloop()