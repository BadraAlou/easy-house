# Generated by Django 5.0.3 on 2024-06-11 02:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EasyHouse', '0035_rename_name_contact_nom_remove_contact_subject'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='objet',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]