# Generated by Django 4.1.2 on 2022-10-25 14:44

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        (
            "nadooit_hr",
            "0002_rename_customers_employee_customers_the_employee_works_for",
        ),
        ("nadooit_crm", "0001_initial"),
        ("nadooit_api_executions_system", "0002_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="CustomerProgramExecutionManager",
            fields=[
                (
                    "Employee",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        primary_key=True,
                        serialize=False,
                        to="nadooit_hr.employee",
                    ),
                ),
                (
                    "can_create_customer_program_execution",
                    models.BooleanField(default=False),
                ),
                (
                    "can_delete_customer_program_execution",
                    models.BooleanField(default=False),
                ),
                (
                    "customers_the_manager_is_responsible_for",
                    models.ManyToManyField(blank=True, to="nadooit_crm.customer"),
                ),
            ],
        ),
    ]
