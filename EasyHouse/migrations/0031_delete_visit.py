# Generated by Django 5.0.3 on 2024-06-09 05:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('EasyHouse', '0030_alter_visit_date_visit_alter_visit_heure_visit'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Visit',
        ),
    ]
