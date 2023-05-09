from django.db import models
from .validadores import documentos_validador,imagen_validador



class Discapacidades_motoras(models.Model):
    nombreDisapacidad = models.CharField("Nombre del la discapacidad", max_length=200,unique=True)
    que_es=models.TextField("¿Que es?")
    que_es_im = models.ImageField('', upload_to='Imagenes/',validators=[imagen_validador],null=True,blank=True)
    que_deve_conocer_familia=models.TextField("¿Que se debe conocer en el entorno familiar?")
    que_deve_im = models.ImageField('', upload_to='Imagenes/',validators=[imagen_validador],null=True,blank=True)
    recomendaciones=models.TextField("Recomendaciones")
    recomendaciones_im = models.ImageField('', upload_to='Imagenes/',validators=[imagen_validador],null=True,blank=True)
    documentaciones= models.FileField(upload_to = 'Documentos/', null=True,blank=True,validators=[documentos_validador])
    referencias=models.TextField("Referencias")
    def __str__(self):
        return f"{self.nombreDisapacidad}" 

class Actividad(models.Model):
    nombreActividad = models.CharField("Nombre de la actividad", max_length=200)
    tempo= models.IntegerField(default=0)
    aprendizajes_esperados  = models.TextField("Aprendizajes esperados ")
    aspectos_a_favorecer= models.TextField("Aspectos a favorecer")
    Recursos= models.TextField("Recursos")
    competencias_desarrollar=models.TextField("Competencias a desarrollar",null=True,blank=True)
    descripción_actividad=models.TextField("Descripción de la actividad")
    url = models.URLField(max_length = 500,null=True,blank=True)
    referencias=models.TextField("Referencias")
    def __str__(self):
        return f"{self.nombreActividad}"