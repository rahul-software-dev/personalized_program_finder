from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from ..app.models import User, Program

class ViewTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.client = APIClient()
        cls.user = User.objects.create(username="testuser", email="test@example.com")
        cls.program = Program.objects.create(name="AI Program", location="Germany", duration=24)

    def test_get_programs(self):
        response = self.client.get(reverse('program-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(len(response.json()) > 0)

    def test_get_program_detail(self):
        response = self.client.get(reverse('program-detail', kwargs={'pk': self.program.id}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()["name"], "AI Program")

    def test_post_program_unauthorized(self):
        response = self.client.post(reverse('program-list'), {"name": "New Program", "location": "USA"}, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_invalid_program_request(self):
        response = self.client.get(reverse('program-detail', kwargs={'pk': 9999}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)