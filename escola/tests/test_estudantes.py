from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from escola.models import Estudante
from escola.serializers import EstudanteSerializer

class EstudantesTestCase(APITestCase):
    def setUp(self):
        self.usuario = User.objects.create_superuser(username='admin', password='admin')
        self.url = reverse('Estudantes-list')
        self.client.force_authenticate(user=self.usuario)
        self.estudante_01 = Estudante.objects.create(
            nome = 'Frank Lampard',
            email = 'testeestudante@gmail.com',
            cpf = '00089674820',
            data_nascimento = '1994-10-20',
            celular = '13 99405-2200'

        )

        self.estudante_02 = Estudante.objects.create(
            nome = 'John Terry',
            email = 'testeestudante22@gmail.com',
            cpf = '04650232821',
            data_nascimento = '1994-10-20',
            celular = '13 99405-2200'

        )

    def test_requisicao_get_para_listar_estudantes(self):
        """teste de requisicao GET"""
        response = self.client.get(self.url)
        self.assertEqual(response.status_code,status.HTTP_200_OK)

    def test_requisicao_get_para_listar_um_estudante(self):
        """Teste de requisição GET para um estudante"""
        response = self.client.get(self.url+'1/')
        self.assertEqual(response.status_code,status.HTTP_200_OK)
        dados_estudante = Estudante.objects.get(pk=1)
        dados_estudante_serializados = EstudanteSerializer(instance=dados_estudante).data
        self.assertEqual(response.data,dados_estudante_serializados)
