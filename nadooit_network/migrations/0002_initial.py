# Generated by Django 4.0.7 on 2022-08-25 12:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('nadooit_network', '0001_initial'),
        ('nadooit_program_ownership_system', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='nadooitinventory',
            name='list_of_nadooit_program_ownership_shares',
            field=models.ManyToManyField(blank=True, to='nadooit_program_ownership_system.nadooitprogramshare'),
        ),
        migrations.AddField(
            model_name='nadooitguildbank',
            name='guild_inventory',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nadooit_network.nadooitinventory'),
        ),
        migrations.AddField(
            model_name='nadooitguild',
            name='member_list',
            field=models.ManyToManyField(blank=True, to='nadooit_network.nadooitnetworkguildmember'),
        ),
    ]
