# Generated by Django 4.1.5 on 2023-01-05 23:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("product", "0003_product_brand_company_product_client_company_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="name",
            field=models.CharField(
                default="", max_length=256, null=True, verbose_name="상품명"
            ),
        ),
    ]
