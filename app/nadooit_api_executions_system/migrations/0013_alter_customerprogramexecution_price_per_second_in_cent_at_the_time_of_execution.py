# Generated by Django 4.1.3 on 2022-11-19 12:09

from decimal import Decimal
from django.db import migrations
import djmoney.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('nadooit_api_executions_system', '0012_customerprogramexecution_price_per_second_in_cent_at_the_time_of_execution_currency_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customerprogramexecution',
            name='price_per_second_in_cent_at_the_time_of_execution',
            field=djmoney.models.fields.MoneyField(decimal_places=6, default=Decimal('0'), default_currency='EUR', max_digits=14),
        ),
    ]
