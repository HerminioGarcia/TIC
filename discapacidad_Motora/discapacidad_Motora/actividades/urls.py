from django.urls import path, include
from actividades import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', login_required(views.BienvenidaView.as_view()), name='bienvenida'),
    path('lista_Discapacidades', login_required(views.ListaDiscapacidades.as_view()), name='lista_Discapacidades'),
    path('nueva_discapacidad', login_required(views.CrearDiscapacidadView.as_view()), name='nueva_discapacidad'),
    path('eliminar_discapacidad/<int:id>', views.eliminarMateriaDiscapacidad, name='eliminar_Discapacidad'),
    path('editar_discapacidad/<str:pk>', login_required(views.EditarDiscapacidadView.as_view()), name='editar_discapacidad'),
    path('actividad_discapacidad', login_required(views.ListaActividades.as_view()), name='actividad_Lista'),
    path('nueva_actividad', login_required(views.CrearActividadView.as_view()), name='nueva_actividad'),
    path('editar_actividad/<str:pk>', login_required(views.EditarActividadView.as_view()), name='editar_actividad'),
    path('eliminar_actividad/<int:id>', views.eliminarMateriaActividad, name='eliminar_actividad'),
    path('actividad/<int:id>', views.actividad_view, name='atividadVista'),
    path('Discapacidad/<int:id>', views.discapacidad_view, name='discapacidadVista'),
    path('pdf/<int:model_id>/', views.pdf_view, name='pdf_view'),
    path('like/<int:pk>', views.dar_like, name='dar_like'),
    path('graficas/', login_required(views.Grafica.as_view()), name='solicitudes_Grafica'),
]
