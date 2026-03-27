from cliente import Cliente, ClientePremium, ClienteCorporativo, ErrorValidacion
from base_datos import configurar_base_datos, guardar_cliente_bd, guardar_en_json 
from registro import registrar_actividad

print("Iniciando Gestor Inteligente de Clientes")
registrar_actividad("El sistema GIC ha sido iniciado.")
configurar_base_datos()

# Creamos un cliente nuevo.
cliente_empresa = ClienteCorporativo(7, "SIN VUELTAS", "contacto@sinvueltas.cl", "999888777", "76.543.210-K")

print("\nGuardando clientes en la base de datos y JSON...")

try:
    guardar_cliente_bd(cliente_empresa)
    guardar_en_json(cliente_empresa)
    registrar_actividad(f"Se guardó exitosamente al cliente: {cliente_empresa.nombre}")
    
except Exception as e:
    print(f" Hubo un error al guardar: {e}")
    registrar_actividad(f"Errkor al intentar guardar: {e}")