# Error personalizado para validación de los datos
class ErrorValidacion(Exception):
    pass

class Cliente:
    def __init__(self, id_cliente, nombre, email, telefono):
        self.id_cliente = id_cliente
        self.nombre = nombre
        
        # Validación email: debe contener '@'
        if "@" not in email:
            raise ErrorValidacion(f"¡Atención! El email '{email}' no es válido.")
        self.email = email
        
        self.telefono = telefono

    def __str__(self):
        return f"ID: {self.id_cliente} | Nombre: {self.nombre} | Email: {self.email}"

# Herencia. Cliente Premium es un tipo de cliente pero con beneficios.
class ClientePremium(Cliente):
    def __init__(self, id_cliente, nombre, email, telefono, nivel_beneficios):
        super().__init__(id_cliente, nombre, email, telefono)
        self.nivel_beneficios = nivel_beneficios

    def __str__(self):
        return f"PREMIUM | ID: {self.id_cliente} | Nombre: {self.nombre} | Nivel: {self.nivel_beneficios}"
    
   

# Nuevo tipo de cliente: Corporativo, con un campo adicional para el RUT de la empresa.
class ClienteCorporativo(Cliente):
    def __init__(self, id_cliente, nombre, email, telefono, rut_empresa):
        super().__init__(id_cliente, nombre, email, telefono)
        self.rut_empresa = rut_empresa

    def __str__(self):
        return f" CORPORATIVO | ID: {self.id_cliente} | Empresa: {self.nombre} | RUT: {self.rut_empresa}"
    
