from django.urls import path, include
from actividades import views

urlpatterns = [
    path('lista_Discapacidades', views.ListaDiscapacidades.as_view(), name='lista_Discapacidades'),
    path('nueva_discapacidad', views.CrearDiscapacidadView.as_view(), name='nueva_discapacidad'),
    #path('editar_discapacidad/<str:pk>', views.EditarDiscapacidadView.as_view(), name='editar_discapacidad'),
    path('eliminar_discapacidad/<int:id>', views.eliminarMateriaDiscapacidad, name='eliminar_Discapacidad'),
    path('editar_discapacidad/<str:pk>', views.EditarDiscapacidadView.as_view(), name='editar_discapacidad'),
    path('actividad_discapacidad', views.ListaActividades.as_view(), name='actividad_Lista'),
    path('nueva_actividad', views.CrearActividadView.as_view(), name='nueva_actividad'),
    path('editar_actividad/<str:pk>', views.EditarActividadView.as_view(), name='editar_actividad'),
    path('eliminar_actividad/<int:id>', views.eliminarMateriaActividad, name='eliminar_actividad'),

    
    
]
