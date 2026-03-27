import unittest
from cliente import Cliente, ErrorValidacion

class TestGestionClientes(unittest.TestCase):

    # Prueba 1: Verificar que un cliente válido se crea sin problemas
    def test_cliente_valido(self):
        try:
            c = Cliente(100, "Diego", "diego@mail.com", "555")
            self.assertEqual(c.nombre, "Diego")
        except ErrorValidacion:
            self.fail("ErrorValidacion se lanzó con un email que sí era válido")

    # Prueba 2: Verificar si el sistema detecta un error de email
    def test_email_invalido(self):
        with self.assertRaises(ErrorValidacion):
            Cliente(101, "Falla", "correo-sin-arroba.com", "000")

if __name__ == "__main__":
    unittest.main()