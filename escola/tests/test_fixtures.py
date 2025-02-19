from django.test import TestCase
from escola.models import Estudante, Curso

class FixturesTestCase(TestCase):
    fixtures = ['prototipo_banco.json']

    def test_carregamento_da_fixtures(self):
        """teste que verifica o carregamento das fixtures"""
        estudante = Estudante.objects.get(cpf='89291881503')
        curso = Curso.objects.get(pk=1)
        self.assertEqual(estudante.celular,"74 97132-5701")
        self.assertEqual(curso.codigo,"CPOO1")