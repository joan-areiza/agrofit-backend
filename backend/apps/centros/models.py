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
    id_region_pk = models.AutoField(primary_key=True, verbose_name="ID de región")
    nombre_region = models.CharField(max_length=100, verbose_name="Nombre de región")

    class Meta:

        db_table = "regiones"
        verbose_name = "Región"
        verbose_name_plural = "Regiones"
        ordering = ['nombre_region']

    def __str__(self):
        return str(self.nombre_region)


class Departamentos(models.Model):
    cod_departamento_pk = models.CharField(
        max_length=6, primary_key=True, verbose_name="Código de departamento"
    )
    nombre_departamento = models.CharField(
        max_length=100, verbose_name="Nombre de departamento"
    )
    id_region_departamento_fk = models.ForeignKey(
        "Regiones",
        on_delete=models.CASCADE,
        db_column="id_region_departamento_fk",
        verbose_name="Región",
    )

    class Meta:

        db_table = "departamentos"
        verbose_name = "Departamento"
        verbose_name_plural = "Departamentos"
        ordering = ['nombre_departamento']

    def __str__(self):
        return str(self.nombre_departamento)


class Municipios(models.Model):
    cod_municipio_pk = models.CharField(
        max_length=6, primary_key=True, verbose_name="Código de municipio"
    )
    nombre_municipio = models.CharField(
        max_length=150, verbose_name="Nombre de municipio"
    )
    cod_departamento_municipio_fk = models.ForeignKey(
        "Departamentos",
        on_delete=models.CASCADE,
        db_column="cod_departamento_municipio_fk",
        verbose_name="Departamento",
    )

    class Meta:

        db_table = "municipios"
        verbose_name = "Municipio"
        verbose_name_plural = "Municipios"
        ordering = ['nombre_municipio']

    def __str__(self):
        return str(self.nombre_municipio)


class CentrosFormacion(models.Model):
    id_centro_pk = models.AutoField(primary_key=True, verbose_name="ID de centro")
    cod_centro = models.CharField(
        max_length=6, unique=True, verbose_name="Código de centro"
    )
    nombre_centro = models.CharField(max_length=100, verbose_name="Nombre de centro")
    direccion_centro = models.CharField(max_length=150, verbose_name="Dirección")
    dias_permitidos = models.IntegerField(verbose_name="Días permitidos")
    cod_municipio_centro_fk = models.ForeignKey(
        "Municipios",
        on_delete=models.CASCADE,
        db_column="cod_municipio_centro_fk",
        verbose_name="Municipio",
    )

    class Meta:

        db_table = "centros_formacion"
        verbose_name = "Centro de formación"
        verbose_name_plural = "Centros de formación"
        ordering = ['nombre_centro']

    def __str__(self):
        return str(self.nombre_centro)


class Sedes(models.Model):
    id_sede_pk = models.AutoField(primary_key=True, verbose_name="ID de sede")
    nombre_sede = models.CharField(max_length=100, verbose_name="Nombre de sede")
    direccion_sede = models.CharField(max_length=50, verbose_name="Dirección")
    id_centro_sede_fk = models.ForeignKey(
        "CentrosFormacion",
        on_delete=models.CASCADE,
        db_column="id_centro_sede_fk",
        verbose_name="Centro de formación",
    )

    class Meta:
        db_table = "sedes"
        verbose_name = "Sede"
        verbose_name_plural = "Sedes"
        ordering = ['nombre_sede']

    def __str__(self):
        return str(self.nombre_sede)


class DependenciasFuncionario(models.Model):
    id_dependencia_funcionario_pk = models.AutoField(
        primary_key=True, verbose_name="ID de dependencia de funcionario"
    )
    nombre_dependencia_funcionario = models.CharField(
        max_length=100, verbose_name="Nombre de dependencia"
    )
    id_centro_dependencia_fk = models.ForeignKey(
        "CentrosFormacion",
        on_delete=models.CASCADE,
        db_column="id_centro_dependencia_fk",
        verbose_name="Centro de formación",
    )

    class Meta:

        db_table = "dependencias_funcionario"
        verbose_name = "Dependencia de funcionario"
        verbose_name_plural = "Dependencias de funcionario"
        ordering = ['nombre_dependencia_funcionario']

    def __str__(self):
        return str(self.nombre_dependencia_funcionario)
