import unittest
from src.cpf_validator import validar_cpf

class TestCPFValidator(unittest.TestCase):
    def test_cpfs_validos(self):
        self.assertTrue(validar_cpf("529.982.247-25"))
        self.assertTrue(validar_cpf("134.078.437-06"))

    def test_cpfs_invalidos(self):
        self.assertFalse(validar_cpf("123.456.789-09"))
        self.assertFalse(validar_cpf("111.111.111-11"))
        self.assertFalse(validar_cpf("00000000000"))
        self.assertFalse(validar_cpf("52998224724"))

    def test_cpf_vazio(self):
        self.assertFalse(validar_cpf(""))

    def test_cpf_nulo(self):
        self.assertFalse(validar_cpf(None))

if __name__ == "__main__":
    unittest.main()