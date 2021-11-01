from django.contrib.auth import authenticate
from django.urls import reverse

from fitness.accounts.models import FitnessUser
from tests.base.mixins import WorkoutTestUtils
from tests.base.tests import FitnessTestCase


class UserTest(WorkoutTestUtils, FitnessTestCase):

    def test_login(self):
        response = self.client.post(reverse('log in'), {'email': 'test@test.com', 'password': '!12test12!'})
        self.assertTemplateUsed(response, 'login.html')
        self.assertEqual(200, response.status_code)

    def test_register(self):
        response = self.client.post(reverse('register'), {'email': 'test@test.com', 'password': '!12test12!'})
        self.assertTemplateUsed(response, 'register_user.html')
        self.assertEqual(200, response.status_code)

    def test_logout(self):
        response = self.client.post(reverse('register'), {'email': 'test@test.com', 'password': '!12test12!'})
        self.assertEqual(200, response.status_code)
