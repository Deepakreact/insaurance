# Generated by Django 4.0.3 on 2023-03-24 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('insaurance', '0004_alter_lead_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lead',
            name='price',
            field=models.CharField(blank=True, default=0, max_length=200, null=True),
        ),
    ]
