from django.test import TestCase
from ..app.models import Program, Preferences, User
from ..app.algorithms.preference_matching import match_preferences
from ..app.algorithms.career_alignment import align_with_career_goals
from ..app.algorithms.cultural_fit import assess_cultural_compatibility
from ..app.algorithms.teaching_style import match_teaching_style

class AlgorithmTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create(username="testuser", email="test@example.com")
        cls.preferences = Preferences.objects.create(user=cls.user, preferred_location="Germany")
        cls.program1 = Program.objects.create(name="AI Program", location="Germany", duration=24)
        cls.program2 = Program.objects.create(name="Data Science Program", location="USA", duration=18)

    def test_preference_matching(self):
        results = match_preferences(self.user, self.preferences)
        self.assertGreaterEqual(len(results), 1)
        self.assertIn(self.program1, results)

    def test_career_alignment(self):
        results = align_with_career_goals(self.user, self.preferences)
        self.assertIsInstance(results, list)

    def test_cultural_fit(self):
        results = assess_cultural_compatibility(self.user, self.preferences)
        self.assertIsInstance(results, list)

    def test_teaching_style_matching(self):
        results = match_teaching_style(self.user, self.preferences)
        self.assertIsInstance(results, list)

    def test_no_matching_programs(self):
        empty_preferences = Preferences.objects.create(user=self.user, preferred_location="Unknown")
        results = match_preferences(self.user, empty_preferences)
        self.assertEqual(len(results), 0)