# Generated by Django 4.1 on 2022-10-05 16:09

import uuid

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("nadooit_crm", "0001_initial"),
        ("nadooit_program", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Process",
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
                ("name", models.CharField(max_length=255)),
                ("description", models.TextField()),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "customer",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="nadooit_crm.customer",
                    ),
                ),
                (
                    "list_of_nadooit_programs",
                    models.ManyToManyField(to="nadooit_program.nadooitprogram"),
                ),
                (
                    "tiggers_process",
                    models.ManyToManyField(blank=True, to="nadooit_workflow.process"),
                ),
                (
                    "trigger_process",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="nadooit_workflow.process",
                    ),
                ),
            ],
        ),
    ]
