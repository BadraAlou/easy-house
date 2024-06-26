from django.contrib import admin
from .models import *
# Register your models here.
class ImageInline(admin.TabularInline):
    model = Image
    extra = 3  
class ImageAdmin(admin.ModelAdmin):
    list_display=['image']

class PropertyAdmin(admin.ModelAdmin):
    list_display=['titre','description','property_type','nombre_de_chambres','nombre_de_toilettes','prix','address']
    list_filter=('property_type','titre')
    search_fields=('address','property_type')
    inlines = [ImageInline]

class MaisonDisponibleAdmin(admin.ModelAdmin):
    list_display=['latitude','longitude']
    
class RentalAdmin(admin.ModelAdmin):
    list_display=[' prenom','nom','adresse_email','telephone','date_arrivee','date_depart','nombre_personnes','animaux','mode_paiement']

class ContactAdmin(admin.ModelAdmin):
    list_display = ('nom', 'email', 'objet', 'created_at')
    search_fields = ('name', 'email', 'objet')

class EquipeAdmin(admin.ModelAdmin):
    list_display = ('nom', 'poste')

admin.site.register(Image ,ImageAdmin)
admin.site.register(Property,PropertyAdmin)
admin.site.register(MaisonDisponible ,MaisonDisponibleAdmin)
admin.site.register(Rental)
admin.site.register(Contact)
admin.site.register(Equipe)
admin.site.site_header='Easy House'

