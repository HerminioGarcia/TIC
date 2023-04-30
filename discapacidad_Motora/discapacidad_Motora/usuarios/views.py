from django.shortcuts import render
from django.views.generic import TemplateView


class BienvenidaView(TemplateView):
    template_name = 'bienvenida.html'