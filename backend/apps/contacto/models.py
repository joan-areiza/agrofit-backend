# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.

from django.db import models
from ckeditor.fields import RichTextField


# Create your models here.
class EstadosContacto(models.Model):
    id_estado_contacto_pk = models.AutoField(
        primary_key=True, verbose_name="ID de estado de contacto"
    )
    nombre_estado = models.CharField(max_length=50, verbose_name="Nombre de estado")

    class Meta:
        db_table = "estados_contacto"
        verbose_name = "Estado de contacto"
        verbose_name_plural = "Estados de contacto"
        ordering = ['nombre_estado']

    def __str__(self):
        return str(self.nombre_estado)


class MensajesContacto(models.Model):
    id_mensaje_pk = models.AutoField(primary_key=True, verbose_name="ID de mensaje")
    nombres_remitente = models.CharField(
        max_length=150, verbose_name="Nombres del remitente"
    )
    correo_remitente = models.CharField(
        max_length=150, verbose_name="Correo electrónico"
    )
    titulo_mensaje = models.CharField(max_length=150, verbose_name="Título del mensaje")
    contenido_mensaje = RichTextField(verbose_name="Contenido del mensaje")
    fecha_envio = models.DateTimeField(
        auto_now_add=True, verbose_name="Fecha de envío"
    )
    id_estado_contacto_fk = models.ForeignKey(
        "EstadosContacto",
        on_delete=models.CASCADE,
        db_column="id_estado_contacto_fk",
        verbose_name="Estado de contacto",
    )

    class Meta:
        db_table = "mensajes_contacto"
        verbose_name = "Mensaje de contacto"
        verbose_name_plural = "Mensajes de contacto"
        ordering = ['-fecha_envio']

    def __str__(self):
        return str(self.titulo_mensaje)
