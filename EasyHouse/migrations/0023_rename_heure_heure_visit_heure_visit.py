# Generated by Django 5.0.3 on 2024-06-09 04:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('EasyHouse', '0022_visit'),
    ]

    operations = [
        migrations.RenameField(
            model_name='visit',
            old_name='heure_heure',
            new_name='heure_visit',
        ),
    ]
