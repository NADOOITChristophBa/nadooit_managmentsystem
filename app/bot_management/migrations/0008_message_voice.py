# Generated by Django 4.1.9 on 2023-06-15 09:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bot_management', '0007_message_advertisement'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='voice',
            field=models.FileField(blank=True, null=True, upload_to='voice_messages/'),
        ),
    ]