# Generated by Django 3.2.12 on 2022-05-04 10:46

from decimal import Decimal
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("checkout", "0052_auto_20220412_0831"),
    ]

    operations = [
        migrations.AlterField(
            model_name="checkout",
            name="shipping_tax_rate",
            field=models.DecimalField(
                decimal_places=2, default=Decimal("0.0"), max_digits=5
            ),
        ),
    ]
