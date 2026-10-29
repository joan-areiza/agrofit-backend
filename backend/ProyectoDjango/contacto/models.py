# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.

from django.db import models

# Create your models here.
class EstadosContacto(models.Model):
    id_estado_contacto_pk = models.AutoField(primary_key=True, blank=True, null=True)
    nombre_estado = models.CharField()

    class Meta:
        
        db_table = "estados_contacto"

class MensajesContacto(models.Model):
    id_mensaje_pk = models.AutoField(primary_key=True, blank=True, null=True)
    nombres_remitente = models.CharField()
    correo_remitente = models.CharField()
    titulo_mensaje = models.CharField()
    contenido_mensaje = models.TextField()
    fecha_envio = models.DateTimeField()
    id_estado_contacto_fk = models.ForeignKey(
        EstadosContacto, models.DO_NOTHING, db_column="id_estado_contacto_fk"
    )

    class Meta:
        
        db_table = "mensajes_contacto"