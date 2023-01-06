# Generated by Django 4.1.5 on 2023-01-05 23:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("lifanguser", "0005_alter_lifanguser_level"),
    ]

    operations = [
        migrations.AlterField(
            model_name="lifanguser",
            name="level",
            field=models.CharField(
                choices=[("user", "user"), ("admin", "admin")],
                max_length=64,
                verbose_name="등급",
            ),
        ),
    ]
