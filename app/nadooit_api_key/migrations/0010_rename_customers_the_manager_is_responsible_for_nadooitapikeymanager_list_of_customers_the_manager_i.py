# Generated by Django 4.1.2 on 2022-10-28 11:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("nadooit_api_key", "0009_nadooitapikeymanager_can_give_apikeymanager_role"),
    ]

    operations = [
        migrations.RenameField(
            model_name="nadooitapikeymanager",
            old_name="customers_the_manager_is_responsible_for",
            new_name="list_of_customers_the_manager_is_responsible_for",
        ),
    ]
