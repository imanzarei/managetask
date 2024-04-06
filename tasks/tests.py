from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.test import APIClient


class TaskViewsTestCase(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='test_user', password='test_password')
        self.client = APIClient()

    def perform_authentication(self):
        self.client.force_login(self.user)

    def test_task_list(self):
        self.perform_authentication()
        response = self.client.get('/list/')
        self.assertEqual(response.status_code, 200)

    def test_create_task(self):
        self.perform_authentication()
        data = {
            'title': 'Task Title',
            'description': 'Task Description',
            'created_by': self.user.id
        }
        response = self.client.post('/create/', data, format='json')
        self.assertEqual(response.status_code, 201)
