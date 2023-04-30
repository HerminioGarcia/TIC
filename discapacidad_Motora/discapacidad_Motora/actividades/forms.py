from django import forms
from django.db import models
from .models import Discapacidades_motoras

class FormDiscapacidades_motoras(forms.ModelForm):
    class Meta:
        model = Discapacidades_motoras
        exclude = []
        widgets = {
            'nombreDisapacidad': forms.TextInput(attrs={'class':'form-control'}),
            'descripcion': forms.Textarea(attrs={'class':'form-control'}),
        }

class FormDiscapacidadEditar(FormDiscapacidades_motoras):
    class Meta:
        exclude = []
        model = Discapacidades_motoras

class FormdiscapacidadActividad(forms.Form):  
    nombreActividad = forms.CharField( 
        widget=forms.TextInput(attrs={'class':'form-control','placeholder':'nombreActividad'}),
        required=False
    ) 
        