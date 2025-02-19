from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from django.contrib.auth import authenticate
from django.urls import reverse
from rest_framework import status

class AuthenticationUserTestCase(APITestCase):
    def setUp(self):
        self.usuario = User.objects.create_superuser(username='admin', password='admin')
        self.url = reverse('Estudantes-list')

    def test_autenticacao_user_com_credenciais_corretas(self):
        """teste que verifica a autenticacao do user com as credenciais corretas"""
        usuario = authenticate(username='admin', password='admin')
        self.assertTrue((usuario is not None) and usuario.is_authenticated)

    def test_autenticacao_user_incorretas(self):
        """teste que verifica a autenticacao do user incorreta"""
        usuario = authenticate(username='adn', password='admin')
        self.assertFalse((usuario is not None) and usuario.is_authenticated)

    def test_autenticacao_senha_incorretas(self):
        """teste que verifica a autenticacao com senha incorreta"""
        usuario = authenticate(username='admin', password='adn')
        self.assertFalse((usuario is not None) and usuario.is_authenticated)

    def test_requisicao_get_autorizado(self):
        """teste que verifica requisicao GET autorizada"""
        self.client.force_authenticate(self.usuario)
        response = self.client.get(self.url)
        self.assertEqual(response.status_code,status.HTTP_200_OK)

    def test_requisicao_get_nao_autorizado(self):
        """teste que verifica requisicao GET nao autorizada"""
        response = self.client.get(self.url)
        self.assertEqual(response.status_code,status.HTTP_401_UNAUTHORIZED)
