# Generated by Django 4.1.2 on 2022-10-21 10:01

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ("nadooit_hr", "0001_initial"),
        ("nadooit_crm", "0001_initial"),
        ("nadooit_time_account", "0001_initial"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="TimeAccountEmployee",
            new_name="EmployeeTimeAccount",
        ),
        migrations.CreateModel(
            name="TimeAccountManager",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                (
                    "employee",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="nadooit_hr.employee",
                    ),
                ),
                (
                    "time_accounts",
                    models.ManyToManyField(
                        blank=True, to="nadooit_time_account.timeaccount"
                    ),
                ),
            ],
        ),
    ]
