# Generated by Django 4.1.5 on 2023-01-06 00:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("lifanguser", "0008_alter_lifanguser_level"),
    ]

    operations = [
        migrations.AlterField(
            model_name="lifanguser",
            name="level",
            field=models.CharField(
                choices=[("admin", "admin"), ("user", "user")],
                max_length=64,
                verbose_name="등급",
            ),
        ),
    ]
