# Generated by Django 5.0.3 on 2024-06-29 01:26

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Contact",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nom", models.CharField(max_length=100)),
                ("email", models.EmailField(max_length=254)),
                ("objet", models.CharField(blank=True, max_length=100)),
                ("message", models.TextField()),
                ("created_at", models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name="Equipe",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nom", models.CharField(max_length=100)),
                ("poste", models.CharField(max_length=100)),
                ("description", models.TextField()),
                ("photo", models.ImageField(upload_to="team_photos/")),
            ],
        ),
        migrations.CreateModel(
            name="Rental",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("prenom", models.CharField(max_length=100)),
                ("nom", models.CharField(max_length=100)),
                ("adresse_email", models.EmailField(blank=True, max_length=254)),
                ("telephone", models.CharField(max_length=20)),
                ("date_arrivee", models.DateField()),
                ("date_depart", models.DateField()),
                ("nombre_personnes", models.PositiveIntegerField()),
                (
                    "animaux",
                    models.CharField(
                        choices=[("oui", "Oui"), ("non", "Non")], max_length=3
                    ),
                ),
                (
                    "mode_paiement",
                    models.CharField(
                        choices=[
                            ("carte_credit", "Carte de crédit"),
                            ("paypal", "Orange-Money"),
                            ("virement_bancaire", "Virement bancaire"),
                        ],
                        max_length=20,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Property",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("titre", models.CharField(max_length=255)),
                ("description", models.TextField()),
                (
                    "property_type",
                    models.CharField(
                        choices=[
                            ("Easy Day", "Easy Day"),
                            ("Easy Month", "Easy Month"),
                        ],
                        max_length=255,
                    ),
                ),
                ("nombre_de_chambres", models.IntegerField(blank=True, null=True)),
                ("nombre_de_toilettes", models.IntegerField(blank=True, null=True)),
                ("prix", models.IntegerField(default=0)),
                ("address", models.CharField(max_length=255)),
                ("superficie_interne", models.IntegerField(default=0)),
                ("nombre_de_salons", models.IntegerField(blank=True, null=True)),
                (
                    "terrasse",
                    models.CharField(
                        blank=True,
                        choices=[("oui", "Oui"), ("non", "Non")],
                        max_length=25,
                    ),
                ),
                (
                    "wifi",
                    models.CharField(
                        blank=True,
                        choices=[("oui", "Oui"), ("non", "Non")],
                        max_length=25,
                    ),
                ),
                (
                    "parking",
                    models.CharField(
                        blank=True,
                        choices=[("oui", "Oui"), ("non", "Non")],
                        max_length=25,
                    ),
                ),
                (
                    "favorites",
                    models.ManyToManyField(
                        blank=True,
                        related_name="favorite_properties",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="MaisonDisponible",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("latitude", models.CharField(max_length=30)),
                ("longitude", models.CharField(max_length=30)),
                (
                    "property",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="EasyHouse.property",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Image",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("image", models.ImageField(upload_to="property_images/")),
                ("description", models.CharField(blank=True, max_length=50)),
                (
                    "property",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="photos",
                        to="EasyHouse.property",
                    ),
                ),
            ],
        ),
    ]