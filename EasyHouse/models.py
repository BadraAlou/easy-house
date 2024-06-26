from django.db import models
from django.contrib.auth.models import User
    
class Property(models.Model):
    titre = models.CharField(max_length=255,)
    description = models.TextField()
    property_type = models.CharField(max_length=255, choices=(
        ('Easy Day', 'Easy Day'),
        ('Easy Month', 'Easy Month')
    ))
    nombre_de_chambres = models.IntegerField(null=True, blank=True)
    nombre_de_toilettes = models.IntegerField(null=True, blank=True)
    prix = models.IntegerField(default=0)
    address = models.CharField(max_length=255)
    superficie_interne = models.IntegerField(default=0)  # Ajout d'une valeur par défaut
    nombre_de_salons = models.IntegerField(null=True, blank=True)
    terrasse = models.CharField(max_length=25,blank=True,choices=(
       ('oui','Oui'),
       ('non', 'Non'),
       
    ))
    wifi = models.CharField(max_length=25,blank=True,choices=(
       ('oui','Oui'),
       ('non', 'Non'),
       
    ))
    parking = models.CharField(max_length=25,blank=True,choices=(
       ('oui','Oui'),
       ('non', 'Non'),
       
    ))
    favorites = models.ManyToManyField(User, related_name='favorite_properties', blank=True)


    def __str__(self):
        return self.titre
    
class Image(models.Model):
    property = models.ForeignKey(Property, related_name='photos', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='property_images/')
    description = models.CharField(max_length=50, blank=True)  # Ajouter ce champ

    def __str__(self):
        return f"Image {self.id}"
    
class MaisonDisponible(models.Model):
    latitude = models.CharField(max_length=30)
    longitude = models.CharField(max_length=30)
    property = models.ForeignKey(Property, on_delete=models.CASCADE)  # Champ ForeignKey vers le modèle Property
    def __str__(self):
      return f"Latitude: {self.latitude}, Longitude: {self.longitude}, Property: {self.property}"
    
class Rental(models.Model):
    prenom = models.CharField(max_length=100)
    nom = models.CharField(max_length=100)
    adresse_email = models.EmailField(blank=True)
    telephone = models.CharField(max_length=20)
    date_arrivee = models.DateField()
    date_depart = models.DateField()
    nombre_personnes = models.PositiveIntegerField()
    animaux = models.CharField(max_length=3, choices=[('oui', 'Oui'), ('non', 'Non')])
    mode_paiement = models.CharField(max_length=20, choices=[('carte_credit', 'Carte de crédit'), ('paypal', 'Orange-Money'), ('virement_bancaire', 'Virement bancaire')])
    def __str__(self):
     return f"{self.prenom} {self.nom} "
    
class Contact(models.Model):
    nom = models.CharField(max_length=100)
    email = models.EmailField()
    objet = models.CharField(max_length=100,blank=True)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nom
    
class Equipe(models.Model):
    nom = models.CharField(max_length=100)
    poste = models.CharField(max_length=100)
    description = models.TextField()
    photo = models.ImageField(upload_to='team_photos/')

    def __str__(self):
        return self.nom





