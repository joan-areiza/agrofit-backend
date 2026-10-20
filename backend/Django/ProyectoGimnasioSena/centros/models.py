from django.db import models
from django.contrib.auth.models import nivel_fk
from django.contrib.auth.models import centro_fk
from django.contrib.auth.models import niveau_fk
from django.contrib.auth.models import programa_fk

# Create your models here.
class NivelesFormacion(models.Model):
    nombre_nivel = models.CharField(max_length=100, verbose_name='Nombre')

    class Meta:
        verbose_name = 'Nivel Formación'
        verbose_name_plural = 'Niveles Formación'

    def __str__(self):
        return self.nombre_nivel
    
class CentrosFormacion(models.Model):
    nombre_centro = models.CharField(max_length=100, verbose_name='Nombre')
    sigla = models.CharField(max_length=100, verbose_name='Nombre')
    direccion = models.CharField(max_length=255,verbose_name='Descripción')
    dias_permitidos = models.CharField(max_length=100, verbose_name='Nombre')
    idnivel_fk  = models.ForeignKey(nivel_fk, editable=False, verbose_name='Usuario', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Centro'
        verbose_name_plural = 'Centros'

    def __str__(self):
        return self.nombre_centro

class Dependencias(models.Model):
    nombre_dependencia = models.CharField(max_length=100, verbose_name='Nombre')
    idcentro_fk = models.ForeignKey(centro_fk, editable=False, verbose_name='Usuario', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Dependencia'
        verbose_name_plural = 'Dependencias'

    def __str__(self):
        return self.nombre_dependencia
    
class ProgramasFormacion(models.Model):
    nombre_programa = models.CharField(max_length=100, verbose_name='Nombre')
    sigla_programa = models.CharField(max_length=255,verbose_name='Descripción')
    idniveau_fk  = models.ForeignKey(niveau_fk, editable=False, verbose_name='Usuario', on_delete=models.CASCADE)
    idcentro_fk = models.ForeignKey(centro_fk, editable=False, verbose_name='Usuario', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Programa'
        verbose_name_plural = 'Programas'

    def __str__(self):
        return self.nombre_programa
    
class Fichas(models.Model):
    codigo_ficha = models.CharField(max_length=100, verbose_name='Nombre')
    idprograma_fk  = models.ForeignKey(programa_fk , editable=False, verbose_name='Usuario', on_delete=models.CASCADE)
    idcentro_fk = models.ForeignKey(centro_fk, editable=False, verbose_name='Usuario', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Creado el')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Creado el')
    jornada = models.CharField(max_length=100, verbose_name='Nombre')

    class Meta:
        verbose_name = 'Ficha'
        verbose_name_plural = 'Fichas'

    def __str__(self):
        return self.codigo_ficha