# Generated by Django 4.0.7 on 2022-08-25 12:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('nadooit_api_executions_system', '0003_remove_customerprogram_customer_id_and_more'),
        ('nadooit_program_ownership_system', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customerprogramexecution',
            name='customer_program',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='nadooit_program_ownership_system.nadooitcustomerprogram'),
        ),
        migrations.DeleteModel(
            name='CustomerProgram',
        ),
    ]
