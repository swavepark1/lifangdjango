# Generated by Django 4.1.5 on 2023-01-05 23:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("product", "0005_alter_product_stock"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="product",
            options={"verbose_name": "기업목록", "verbose_name_plural": "기업목록"},
        ),
    ]