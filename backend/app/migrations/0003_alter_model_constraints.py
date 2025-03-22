from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_add_fields'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=254, unique=True, blank=False, null=False),
        ),
        migrations.AlterField(
            model_name='preference',
            name='career_goals',
            field=models.TextField(
                blank=True, 
                null=True, 
                help_text="Describe your career goals in detail."
            ),
        ),
        migrations.AlterField(
            model_name='program',
            name='tuition_fee',
            field=models.DecimalField(
                max_digits=10, decimal_places=2, default=0.0, validators=[]
            ),
        ),
    ]