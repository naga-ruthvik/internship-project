# Generated by Django 5.1.1 on 2025-06-14 15:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0002_address'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='profie_picture',
            new_name='profile_picture',
        ),
    ]
