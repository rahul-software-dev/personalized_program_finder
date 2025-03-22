from django.test import TestCase
from ..app.models import User, Program, Preferences

class ModelTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create(username="testuser", email="test@example.com")
        cls.program = Program.objects.create(name="AI Program", location="Germany", duration=24)
        cls.preferences = Preferences.objects.create(user=cls.user, preferred_location="Germany")

    def test_user_creation(self):
        self.assertEqual(str(self.user), "testuser")
        self.assertEqual(self.user.email, "test@example.com")

    def test_program_creation(self):
        self.assertEqual(str(self.program), "AI Program")
        self.assertEqual(self.program.duration, 24)

    def test_preferences_creation(self):
        self.assertEqual(self.preferences.user, self.user)
        self.assertEqual(self.preferences.preferred_location, "Germany")