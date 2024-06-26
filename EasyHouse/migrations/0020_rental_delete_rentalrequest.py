# Generated by Django 5.0.3 on 2024-06-08 03:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EasyHouse', '0019_rentalrequest'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rental',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prenom', models.CharField(max_length=100)),
                ('nom', models.CharField(max_length=100)),
                ('adresse', models.EmailField(blank=True, max_length=254)),
                ('telephone', models.CharField(max_length=20)),
                ('date_arrivee', models.DateField()),
                ('date_depart', models.DateField()),
                ('nombre_personnes', models.PositiveIntegerField()),
                ('animaux', models.CharField(choices=[('oui', 'Oui'), ('non', 'Non')], max_length=3)),
                ('mode_paiement', models.CharField(choices=[('carte_credit', 'Carte de crédit'), ('paypal', 'Orange-Money'), ('virement_bancaire', 'Virement bancaire')], max_length=20)),
            ],
        ),
        migrations.DeleteModel(
            name='RentalRequest',
        ),
    ]
