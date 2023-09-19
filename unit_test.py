"""
    Módulo que contiene pruebas para la función de suma y su importación.
"""
import unittest

def suma(num1, num2):
    """
    Suma dos números y devuelve el resultado.

    Args:
        num1 (int): El primer número.
        num2 (int): El segundo número.

    Returns:
        int: La suma de num1 y num2.
    """
    return abs(num1) + num2

class BlackBoxTest(unittest.TestCase):
    """
    Clase que contiene pruebas para la función de suma.
    """

    def test_suma_dos_positivos(self):
        """
        Prueba la función de suma con dos números positivos.
        Verifica que la suma se realice correctamente.

        """
        num_1 = 10
        num_2 = 5
        result = suma(num_1, num_2)
        self.assertEqual(result, 15)

    def test_suma_dos_negativos(self):
        """
        Prueba la función de suma con dos números negativos.
        Verifica que la suma se realice correctamente y dé un resultado negativo.

        """
        num_1 = -10
        num_2 = -7
        result = suma(num_1, num_2)
        self.assertEqual(result, -17)

if __name__ == '__main__':
    unittest.main()
    