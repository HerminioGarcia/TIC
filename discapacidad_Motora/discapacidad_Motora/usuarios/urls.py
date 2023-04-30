from django.urls import path, re_path, include
from usuarios import views
from django.contrib.auth.views import LogoutView
from django.contrib.auth.decorators import login_required
from django.contrib.auth import views as auth_views

urlpatterns = [
    # Bienbenida del sitio
    path('', views.BienvenidaView.as_view(), name='bienvenida'),

]
