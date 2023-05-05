from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Discapacidades_motoras,Actividad
from .forms import FormActividad, FormActividadEditar, FormDiscapacidades_motoras,FormDiscapacidadEditar,FormdiscapacidadActividad

class ListaDiscapacidades(ListView):
    model = Discapacidades_motoras

class CrearDiscapacidadView(CreateView):
    model = Discapacidades_motoras
    form_class = FormDiscapacidades_motoras
    success_url = reverse_lazy('lista_Discapacidades')
    success_message = "Datos guardados de manera exitosa"

#class EditarDiscapacidadView(UpdateView):
#    model = Discapacidades_motoras
#    form_class = FormDiscapacidadEditar
#    extra_context = {'accion': 'Editar'}
#    success_url = reverse_lazy('lista_Discapacidades')

class EditarDiscapacidadView(UpdateView):
    model = Discapacidades_motoras
    form_class = FormDiscapacidadEditar
    extra_context = {'accion': 'Editar'}
    success_url = reverse_lazy('lista_Discapacidades')

def eliminarMateriaDiscapacidad(request, id):
    Discapacidades_motoras.objects.get(id=id).delete()
    return redirect('lista_Discapacidades')

class ListaActividades(ListView):
    model = Actividad

class CrearActividadView(CreateView):
    model = Actividad
    form_class = FormActividad
    success_url = reverse_lazy('actividad_Lista')
    success_message = "Datos guardados de manera exitosa"

class EditarActividadView(UpdateView):
    model = Actividad
    form_class = FormActividadEditar
    extra_context = {'accion': 'Editar'}
    success_url = reverse_lazy('actividad_Lista')
    success_message = "Datos guardados de manera exitosa"

def eliminarMateriaActividad(request, id):
    actividad=Actividad.objects.get(id=id)
    id_r = actividad.discapacidad.id
    Actividad.objects.get(id=id).delete()
    return redirect('actividad_Lista')