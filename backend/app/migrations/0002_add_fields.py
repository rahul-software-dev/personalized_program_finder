from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='program',
            name='duration',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='program',
            name='tuition_fee',
            field=models.DecimalField(max_digits=10, decimal_places=2, default=0.0),
        ),
    ]