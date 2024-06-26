# forms.py
from django import forms
from .models import Rental,Contact

class PropertyFilterForm(forms.Form):
    property_type = forms.ChoiceField(
        choices=[
            ('', 'Type de propriété'),
            ('Easy Day', 'Easy Day'),
            ('Easy Month', 'Easy Month')
        ],
        required=False
    )
    prix_min = forms.IntegerField(required=False, min_value=0, label='Prix min (fcfa)')
    prix_max = forms.IntegerField(required=False, min_value=0, label='Prix max (fcfa)')
    nombre_de_chambres = forms.IntegerField(required=False, min_value=0, label='Nombre de chambres')
    nombre_de_toilettes = forms.IntegerField(required=False, min_value=0, label='Nombre de toilettes')

class RentalForm(forms.ModelForm):
    class Meta:
        model = Rental
        fields = [
            'prenom', 'nom', 'adresse_email', 'telephone', 
            'date_arrivee', 'date_depart', 'nombre_personnes', 
            'animaux', 'mode_paiement'
        ]
class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['nom', 'email', 'objet', 'message']
        widgets = {
            'nom': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Votre Nom'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
            'objet': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Subject'}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Entrer Votre message'}),
        }