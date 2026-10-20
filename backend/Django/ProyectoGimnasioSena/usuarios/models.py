from django.db import models

# Create your models here.
class TipoDocumento(models.Model):
    nombre_nivel = models.CharField(max_length=100, verbose_name='Nombre')

    class Meta:
        verbose_name = 'Nivel Formación'
        verbose_name_plural = 'Niveles Formación'

    def __str__(self):
        return self.nombre_nivel