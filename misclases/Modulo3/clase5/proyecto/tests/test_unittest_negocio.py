import sys
import os

# Fijar ruta firecta de lógica de negocio 
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from negocio import VendedorBase, VendedorPremium
import unittest

class TestVendedor(unittest.TestCase):
    def setUp(self):
        self.vendedor_base  = VendedorBase('Luis', 1000) # Comision  = 100.0
        self.vendedor_premium = VendedorPremium('Carlos', 2000) # Comisión = 300.0

    def test_calcular_comision_base(self):
        self.assertEqual(self.vendedor_base.calcular_comision(), 100.0)

    def test_calcular_comision_premium(self):
        self.assertEqual(self.vendedor_premium.calcular_comision(), 300.0)

if __name__ == '__main__':
    unittest.main()
    
# ejecutar el test
#python -m unittest discover -s tests