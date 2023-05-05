from django.urls import path, re_path, include
from usuarios import views
from django.contrib.auth.views import LogoutView
from django.contrib.auth.decorators import login_required
from django.contrib.auth import views as auth_views

#app_name = 'usuarios'
urlpatterns = [
    # Bienbenida del sitio
    path('', views.BienvenidaView.as_view(), name='bienvenida'),
    path('salir', LogoutView.as_view(), name='logout'),
    path('entrar', views.LoginView.as_view(), name='login'),
    path('registrar', views.RegistrarView.as_view(), name='registrar'),
    path('lista', views.ListaUsuariosView.as_view(), name='lista'),
    path('grupos', views.asignar_grupos, name='asignar_grupos'),
    path('activar/<slug:uidb64>/<slug:token>', views.ActivarCuentaView.as_view(), name='activar'),
    path('eliminar/<int:id>', views.eliminar_usuario, name='eliminar_usuario2'),
    
    path('reset/password_reset', auth_views.PasswordResetView.as_view(template_name='registration/password_reset_form.html'
    , email_template_name="registration/password_reset_email.html"), name = 'password_reset'),
    
    path('reset/password_reset_done', 
    auth_views.PasswordResetDoneView.as_view(template_name='registration/password_reset_done.html'), 
    name = 'password_reset_done'),
    
    re_path(r'^reset/(?P<uidb64>[0-9A-za-z_\-]+)/(?P<token>.+)/$', 
    auth_views.PasswordResetConfirmView.as_view(template_name="registration/password_reset_confirm.html"), 
    name = 'password_reset_confirm'),
    
    path('reset/done',
    auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html'), 
    name = 'password_reset_complete'),
]