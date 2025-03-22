from rest_framework import serializers
from .models import User, Program, UserPreference, Recommendation

class UserSerializer(serializers.ModelSerializer):
    """Serializer for User model."""

    class Meta:
        model = User
        fields = ['id', 'name', 'email', 'created_at']

class ProgramSerializer(serializers.ModelSerializer):
    """Serializer for Program model."""

    class Meta:
        model = Program
        fields = [
            'id', 'name', 'university', 'country', 'field_of_study', 'duration',
            'tuition_fees', 'research_opportunities', 'cultural_environment', 'teaching_style'
        ]

class UserPreferenceSerializer(serializers.ModelSerializer):
    """Serializer for User preferences, including preferred countries and fields."""

    class Meta:
        model = UserPreference
        fields = ['user', 'preferred_countries', 'preferred_fields', 'career_goals', 
                  'prefers_research', 'preferred_teaching_style']

class RecommendationSerializer(serializers.ModelSerializer):
    """Serializer for program recommendations with scores."""

    user = UserSerializer(read_only=True)
    program = ProgramSerializer(read_only=True)

    class Meta:
        model = Recommendation
        fields = ['user', 'program', 'score', 'generated_at']