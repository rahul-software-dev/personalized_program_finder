"""
This package contains algorithms for personalized program recommendations.

Modules:
- preference_matching.py: Matches programs based on user preferences.
- career_alignment.py: Aligns programs with user career goals.
- cultural_fit.py: Evaluates cultural compatibility between users and programs.
- teaching_style.py: Matches programs based on teaching styles.
"""

from .preference_matching import match_programs_based_on_preferences
from .career_alignment import align_programs_with_career_goals
from .cultural_fit import evaluate_cultural_fit
from .teaching_style import match_teaching_styles