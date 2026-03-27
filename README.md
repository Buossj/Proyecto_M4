## Gestor Inteligente de Clientes

Sistema de gestión de cartera de clientes desarrollado íntegramente en Python. Este proyecto aplica los fundamentos de la Programación Orientada a Objetos (POO) para ofrecer una solución robusta y escalabe.
## Características Principales

* **Arquitectura POO:** Implementación de herencia y polimorfismo para clasificar usuarios (Cliente Regular, Premium y Corporativo).
* **Persistencia Doble:** Almacenamiento local mediante base de datos **SQLite** (evitando duplicidad de IDs) y generación automática de respaldos en **JSON**.
* **Interfaz Gráfica (GUI):** Ventana interactiva desarrollada con la librería nativa **Tkinter** para facilitar el ingreso de datos.
* **Testing:** Pruebas unitarias integradas (unittest) para garantizar la correcta validación de correos electrónicos.

El sistema permite gestionar desde clientes individuales hasta cuentas corporativas complejas (ej. registro de empresas y e-commerce locales como "SIN VUELTAS" asociando su respectivo RUT y nivel de beneficios).

## Tecnologías Utilizadas
* Python 3.x
* Tkinter (GUI)
* SQLite3 (Base de Datos)
*JSON (backups)
