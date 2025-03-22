from flask import Flask
from django.apps import AppConfig
from .models import *  # Import models to ensure they are registered
from .views import *  # Import views to register API endpoints

class ProgramFinderConfig(AppConfig):
    """Django App Configuration for the Personalized Program Finder backend."""
    default_auto_field = "django.db.models.BigAutoField"
    name = "app"

def create_app():
    """Factory function to create and configure the Flask/Django app."""
    app = Flask(__name__)

    with app.app_context():
        # Additional setup if needed (e.g., database connections)
        pass  

    return app