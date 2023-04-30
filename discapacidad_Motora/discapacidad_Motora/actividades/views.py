from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Discapacidades_motoras,Actividad
from .forms import FormDiscapacidades_motoras,FormDiscapacidadEditar,FormdiscapacidadActividad

class ListaDiscapacidades(ListView):
    model = Discapacidades_motoras

class CrearDiscapacidadView(CreateView):
    model = Discapacidades_motoras
    form_class = FormDiscapacidades_motoras
    success_url = reverse_lazy('lista_Discapacidades')
    success_message = "Datos guardados de manera exitosa"

class EditarDiscapacidadView(UpdateView):
    model = Discapacidades_motoras
    form_class = FormDiscapacidadEditar
    extra_context = {'accion': 'Editar'}
    success_url = reverse_lazy('lista_Discapacidades')

def eliminarMateriaDiscapacidad(request, id):
    Discapacidades_motoras.objects.get(id=id).delete()
    return redirect('lista_Discapacidades')

def discapacidadActividadLista(request, id):
    nom_discap_motoras=""
    form = FormdiscapacidadActividad()
    actividadDiscapacitados = Actividad.objects.filter(discapacidad_id=id)
    discap_motoras=Discapacidades_motoras.objects.filter(id=id)
    for formu in discap_motoras:
        nom_discap_motoras=formu.nombreDisapacidad

    if request.method == 'POST':
        form = FormdiscapacidadActividad(request.POST)
        nombreActividad = request.POST.get('nombreActividad', None)
        if nombreActividad:
            actividadDiscapacitados = actividadDiscapacitados.filter(nombreActividad__contains=nombreActividad)
        
        
    context={
        'actividadDiscapacitados': actividadDiscapacitados,
        'form':form,
        'id_form':id,
        'nom_discap_motoras':nom_discap_motoras
    }
    return render(request, 'actividadDiscapacitados.html', context)