# Generated by Django 4.1.3 on 2022-11-11 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nadooit_api_executions_system', '0010_delete_customerprogramexecutionmanager'),
    ]

    operations = [
        migrations.AddField(
            model_name='customerprogramexecution',
            name='payment_status',
            field=models.CharField(choices=[('NOT_PAID', 'Not Paid'), ('PAID', 'Paid'), ('REFUNDED', 'Refunded'), ('REVOKED', 'Revoked')], default='NOT_PAID', max_length=20),
        ),
    ]
