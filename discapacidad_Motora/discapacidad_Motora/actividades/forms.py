from django import forms
from django.db import models
from .models import Actividad, Discapacidades_motoras

class FormDiscapacidades_motoras(forms.ModelForm):
    class Meta:
        model = Discapacidades_motoras
        exclude = []
        widgets = {
            'nombreDisapacidad': forms.TextInput(attrs={'class':'form-control'}),
            'descripcion': forms.Textarea(attrs={'class':'form-control'}),
            'que_es':forms.Textarea(attrs={'class':'form-control'}),
            'que_deve_conocer_familia':forms.Textarea(attrs={'class':'form-control'}),
            'documentacion':forms.FileInput(attrs={'class':'form-control'}),
            'recomendaciones':forms.Textarea(attrs={'class':'form-control'}),
            'referencias': forms.Textarea(attrs={'class':'form-control'}),
        }

#class FormDiscapacidadEditar(FormDiscapacidades_motoras):
#    class Meta:
#        exclude = []
#        model = Discapacidades_motoras
#        fields = '__all__'
#        widgets = {
#            'nombreDisapacidad': forms.TextInput(attrs={'class':'form-control'}),
#            'descripcion': forms.Textarea(attrs={'class':'form-control'}),
#            'que_es':forms.Textarea(attrs={'class':'form-control'}),
#            'que_deve_conocer_familia':forms.Textarea(attrs={'class':'form-control'}),
#            'documentacion':forms.FileInput(attrs={'class':'form-control'}),
#            'recomendaciones':forms.Textarea(attrs={'class':'form-control'}),
#            'referencias': forms.Textarea(attrs={'class':'form-control'}),
#        }

class FormDiscapacidadEditar(FormDiscapacidades_motoras):
    class Meta:
        exclude = []
        model = Discapacidades_motoras
        fields = '__all__'
        widgets = {
            'nombreDisapacidad': forms.TextInput(attrs={'class':'form-control'}),
            'que_es':forms.Textarea(attrs={'class':'form-control'}),
            'que_deve_conocer_familia':forms.Textarea(attrs={'class':'form-control'}),
            'recomendaciones':forms.Textarea(attrs={'class':'form-control'}),
            'referencias': forms.Textarea(attrs={'class':'form-control'}),

        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance.pk and self.instance.nombreDisapacidad:
            self.fields['nombreDisapacidad'].widget.attrs.update({'disabled': True})
        if self.instance.pk and self.instance.que_es:
            self.fields['que_es'].widget.attrs.update({'disabled': True})
        if self.instance.pk and self.instance.que_deve_conocer_familia:
            self.fields['que_deve_conocer_familia'].widget.attrs.update({'disabled': True})
        if self.instance.pk and self.instance.recomendaciones:
            self.fields['recomendaciones'].widget.attrs.update({'disabled': True})
        if self.instance.pk and self.instance.referencias:
            self.fields['referencias'].widget.attrs.update({'disabled': True})

class FormdiscapacidadActividad(forms.Form):  
    nombreActividad = forms.CharField( 
        widget=forms.TextInput(attrs={'class':'form-control','placeholder':'nombreActividad'}),
        required=False
    )

class FormActividad(forms.ModelForm):
    class Meta:
        model = Actividad
        exclude = []
        widgets = {
            'nombreActividad' : forms.TextInput(attrs={'class':'form-control'}),
            'tempo': forms.NumberInput(attrs={'class':'form-control'}),
            'aprendizajes_esperados':forms.Textarea(attrs={'class':'form-control'}),
            'aspectos_a_favorecer':forms.Textarea(attrs={'class':'form-control'}),
            'Recursos':forms.Textarea(attrs={'class':'form-control'}),
            'competencias_desarrollar':forms.Textarea(attrs={'class':'form-control'}),
            'descripción_actividad':forms.Textarea(attrs={'class':'form-control'}),
            'url' : forms.TextInput(attrs={'class':'form-control'}),
            'referencias': forms.Textarea(attrs={'class':'form-control'}),
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance.pk and self.instance.nombreActividad:
            self.fields['nombreActividad'].widget.attrs.update({'disabled': True})
        if self.instance.pk and self.instance.tempo:
            self.fields['tempo'].widget.attrs.update({'disabled': True})
        if self.instance.pk and self.instance.aprendizajes_esperados:
            self.fields['aprendizajes_esperados'].widget.attrs.update({'disabled': True})
        if self.instance.pk and self.instance.Recursos:
            self.fields['Recursos'].widget.attrs.update({'disabled': True})
        if self.instance.pk and self.instance.competencias_desarrollar:
            self.fields['competencias_desarrollar'].widget.attrs.update({'disabled': True})
        if self.instance.pk and self.instance.descripción_actividad:
            self.fields['descripción_actividad'].widget.attrs.update({'disabled': True})
        if self.instance.pk and self.instance.url:
            self.fields['url'].widget.attrs.update({'disabled': True})
        if self.instance.pk and self.instance.referencias:
            self.fields['referencias'].widget.attrs.update({'disabled': True})


class FormActividadEditar(FormActividad):
    class Meta:
        exclude = []
        model = Actividad
        widgets = {
            'nombreActividad' : forms.TextInput(attrs={'class':'form-control'}),
            'tempo': forms.NumberInput(attrs={'class':'form-control'}),
            'aprendizajes_esperados':forms.Textarea(attrs={'class':'form-control'}),
            'aspectos_a_favorecer':forms.Textarea(attrs={'class':'form-control'}),
            'Recursos':forms.Textarea(attrs={'class':'form-control'}),
            'competencias_desarrollar':forms.Textarea(attrs={'class':'form-control'}),
            'descripción_actividad':forms.Textarea(attrs={'class':'form-control'}),
            'url' : forms.TextInput(attrs={'class':'form-control'}),
            'referencias': forms.Textarea(attrs={'class':'form-control'}),
        }