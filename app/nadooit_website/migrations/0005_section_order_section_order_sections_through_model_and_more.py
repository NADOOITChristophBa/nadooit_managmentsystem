# Generated by Django 4.1.3 on 2023-04-03 11:14

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ("nadooit_website", "0004_alter_session_session_duration"),
    ]

    operations = [
        migrations.CreateModel(
            name="Section_Order",
            fields=[
                (
                    "section_order_id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("section_order_date", models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name="Section_Order_Sections_Through_Model",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "order",
                    models.PositiveIntegerField(
                        db_index=True, editable=False, verbose_name="order"
                    ),
                ),
                (
                    "section",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="nadooit_website.section",
                    ),
                ),
                (
                    "section_order",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="nadooit_website.section_order",
                    ),
                ),
            ],
            options={
                "ordering": ("section_order", "order"),
            },
        ),
        migrations.AddField(
            model_name="section_order",
            name="sections",
            field=models.ManyToManyField(
                through="nadooit_website.Section_Order_Sections_Through_Model",
                to="nadooit_website.section",
            ),
        ),
        migrations.AlterField(
            model_name="session",
            name="session_section_order",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="nadooit_website.section_order",
            ),
        ),
    ]