# Generated by Django 5.0.3 on 2024-06-11 02:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('EasyHouse', '0034_contact'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='name',
            new_name='nom',
        ),
        migrations.RemoveField(
            model_name='contact',
            name='subject',
        ),
    ]
