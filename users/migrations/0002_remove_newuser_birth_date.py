# Generated by Django 4.1.5 on 2023-08-28 13:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='newuser',
            name='birth_date',
        ),
    ]
