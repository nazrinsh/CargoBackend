# Generated by Django 4.1.5 on 2023-08-28 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_alter_newuser_email_alter_newuser_first_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newuser',
            name='client_code',
            field=models.CharField(max_length=6, null=True),
        ),
    ]
