# Generated by Django 4.1.2 on 2022-10-28 11:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        (
            "nadooit_time_account",
            "0011_rename_can_delete_api_key_timeaccountmanager_can_delete_time_accounts_and_more",
        ),
    ]

    operations = [
        migrations.RenameField(
            model_name="timeaccountmanager",
            old_name="customers_the_manager_is_responsible_for",
            new_name="list_of_customers_the_manager_is_responsible_for",
        ),
    ]
