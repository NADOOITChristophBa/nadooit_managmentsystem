# Generated by Django 4.1.2 on 2022-11-04 16:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        (
            "nadooit_hr",
            "0014_rename_can_give_customermanager_role_customermanager_can_give_manager_role",
        ),
    ]

    operations = [
        migrations.RenameField(
            model_name="employeemanager",
            old_name="can_add_new_employees",
            new_name="can_add_new_employee",
        ),
    ]
