# Generated by Django 4.0.7 on 2022-08-25 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nadooit_time_account', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timeaccount',
            name='time_balance_in_seconds',
            field=models.BigIntegerField(blank=True, default=0, null=True),
        ),
    ]
