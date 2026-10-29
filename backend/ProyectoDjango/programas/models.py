# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.

from django.db import models
from centros.models import CentrosFormacion


# Create your models here.
class Jornadas(models.Model):
    id_jornada_pk = models.AutoField(primary_key=True, blank=True, null=True)
    nombre_jornada = models.CharField(max_length=100)
    estado_jornada = models.TextField()  # This field type is a guess.

    class Meta:

        db_table = "jornadas"


class Modalidades(models.Model):
    id_modalidad_pk = models.AutoField(primary_key=True, blank=True, null=True)
    nombre_modalidad = models.CharField(max_length=100)

    class Meta:

        db_table = "modalidades"


class NivelesFormacionPrograma(models.Model):
    id_niveles_formacion_programa_pk = models.AutoField(
        primary_key=True, blank=True, null=True
    )
    nombre_nivel_formacion_programa = models.CharField(max_length=100)

    class Meta:

        db_table = "niveles_formacion_programa"


class RequisitosPrograma(models.Model):
    id_requisito_programa_pk = models.AutoField(primary_key=True, blank=True, null=True)
    nombre_requisito_programa = models.CharField(max_length=100)

    class Meta:

        db_table = "requisitos_programa"


class ProgramasFormacion(models.Model):
    id_programa_pk = models.AutoField(primary_key=True, blank=True, null=True)
    cod_programa_pk = models.CharField(max_length=6)
    nombre_programa = models.CharField(max_length=200)
    id_requisito_programa_fk = models.ForeignKey(
        "RequisitosPrograma", models.DO_NOTHING, db_column="id_requisito_programa_fk"
    )
    duracion_programa = models.IntegerField()
    id_centro_formacion_programa_fk = models.ForeignKey(
        CentrosFormacion, models.DO_NOTHING, db_column="id_centro_formacion_programa_fk"
    )
    id_nivel_formacion_programa_fk = models.ForeignKey(
        NivelesFormacionPrograma,
        models.DO_NOTHING,
        db_column="id_nivel_formacion_programa_fk",
    )
    estado_programa = models.TextField()  # This field type is a guess.

    class Meta:

        db_table = "programas_formacion"


class FichasFormacion(models.Model):
    id_ficha_formacion_pk = models.AutoField(primary_key=True, blank=True, null=True)
    numero_ficha = models.CharField(max_length=7)
    id_programa_ficha_fk = models.ForeignKey(
        "ProgramasFormacion", models.DO_NOTHING, db_column="id_programa_ficha_fk"
    )
    id_jornada_ficha_fk = models.ForeignKey(
        "Jornadas", models.DO_NOTHING, db_column="id_jornada_ficha_fk"
    )
    id_sede_ficha_fk = models.ForeignKey(
        "Sedes", models.DO_NOTHING, db_column="id_sede_ficha_fk"
    )
    fecha_inicio_ficha = models.DateField()
    fecha_fin_ficha = models.DateField()
    estado_ficha = models.TextField()  # This field type is a guess.
    id_modalidad_ficha_fk = models.ForeignKey(
        "Modalidades", models.DO_NOTHING, db_column="id_modalidad_ficha_fk"
    )
    id_instructor_lider_ficha_fk = models.ForeignKey(
        "Funcionarios", models.DO_NOTHING, db_column="id_instructor_lider_ficha_fk"
    )

    class Meta:

        db_table = "fichas_formacion"
