from django.test import TestCase

from flopfarm_admin.models import User
# Create your tests here.

class UserModelTest(TestCase):
    @classmethod
    def setUp(self):
        print("setUpTestData: Run once to set up non-modified data for all class methods.")
        User.objects.create(id=1, username="John", password="123456")
        

    # def setUp(self):
    #     print("setUp: Run once for every test method to setup clean data.")
    #     pass

    def test_user_name(self):
        print("Method: test_user_name.")
        user = User.objects.get(id=1)
        user_name = user.username
        self.assertEqual(user_name, 'John')

    def test_user_password(self):
        print("Method: test_user_password.")
        user = User.objects.get(id=1)
        password = user.password
        self.assertEqual(password, '123456')

    def test_str(self):
        print("Method: test_str.")
        user = User.objects.get(id=1)
        expected = f'{user.id} ({user.username})'
        self.assertEqual(expected, str(user))
