from django.test import TestCase

from flopfarm_admin.models import User
from flopfarm_admin.models import EdgeProvider
from flopfarm_admin.models import Instance
# Create your tests here.

class UserModelTest(TestCase):
    @classmethod
    def setUp(self):
        print("setUpTestData: Run once to set up non-modified data for all class methods.")
        User.objects.create(id=1, username="John", password="123456")

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


class UserEdgeTest(TestCase):
    @classmethod
    def setUp(self):
        print("setUpTestData: Run once to set up non-modified data for all class methods.")
        EdgeProvider.objects.create(id=1, username="John", password="123456")

    def test_user_name(self):
        print("Method: test_user_name.")
        user = EdgeProvider.objects.get(id=1)
        user_name = user.username
        self.assertEqual(user_name, 'John')

    def test_user_password(self):
        print("Method: test_user_password.")
        user = EdgeProvider.objects.get(id=1)
        password = user.password
        self.assertEqual(password, '123456')

    def test_str(self):
        print("Method: test_str.")
        user = EdgeProvider.objects.get(id=1)
        expected = f'{user.id} ({user.username})'
        self.assertEqual(expected, str(user))



class InstanceTest(TestCase):
    @classmethod
    def setUp(self):
        Instance.objects.create(id=1, name="EC2", type="c", status="a", provider=EdgeProvider.objects.create(id=1, username="John"), user=User.objects.create(id=1, username="Ben"))

    def test_type(self):
        instance = Instance.objects.get(id=1)
        self.assertEqual(instance.get_type_display(), "General Computing Instance")

    def test_status(self):
        instance = Instance.objects.get(id=1)
        self.assertEqual(instance.get_status_display(), "Available")

    def test_foreign_key_user(self):
        instance = Instance.objects.get(id=1)
        user = User.objects.get(id=1)
        self.assertEqual(instance.user, user)

    def test_foreign_key_provider(self):
        instance = Instance.objects.get(id=1)
        provider = EdgeProvider.objects.get(id=1)
        self.assertEqual(instance.provider, provider)


    def test_str(self):
        instance = Instance.objects.get(id=1)
        expected = f'{instance.name}'
        self.assertEqual(expected, str(instance))
