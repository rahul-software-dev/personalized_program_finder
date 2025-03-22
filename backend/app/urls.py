from django.urls import path
from .views import ProgramRecommendationView, UserPreferencesView

urlpatterns = [
    path('recommendations/', ProgramRecommendationView.as_view(), name='get_program_recommendations'),
    path('user/preferences/', UserPreferencesView.as_view(), name='get_or_update_user_preferences'),
]