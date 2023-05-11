from django.urls import reverse_lazy
from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User

from .models import DatosPersonales

class UserForm(forms.ModelForm):
    repassword = forms.CharField()
    class Meta:
        model = User
        fields = ('username','password','email','repassword')

    email = forms.EmailField(required=True)
    
    
    def save(self, commit=True):
        user = super(UserForm, self).save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user
    
    def clean_password(self, *args, **kwargs):
        if self.data['password'] != self.data['repassword']:
            raise forms.ValidationError('Las contraseñas son diferentes; favor de verificar')
        
        return self.data['password']
    
class FormDatosPersonales(forms.ModelForm):
    class Meta:
        model=DatosPersonales
        exclude = ['user']
        widgets = {
            'nombre': forms.TextInput(attrs={'class':'form-control'}),
            'apellido_paterno': forms.TextInput(attrs={'class':'form-control'}),
            'apellido_materno': forms.TextInput(attrs={'class':'form-control'}),
            'genero': forms.Select(attrs={'class':'form-control'}),'colonia': forms.TextInput(attrs={'class':'form-control'}),
            'instituto': forms.TextInput(attrs={'class':'form-control'}),
            'grado_estudio': forms.Select(attrs={'class':'form-control'}),
            'curp': forms.TextInput(attrs={'class':'form-control'}),
            'fecha_nacimiento': forms.DateInput(attrs={'type': 'date'}),
        }
