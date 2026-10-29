# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.

from django.db import models

# Create your models here.
class TiposMaquina(models.Model):
    id_tipo_maquina_pk = models.AutoField(primary_key=True, blank=True, null=True)
    nombre_tipo_maquina = models.CharField(max_length=100)

    class Meta:
        
        db_table = "tipos_maquina"

class Maquinas(models.Model):
    id_maquina_pk = models.AutoField(primary_key=True, blank=True, null=True)
    nombre_maquina = models.CharField(max_length=100)
    estado_maquina = models.TextField()  # This field type is a guess.
    id_tipo_maquina_fk = models.ForeignKey(
        "TiposMaquina", models.DO_NOTHING, db_column="id_tipo_maquina_fk"
    )
    descripcion_maquina = models.TextField(blank=True, null=True)

    class Meta:
        
        db_table = "maquinas"

class Horarios(models.Model):
    id_horario_pk = models.AutoField(primary_key=True, blank=True, null=True)
    id_jornada_horario_fk = models.ForeignKey(
        "Jornadas", models.DO_NOTHING, db_column="id_jornada_horario_fk"
    )
    hora_inicio_horario = models.TimeField()
    hora_fin_horario = models.TimeField()
    cupo_maximo_horario = models.IntegerField()
    id_entrenador_horario_fk = models.ForeignKey(
        Entrenadores, models.DO_NOTHING, db_column="id_entrenador_horario_fk"
    )
    estado_horario = models.TextField()  # This field type is a guess.

    class Meta:
        
        db_table = "horarios"