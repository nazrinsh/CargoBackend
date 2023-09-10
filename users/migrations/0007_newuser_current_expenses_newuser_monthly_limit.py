# Generated by Django 4.1.5 on 2023-09-04 23:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_newuser_birthdate'),
    ]

    operations = [
        migrations.AddField(
            model_name='newuser',
            name='current_expenses',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
        migrations.AddField(
            model_name='newuser',
            name='monthly_limit',
            field=models.DecimalField(decimal_places=2, default=300.0, max_digits=10),
        ),
    ]
