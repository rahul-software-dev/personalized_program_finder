from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from django.shortcuts import get_object_or_404
from .models import User, Program, UserPreference, Recommendation
from .serializers import UserSerializer, ProgramSerializer, UserPreferenceSerializer, RecommendationSerializer
from .algorithms.preference_matching import match_programs_based_on_preferences

class UserViewSet(viewsets.ModelViewSet):
    """API endpoint for managing users."""
    queryset = User.objects.all()
    serializer_class = UserSerializer

class ProgramViewSet(viewsets.ModelViewSet):
    """API endpoint for retrieving available academic programs."""
    queryset = Program.objects.all()
    serializer_class = ProgramSerializer

class UserPreferenceViewSet(viewsets.ModelViewSet):
    """API endpoint for user preferences related to program recommendations."""
    queryset = UserPreference.objects.all()
    serializer_class = UserPreferenceSerializer

    @action(detail=True, methods=['get'])
    def recommendations(self, request, pk=None):
        """Generate personalized program recommendations for a user."""
        user = get_object_or_404(User, pk=pk)
        preferences = get_object_or_404(UserPreference, user=user)

        recommended_programs = match_programs_based_on_preferences(user, preferences)

        # Store recommendations in the database
        recommendations = [
            Recommendation(user=user, program=program['program'], score=program['score'])
            for program in recommended_programs
        ]
        Recommendation.objects.bulk_create(recommendations)

        serializer = RecommendationSerializer(recommendations, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class RecommendationViewSet(viewsets.ModelViewSet):
    """API endpoint for retrieving previous program recommendations."""
    queryset = Recommendation.objects.all()
    serializer_class = RecommendationSerializer

    def list(self, request, *args, **kwargs):
        """List recommendations for a specific user if provided in query params."""
        user_id = request.query_params.get('user')
        if user_id:
            recommendations = Recommendation.objects.filter(user_id=user_id).order_by('-score')
            serializer = self.get_serializer(recommendations, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return super().list(request, *args, **kwargs)