# Generated by Django 4.0.4 on 2023-02-06 08:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('leagues', '0002_rename_name_league_league_name'),
    ]

    operations = [
        migrations.DeleteModel(
            name='League',
        ),
    ]
