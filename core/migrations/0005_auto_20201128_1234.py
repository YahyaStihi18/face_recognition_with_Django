# Generated by Django 3.1.3 on 2020-11-28 11:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_profile_prasent'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='prasent',
            new_name='present',
        ),
    ]
