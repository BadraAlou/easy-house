# Generated by Django 5.0.3 on 2024-06-09 05:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EasyHouse', '0025_alter_visit_date_visit'),
    ]

    operations = [
        migrations.AlterField(
            model_name='visit',
            name='date_visit',
            field=models.DateField(default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='visit',
            name='heure_visit',
            field=models.TimeField(),
        ),
    ]
