# Generated by Django 4.1.2 on 2022-10-28 11:38

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('nadooit_crm', '0001_initial'),
        ('nadooit_hr', '0003_employeemanager'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employeemanager',
            old_name='customers_the_manager_is_responsible_for',
            new_name='list_of_customers_the_manager_is_responsible_for',
        ),
        migrations.CreateModel(
            name='CustomerManager',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('employee', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='nadooit_hr.employee')),
                ('list_of_customers_the_manager_is_responsible_for', models.ManyToManyField(blank=True, to='nadooit_crm.customer')),
            ],
        ),
    ]
