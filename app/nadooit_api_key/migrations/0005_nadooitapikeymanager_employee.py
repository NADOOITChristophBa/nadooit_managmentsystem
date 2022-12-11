# Generated by Django 4.1.2 on 2022-10-25 15:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("nadooit_hr", "0003_employeemanager"),
        (
            "nadooit_api_key",
            "0004_remove_nadooitapikeymanager_can_edit_api_key_and_more",
        ),
    ]

    operations = [
        migrations.AddField(
            model_name="nadooitapikeymanager",
            name="employee",
            field=models.OneToOneField(
                default="dced8968-c013-4b0e-9406-bf23b8a7723b",
                on_delete=django.db.models.deletion.CASCADE,
                to="nadooit_hr.employee",
            ),
            preserve_default=False,
        ),
    ]
