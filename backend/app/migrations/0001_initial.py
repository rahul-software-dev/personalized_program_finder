from django.db import migrations, models
import django.contrib.auth.models
import django.utils.timezone
from django.conf import settings

class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=150, unique=True)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now)),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={'abstract': False},
            managers=[('objects', django.contrib.auth.models.UserManager())],
        ),
        migrations.CreateModel(
            name='Program',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('university', models.CharField(max_length=255)),
                ('location', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, null=True)),
                ('career_outcomes', models.TextField(blank=True, null=True)),
                ('teaching_style', models.CharField(
                    max_length=100,
                    choices=[
                        ('lecture', 'Lecture-Based'),
                        ('project', 'Project-Based'),
                        ('research', 'Research-Oriented')
                    ]
                )),
                ('cultural_aspects', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Preference',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('user', models.ForeignKey(
                    on_delete=models.CASCADE,
                    to=settings.AUTH_USER_MODEL,
                    related_name='preferences'
                )),
                ('preferred_teaching_style', models.CharField(max_length=100, blank=True, null=True)),
                ('career_goals', models.TextField(blank=True, null=True)),
                ('cultural_preference', models.TextField(blank=True, null=True)),
            ],
        ),
    ]