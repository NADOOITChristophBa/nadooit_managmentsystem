# Generated by Django 4.1.2 on 2022-10-25 16:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nadooit_api_key', '0006_remove_nadooitapikeymanager_employee'),
    ]

    operations = [
        migrations.DeleteModel(
            name='NadooitApiKeyManager',
        ),
    ]
