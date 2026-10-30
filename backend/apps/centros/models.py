# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.

from django.db import models


# Create your models here.
class Regiones(models.Model):
    id_region_pk = models.AutoField(primary_key=True)
    nombre_region = models.CharField(max_length=100)

    class Meta:

        db_table = "regiones"


class Departamentos(models.Model):
    cod_departamento_pk = models.CharField(max_length=6,primary_key=True)
    nombre_departamento = models.CharField(max_length=100)
    id_region_departamento_fk = models.ForeignKey(
        "Regiones", models.DO_NOTHING, db_column="id_region_departamento_fk"
    )

    class Meta:

        db_table = "departamentos"


class Municipios(models.Model):
    cod_municipio_pk = models.CharField(max_length=6,primary_key=True)
    nombre_municipio = models.CharField(max_length=150)
    cod_departamento_municipio_fk = models.ForeignKey(
        "Departamentos", models.DO_NOTHING, db_column="cod_departamento_municipio_fk"
    )

    class Meta:

        db_table = "municipios"


class CentrosFormacion(models.Model):
    id_centro_pk = models.AutoField(primary_key=True)
    cod_centro = models.CharField(max_length=6)
    nombre_centro = models.CharField(max_length=100)
    direccion_centro = models.CharField(max_length=150)
    dias_permitidos = models.IntegerField()
    cod_municipio_centro_fk = models.ForeignKey(
        "Municipios", models.DO_NOTHING, db_column="cod_municipio_centro_fk"
    )

    class Meta:

        db_table = "centros_formacion"


class Sedes(models.Model):
    id_sede_pk = models.AutoField(primary_key=True)
    nombre_sede = models.CharField(max_length=100)
    direccion_sede = models.CharField(max_length=50)
    id_centro_sede_fk = models.ForeignKey(
        "CentrosFormacion", models.DO_NOTHING, db_column="id_centro_sede_fk"
    )

    class Meta:
        db_table = "sedes"


class DependenciasFuncionario(models.Model):
    id_dependencia_funcionario_pk = models.AutoField(primary_key=True)
    nombre_dependencia_funcionario = models.CharField(max_length=100)
    id_centro_dependencia_fk = models.ForeignKey(
        "CentrosFormacion", models.DO_NOTHING, db_column="id_centro_dependencia_fk"
    )

    class Meta:

        db_table = "dependencias_funcionario"
