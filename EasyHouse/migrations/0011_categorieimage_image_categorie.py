# Generated by Django 5.0.3 on 2024-05-19 03:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EasyHouse', '0010_image_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='CategorieImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='image',
            name='categorie',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='images', to='EasyHouse.categorieimage'),
            preserve_default=False,
        ),
    ]
