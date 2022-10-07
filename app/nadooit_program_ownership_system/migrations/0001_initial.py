# Generated by Django 4.1 on 2022-10-05 16:09

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("nadooit_time_account", "0001_initial"),
        ("nadooit_crm", "0001_initial"),
        ("nadooit_program", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="NadooitProgramShare",
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
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "share_of",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="nadooit_program.nadooitprogram",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="NadooitCustomerProgram",
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
                    "program_time_saved_per_execution_in_seconds",
                    models.IntegerField(default=0),
                ),
                ("over_charge", models.BooleanField(default=False)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "customer",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="nadooit_crm.customer",
                    ),
                ),
                (
                    "program",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="nadooit_program.nadooitprogram",
                    ),
                ),
                (
                    "time_account",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="nadooit_time_account.timeaccount",
                    ),
                ),
            ],
        ),
    ]
