# Generated by Django 4.0.3 on 2023-04-03 10:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('insaurance', '0015_alter_usermappingrequest_created_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usermappingrequest',
            name='created_at',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='usermappingrequest',
            name='updated_at',
            field=models.DateField(auto_now=True),
        ),
    ]
