# Generated by Django 3.1.3 on 2020-11-28 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_profile_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='prasent',
            field=models.BooleanField(default=False),
        ),
    ]
