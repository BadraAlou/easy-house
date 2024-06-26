from django.urls import path
from .import views
from EasyHouse.views import *
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', views.accueil, name='accueil'),
    path('contact/', contact_view, name='contact'),
    path('about/', views.about, name='about'),
    path('recherche/', views.recherche_zone, name='recherche_zone'),
    path('resultats/<str:lat>/<str:lng>/', views.resultats_recherche, name='resultats_recherche'),
    path('Nos Maisons/', views.recherche_zone_par_defaut, name='recherche_zone_par_defaut'),
    path('property/<int:property_id>/', views.property_detail, name='property_detail'),
    path('property_list/', views.property_list, name='property_list'),  # Page pour la liste des propriété
    path('rental_form/', views.rental_form, name='rental_form'),
    path('toggle-favorite/<int:property_id>/', views.toggle_favorite, name='toggle_favorite'),
    path('favorites/', views.favorite_properties, name='favorite_properties'),
    path('login', auth_views.LoginView.as_view(template_name = 'employee_information/login.html',redirect_authenticated_user=True), name="login"),
    path('userlogin', views.login_user, name="login-user"),
    path('logout', views.logoutuser, name="logout"),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)