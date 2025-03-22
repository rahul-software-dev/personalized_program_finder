from django.db import models

class User(models.Model):
    """Model representing a user of the program finder system."""
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Program(models.Model):
    """Model representing an academic program available for recommendation."""
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    university = models.CharField(max_length=255)
    country = models.CharField(max_length=100)
    field_of_study = models.CharField(max_length=150)
    duration = models.IntegerField(help_text="Duration in years")
    tuition_fees = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    research_opportunities = models.BooleanField(default=False)
    cultural_environment = models.CharField(max_length=255, null=True, blank=True)
    teaching_style = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return f"{self.name} - {self.university}"

class UserPreference(models.Model):
    """Model storing user preferences for personalized recommendations."""
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="preferences")
    preferred_countries = models.JSONField(default=list, help_text="List of preferred countries")
    preferred_fields = models.JSONField(default=list, help_text="List of preferred fields of study")
    career_goals = models.TextField(null=True, blank=True)
    prefers_research = models.BooleanField(default=False)
    preferred_teaching_style = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return f"Preferences of {self.user.name}"

class Recommendation(models.Model):
    """Model storing program recommendations for users."""
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="recommendations")
    program = models.ForeignKey(Program, on_delete=models.CASCADE)
    score = models.FloatField(help_text="Relevance score for recommendation")
    generated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Recommendation for {self.user.name} - {self.program.name}"