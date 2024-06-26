# Create your views here.
import json
from django.shortcuts import render, redirect,HttpResponse
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.contrib import messages
from django.http import JsonResponse
from django.core.mail import send_mail, BadHeaderError
from django.template.loader import render_to_string
from django.utils.html import strip_tags

def register_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if password1 != password2:
            return JsonResponse({"success": False, "message": "Les mots de passe ne correspondent pas."})

        if User.objects.filter(username=username).exists():
            return JsonResponse({"success": False, "message": "Le nom d'utilisateur existe déjà."})

        if User.objects.filter(email=email).exists():
            return JsonResponse({"success": False, "message": "L'adresse email est déjà utilisée."})

        try:
            user = User.objects.create_user(username=username, email=email, password=password1)
            user.save()

            # Automatically log in the user
            login(request, user)

            # Send confirmation email
            subject = 'Confirmation de votre inscription'
            html_message = render_to_string('EasyHouse/emails/confirmation_email.html', {'username': username})
            plain_message = strip_tags(html_message)
            from_email = 'easyhousemalii@gmail.com'
            recipient_list = [email]

            try:
                send_mail(subject, plain_message, from_email, recipient_list, html_message=html_message)
            except BadHeaderError:
                return JsonResponse({"success": False, "message": "Invalid header found."})
            except Exception as e:
                print(f"Error sending email: {e}")
                return JsonResponse({"success": False, "message": "Une erreur est survenue lors de l'envoi de l'email de confirmation. Veuillez réessayer plus tard."})

            return JsonResponse({"success": True, "message": "Votre compte a été créé avec succès et un email de confirmation a été envoyé.", "username": username, "email": email})
        except Exception as e:
            print(f"Error during registration: {e}")
            return JsonResponse({"success": False, "message": "Une erreur est survenue lors de l'inscription. Veuillez réessayer plus tard."})

    return JsonResponse({"success": False, "message": "Requête invalide."})

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return JsonResponse({"success": True, "message": "Connexion réussie."})
        else:
            return JsonResponse({"success": False, "message": "Nom utilisateur ou mot de passe incorrect"}, status=400)
    
    # Rediriger vers la page d'accueil si la requête n'est pas de type POST
    return redirect('accueil')
    
    # Par défaut, rediriger vers la page d'accueil
    return redirect('accueil')

def logout_view(request):
    if request.method == 'POST':
        logout(request)
    return redirect('accueil')

def auto_login_view(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        username = data.get('username')
        password = data.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return JsonResponse({"success": True, "message": "Connexion réussie."})
        else:
            return JsonResponse({"success": False, "message": "Échec de la connexion automatique."})
    return JsonResponse({"success": False, "message": "Requête invalide."})
