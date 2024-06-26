import json
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse
import googlemaps
from django.conf import settings
from .forms import PropertyFilterForm,RentalForm,ContactForm
from EasyHouse.models import Equipe, MaisonDisponible, Property
from django.contrib.auth.decorators import login_required
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.core.mail import send_mail, BadHeaderError
from django.contrib.auth import authenticate, login, logout
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here. 

def accueil(request):
    return render(request, 'EasyHouse/accueil.html')

def recherche_zone(request):
    if request.method == 'POST':
        zone_recherchee = request.POST.get('zone_recherchee')
        if zone_recherchee:
            gmaps = googlemaps.Client(key=settings.GOOGLE_MAPS_API_KEY)
            geocode_result = gmaps.geocode(zone_recherchee)
            if geocode_result:
                lat = geocode_result[0]['geometry']['location']['lat']
                lng = geocode_result[0]['geometry']['location']['lng']
                return redirect('resultats_recherche', lat=lat, lng=lng,)
            else:
                # Si aucune zone n'est trouvée, redirigez vers une zone par défaut
                default_lat = 12.625540159393449  # Latitude de Paris
                default_lng =-8.0390739  # Longitude de Paris
                return redirect('resultats_recherche', lat=default_lat, lng=default_lng)
    
    return render(request, 'EasyHouse/resultat_recherche.html')

def resultats_recherche(request, lat, lng):
    marqueurs = MaisonDisponible.objects.all()
    # Logique pour afficher les résultats de recherche avec les coordonnées lat et lng
    return render(request, 'EasyHouse/resultat_recherche.html', {'lat': lat, 'lng': lng, 'marqueurs': marqueurs})

def recherche_zone_par_defaut(request):
    # Logique pour déterminer la zone par défaut ou autres paramètres
    # Vous pouvez définir les coordonnées de la zone par défaut ici
    marqueurs = MaisonDisponible.objects.all()
    return render(request, 'EasyHouse/carte_par_defaut.html',{'marqueurs':marqueurs})

def property_detail(request, property_id):
    property = get_object_or_404(Property, id=property_id)
    
    # Obtenir une liste distincte de descriptions de photos
    distinct_descriptions = property.photos.values_list('description', flat=True).distinct()

    # Obtenir la première photo de chaque catégorie
    category_photos = []
    for description in distinct_descriptions:
        photo = property.photos.filter(description=description).first()
        if photo:
            category_photos.append((description, photo))
    
    return render(request, 'EasyHouse/property_detail.html', {
        'property': property,
        'category_photos': category_photos,
    })

def property_list(request):
   
    properties = Property.objects.all()
    form = PropertyFilterForm(request.GET)
    user = request.user
    favorite_properties = user.favorite_properties.all() if user.is_authenticated else []
    favorite_property_ids = [property.id for property in favorite_properties]


    if form.is_valid():
        if form.cleaned_data['property_type']:
            properties = properties.filter(property_type=form.cleaned_data['property_type'])
        if form.cleaned_data['prix_min'] is not None:
            properties = properties.filter(prix__gte=form.cleaned_data['prix_min'])
        if form.cleaned_data['prix_max'] is not None:
            properties = properties.filter(prix__lte=form.cleaned_data['prix_max'])
        if form.cleaned_data['nombre_de_chambres'] is not None:
            properties = properties.filter(nombre_de_chambres=form.cleaned_data['nombre_de_chambres'])
        if form.cleaned_data['nombre_de_toilettes'] is not None:
            properties = properties.filter(nombre_de_toilettes=form.cleaned_data['nombre_de_toilettes'])

    paginator = Paginator(properties, 4)  # Nombre de propriétés par page

    page = request.GET.get('page')
    try:
        properties = paginator.page(page)
    except PageNotAnInteger:
        properties = paginator.page(1)
    except EmptyPage:
        properties = paginator.page(paginator.num_pages)


    return render(request, 'EasyHouse/property_list.html', {'properties': properties,'form': form, 'favorite_property_ids': favorite_property_ids, 'is_authenticated': request.user.is_authenticated, 'paginator': paginator,})

def about(request):
    equipe = Equipe.objects.all()
   
    return render(request, 'EasyHouse/about.html',{'equipe': equipe})

def contact_view(request):
   
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contact = form.save()
            email = form.cleaned_data.get('email')
            nom = form.cleaned_data.get('nom')
            
            # Send confirmation email
            subject = 'Merci pour votre message'
            html_message = render_to_string('EasyHouse/emails/contact_confirmation.html', {'nom': nom})
            plain_message = strip_tags(html_message)
            from_email = 'easyhousemalii@gmail.com'
            recipient_list = [email]

            try:
                send_mail(subject, plain_message, from_email, recipient_list, html_message=html_message)
            except BadHeaderError:
                return JsonResponse({'success': False, 'message': 'Invalid header found.'})
            except Exception as e:
                print(f"Error sending email: {e}")
                return JsonResponse({'success': False, 'message': "Une erreur est survenue lors de l'envoi de l'email de confirmation. Veuillez réessayer plus tard."})

            return JsonResponse({'success': True})
        else:
            return JsonResponse({'success': False, 'errors': form.errors})

    form = ContactForm()
    return render(request, 'EasyHouse/contact.html', {'form': form})

def rental_form(request):
    if request.method == 'POST':
        form = RentalForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({'success': True})
        else:
            return JsonResponse({'success': False, 'errors': form.errors})
    
    return render(request, 'EasyHouse/rental_form.html')


@login_required
def toggle_favorite(request, property_id):
    property = get_object_or_404(Property, id=property_id)
    user = request.user
    if user in property.favorites.all():
        property.favorites.remove(user)
        is_favorite = False
    else:
        property.favorites.add(user)
        is_favorite = True
    return JsonResponse({'is_favorite': is_favorite,})
@login_required
def favorite_properties(request):
    user = request.user
    favorite_properties = user.favorite_properties.all()
    exclude_footer = True  # Correction de la syntaxe ici
    return render(request, 'EasyHouse/favorite.html', {'properties': favorite_properties, 'exclude_footer': exclude_footer})

# Login
def login_user(request):
    logout(request)
    resp = {"status":'failed','msg':''}
    username = ''
    password = ''
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                resp['status']='success'
            else:
                resp['msg'] = "Nom d'utilisateur ou Mots de passe incorrect"
        else:
            resp['msg'] = "Nom d'utilisateur ou Mots de passe incorrec"
    return HttpResponse(json.dumps(resp),content_type='application/json')

#Logout
def logoutuser(request):
    logout(request)
    return redirect('login')
