from django.db import models
from .validadores import documentos_validador



class Discapacidades_motoras(models.Model):
    nombreDisapacidad = models.CharField("Nombre del la discapacidad", max_length=200,default=False)
    descripcion = models.TextField("Descripcion:",default=False)
    que_es=models.TextField("¿Que es?:",default=False)
    que_deve_conocer_familia=models.TextField("¿Que se debe conocer en el entorno familiar?:",default=False)
    documentacion= models.FileField(upload_to = "Documentos", null=True,blank=True,validators=[documentos_validador])
    recomendaciones=models.TextField("Recomendaciones:",default=False)
    def __str__(self):
        return f"{self.nombreDisapacidad}" 

class Actividad(models.Model):
    nombreActividad = models.CharField("Nombre de la actividad:", max_length=200, null=False,default=False)
    discapacidad = models.ForeignKey(Discapacidades_motoras,related_name="Discapacidad" , on_delete=models.CASCADE,null=False)
    tempo= models.IntegerField(default=0)
    objetivo = models.TextField("Objetivo:",default=False)
    desarrollo_atividad= models.TextField("Desarrollo de la actividad:",default=False)
    Recursos= models.TextField("Material:",default=False)
    competencias_desarrollar=models.TextField("Competencias a desarrollar:",null=True,blank=True)
    url = models.URLField(max_length = 500,null=False,default=False)
    def __str__(self):
        return f"{self.nombreActividad}"
    
