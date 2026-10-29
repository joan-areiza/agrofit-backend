# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.

from django.db import models


# Create your models here.
class EstadosRutina(models.Model):
    id_estado_rutina_pk = models.AutoField(primary_key=True, blank=True, null=True)
    nombre_estado_rutina = models.CharField(max_length=100)

    class Meta:

        db_table = "estados_rutina"


class NivelesActividadFisica(models.Model):
    id_nivel_actividad_fisica_pk = models.AutoField(
        primary_key=True, blank=True, null=True
    )
    nombre_nivel_actividad_fisica = models.CharField(max_length=100)

    class Meta:

        db_table = "niveles_actividad_fisica"


class NivelesRutina(models.Model):
    id_nivel_rutina_pk = models.AutoField(primary_key=True, blank=True, null=True)
    nombre_nivel_rutina = models.CharField(max_length=100)

    class Meta:

        db_table = "niveles_rutina"


class ObjetivosRutina(models.Model):
    id_objetivo_rutina_pk = models.AutoField(primary_key=True, blank=True, null=True)
    nombre_objetivo_rutina = models.CharField(max_length=150)
    descripcion_objetivo = models.TextField(blank=True, null=True)

    class Meta:

        db_table = "objetivos_rutina"


class PartesCuerpo(models.Model):
    id_parte_cuerpo_pk = models.AutoField(primary_key=True, blank=True, null=True)
    nombre_parte_cuerpo = models.CharField(max_length=60)
    descripcion_parte_cuerpo = models.TextField(blank=True, null=True)

    class Meta:

        db_table = "partes_cuerpo"


class TiposParticipacionMusculo(models.Model):
    tipo_participacion_musculo = models.AutoField(
        primary_key=True, blank=True, null=True
    )
    nombre_tipo_participacion_musculo = models.CharField(max_length=100)

    class Meta:

        db_table = "tipos_participacion_musculo"


class ComplexionesFisicas(models.Model):
    id_complexion_fisica_pk = models.AutoField(primary_key=True, blank=True, null=True)
    nombre_complexion_fisica = models.CharField(max_length=100)

    class Meta:

        db_table = "complexiones_fisicas"


class Musculos(models.Model):
    id_musculo_pk = models.AutoField(primary_key=True, blank=True, null=True)
    nombre_musculo = models.CharField(max_length=80)
    decripcion_musculo = models.TextField(blank=True, null=True)
    id_parte_cuerpo_musculo_fk = models.ForeignKey(
        "PartesCuerpo", models.DO_NOTHING, db_column="id_parte_cuerpo_musculo_fk"
    )

    class Meta:

        db_table = "musculos"


class Ejercicios(models.Model):
    id_ejercicio_pk = models.AutoField(primary_key=True, blank=True, null=True)
    nombre_ejercicio = models.CharField(max_length=100)
    repeticiones_ejercicio = models.IntegerField()
    descripcion_ejercicio = models.TextField(blank=True, null=True)
    url_video_demo_ejercicio = models.CharField(max_length=150)
    id_maquina_ejercicio_fk = models.ForeignKey(
        "Maquinas",
        models.DO_NOTHING,
        db_column="id_maquina_ejercicio_fk",
        blank=True,
        null=True,
    )
    carga_ejercicio = models.DecimalField(
        max_digits=10, decimal_places=5
    )  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    id_musculo_ejercicio_fk = models.ForeignKey(
        "Musculos", models.DO_NOTHING, db_column="id_musculo_ejercicio_fk"
    )

    class Meta:

        db_table = "ejercicios"


class EjerciciosMusculo(models.Model):
    id_ejercicio_musculo_pk = models.AutoField(primary_key=True, blank=True, null=True)
    id_ejercicio_fk = models.ForeignKey(
        Ejercicios, models.DO_NOTHING, db_column="id_ejercicio_fk"
    )
    id_musculo_fk = models.ForeignKey(
        "Musculos", models.DO_NOTHING, db_column="id_musculo_fk"
    )
    id_tipo_participacion_musculo_fk = models.ForeignKey(
        "TiposParticipacionMusculo",
        models.DO_NOTHING,
        db_column="id_tipo_participacion_musculo_fk",
    )

    class Meta:

        db_table = "ejercicios_musculo"


class Rutinas(models.Model):
    id_rutina_pk = models.AutoField(primary_key=True, blank=True, null=True)
    nombre_rutina = models.CharField(max_length=100)
    id_objetivo_rutina_fk = models.ForeignKey(
        ObjetivosRutina, models.DO_NOTHING, db_column="id_objetivo_rutina_fk"
    )
    id_nivel_rutina_fk = models.ForeignKey(
        NivelesRutina, models.DO_NOTHING, db_column="id_nivel_rutina_fk"
    )
    id_estado_rutina_fk = models.ForeignKey(
        EstadosRutina, models.DO_NOTHING, db_column="id_estado_rutina_fk"
    )

    class Meta:

        db_table = "rutinas"


class DetallesRutina(models.Model):
    id_detalle_rutina_pk = models.AutoField(primary_key=True, blank=True, null=True)
    series_rutina = models.IntegerField()
    repeticiones_rutina = models.IntegerField()
    id_rutina_fk = models.ForeignKey(
        "Rutinas", models.DO_NOTHING, db_column="id_rutina_fk"
    )
    id_ejercicio_rutina_fk = models.ForeignKey(
        "Ejercicios", models.DO_NOTHING, db_column="id_ejercicio_rutina_fk"
    )

    class Meta:

        db_table = "detalles_rutina"
