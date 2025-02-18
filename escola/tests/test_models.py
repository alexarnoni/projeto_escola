from django.test import TestCase
from escola.models import Estudante

class ModelEstudanteTestCase(TestCase):
    # def teste_falha(self):
    #     self.fail('teste falhou')
    def setUp(self):
        self.estudante = Estudante.objects.create(
            nome = "Teste de Modelo",
            email = "teste@gmail.com",
            cpf = "78432123021",
            data_nascimento = "1994-10-20",
            celular = "13 99999-9999"
        )
    
    def test_verifica_atributo_estudante(self):
        """teste que verifica os atributos de Estudante"""
        self.assertEqual(self.estudante.nome, "Teste de Modelo")
        self.assertEqual(self.estudante.email, "teste@gmail.com")
        self.assertEqual(self.estudante.cpf, "78432123021")
        self.assertEqual(self.estudante.data_nascimento, "1994-10-20")
        self.assertEqual(self.estudante.celular, "13 99999-9999")