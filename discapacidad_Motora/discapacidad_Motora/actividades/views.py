from collections import Counter
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.db.models import Count
from django.urls import reverse_lazy
from django.views.generic import ListView, TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Discapacidades_motoras,Actividad
from .forms import FormActividad, FormActividadEditar, FormDiscapacidades_motoras,FormDiscapacidadEditar,FormdiscapacidadActividad
from django.contrib.auth.decorators import login_required,permission_required
from django.http import FileResponse
from django.shortcuts import get_object_or_404
from django.template import loader

class BienvenidaView(TemplateView):
    template_name = 'bienvenida.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Obtener las actividades con sus respectivos conteos de likes
        actividades = Actividad.objects.annotate(num_likes=Count('likes')).order_by('-num_likes')
        # Obtener los nombres de las actividades y los conteos de likes
        nombres_actividades = [actividad.nombreActividad for actividad in actividades]
        num_likes = [actividad.num_likes for actividad in actividades]

        # Pasar los datos al contexto
        context['nombres_actividades'] = nombres_actividades
        context['num_likes'] = num_likes

        return context

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

@login_required
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

@login_required
def eliminarMateriaActividad(request, id):
    actividad=Actividad.objects.get(id=id)
    id_r = actividad.discapacidad.id
    Actividad.objects.get(id=id).delete()
    return redirect('actividad_Lista')

@login_required
def actividad_view(request, id):
    actividad=Actividad.objects.get(id=id)
    nom=actividad.nombreActividad
    tieneL= request.user in actividad.likes.all()
    context = {
        'actividad': actividad,
        'nom_activ':nom,
        'likes': actividad.cantidad_likes(),
        'tieneL': tieneL
    }
    return render(request, 'actividad_template.html', context)

@login_required
def discapacidad_view(request, id):
    discapacidad=Discapacidades_motoras.objects.get(id=id)
    nom=discapacidad.nombreDisapacidad
    context = {
        'discapacidad': discapacidad,
        'nom_dis':nom
    }
    return render(request, 'discapacidad_template.html', context)

@login_required
def pdf_view(request, model_id):
    obj = get_object_or_404(Discapacidades_motoras, pk=model_id)
    
    # Assuming your model has a 'pdf_file' field representing the PDF file
    pdf_file = obj.documentaciones
    
    response = FileResponse(open(pdf_file.path, 'rb'), content_type='application/pdf')
    return response

@login_required
def dar_like(request, pk):
    post = get_object_or_404(Actividad, id=pk)
    if request.user in post.likes.all():
        post.likes.remove(request.user)
    else:
        post.likes.add(request.user.id)
    
    return redirect('/actividad/'+str(pk))
    
class Grafica(TemplateView):
    template_name="grafica.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Obtener las actividades con sus respectivos conteos de likes
        actividades = Actividad.objects.annotate(num_likes=Count('likes')).order_by('-num_likes')
        # Obtener los nombres de las actividades y los conteos de likes
        nombres_actividades = [actividad.nombreActividad for actividad in actividades]
        num_likes = [actividad.num_likes for actividad in actividades]

        # Pasar los datos al contexto
        context['nombres_actividades'] = nombres_actividades
        context['num_likes'] = num_likes

        return context
    
    