from django.contrib import admin
from django.urls import path, include
from usuarios import views
#agregamos settings y static para lo la subida de archivos
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('usuario/', include('usuarios.urls'),name='bienvenida'),
    path('', include('actividades.urls'),name='bienvenida'),
]
if settings.DEBUG:
 urlpatterns += static(settings.MEDIA_URL, document_root =settings.MEDIA_ROOT)
#agregamos esta linea para dirigirnos los documentos a media
