# Generated by Django 4.1.2 on 2022-10-24 13:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("nadooit_auth", "0002_keymanager"),
    ]

    operations = [
        migrations.DeleteModel(
            name="KeyManager",
        ),
    ]
