# Generated by Django 4.1.9 on 2023-06-29 10:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bot_management', '0018_remove_photomessage_file_id_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='photomessage',
            options={'ordering': ['-message__date']},
        ),
    ]
