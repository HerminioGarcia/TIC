from django.db import models
from django.contrib.auth.models import User
from usuarios.validadores import  curp_validador
# Create your models here.
GENERO = [
    ('1', 'Masculino'),
    ('2', 'Femenino'),
    ('3', 'Otro'),
]

GRADO_STUDIO=[
    ('0', 'Ninguna'),
    ('1', 'Primara'),
    ('2', 'Secundaria'),
    ('3', 'Prepa'),
    ('4', 'Licenciatura'),
    ('5', 'Maestría'),
    ('6', 'Doctorado'),
    ('7', 'Posdoctorado'),
    ]

class DatosPersonales(models.Model):
    user = models.OneToOneField(User, verbose_name="Usuario", related_name='datos', on_delete=models.CASCADE)
    nombre = models.CharField(max_length=150)
    apellido_paterno = models.CharField(max_length=150)
    apellido_materno = models.CharField(max_length=150)
    genero = models.CharField('Género', max_length=1, choices=GENERO,default=1,null=False)
    fecha_nacimiento = models.DateField()
    grado_estudio = models.CharField('Último grado de estudios', max_length=1, choices=GRADO_STUDIO,default=1,null=False)
    instituto = models.CharField("Institución a la que pertenece",max_length=150,null=False)
    curp = models.CharField("C.U.R.P.", max_length=18, validators=[curp_validador],unique=True)