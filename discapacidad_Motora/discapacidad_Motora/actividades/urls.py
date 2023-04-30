from django.urls import path, include
from actividades import views

urlpatterns = [
    path('lista_Discapacidades', views.ListaDiscapacidades.as_view(), name='lista_Discapacidades'),
    path('nueva_discapacidad', views.CrearDiscapacidadView.as_view(), name='nueva_discapacidad'),
    path('editar_discapacidad/<str:pk>', views.EditarDiscapacidadView.as_view(), name='editar_discapacidad'),
    path('eliminar_discapacidad/<int:id>', views.eliminarMateriaDiscapacidad, name='eliminar_Discapacidad'),

    path('actividad_discapacidad/<int:id>', views.discapacidadActividadLista, name='actividad_Lista'),
    #path('nueva_actividad/<int:id>', views.nuevo_campo1, name='nuevo_acti'),
]
