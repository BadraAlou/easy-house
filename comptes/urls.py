from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register_view, name='register'),
    path('auto-login/', views.auto_login_view, name='auto_login'),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)                             