from django.contrib import admin
from .models import User, Program, Preference

class BaseAdmin(admin.ModelAdmin):
    """Base admin class with common configurations."""
    ordering = ['id']
    readonly_fields = ['id']
    list_per_page = 20

@admin.register(User)
class UserAdmin(BaseAdmin):
    list_display = ('id', 'username', 'email', 'date_joined', 'is_active')
    search_fields = ('username', 'email')
    list_filter = ('is_active', 'date_joined')
    fieldsets = (
        ("User Info", {"fields": ("username", "email", "date_joined", "is_active")}),
    )

@admin.register(Program)
class ProgramAdmin(BaseAdmin):
    list_display = ('id', 'name', 'university', 'location', 'teaching_style')
    search_fields = ('name', 'university', 'location')
    list_filter = ('teaching_style', 'location')
    fieldsets = (
        ("Program Details", {"fields": ("name", "university", "location", "teaching_style")}),
    )

@admin.register(Preference)
class PreferenceAdmin(BaseAdmin):
    list_display = ('id', 'user', 'preferred_teaching_style')
    search_fields = ('user__username', 'preferred_teaching_style')
    list_filter = ('preferred_teaching_style',)
    fieldsets = (
        ("Preference Details", {"fields": ("user", "preferred_teaching_style")}),
    )