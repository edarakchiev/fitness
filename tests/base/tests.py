from django.test import TestCase, Client


from django.contrib.auth import get_user_model

UserModel = get_user_model()


class FitnessTestCase(TestCase):
    logged_in_email = 'emo@darakchiev.com'
    logged_in_password = '123qwe'

    def assertListEmpty(self, ll):
        return self.assertListEqual([], ll, 'The list not empty')

    def setUp(self) -> None:
        self.client = Client()
        self.user = UserModel.objects.create_user(
            email=self.logged_in_email,
            password=self.logged_in_password,
        )