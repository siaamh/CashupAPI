# Generated by Django 5.1.3 on 2025-03-15 06:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapi', '0034_buyer_referral_code_used'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cashupdeposit',
            name='cashup_main_balance',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
    ]
