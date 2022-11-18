from django.test import TestCase
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate


class SignInTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='admintest', password='Admin123@'
        )
        self.user.save()

    def tearDown(self):
        self.user.delete()

    def test_correct(self):
        user = authenticate(username='admintest', password='Admin123@')
        self.assertTrue((user is not None) and user.is_authenticated)

    def test_wrong_username(self):
        user = authenticate(username='wrong', password='12test12')
        self.assertFalse(user is not None and user.is_authenticated)

    def test_wrong_pssword(self):
        user = authenticate(username='test', password='wrong')
        self.assertFalse(user is not None and user.is_authenticated)

