# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.

from django.db import models


# Create your models here.
class Jornadas(models.Model):
    id_jornada_pk = models.AutoField(primary_key=True, verbose_name="ID de jornada")
    nombre_jornada = models.CharField(max_length=100, verbose_name="Nombre de jornada")
    estado_jornada = models.BooleanField(verbose_name="Estado")

    class Meta:
        db_table = "jornadas"
        verbose_name = "Jornada"
        verbose_name_plural = "Jornadas"

    def __str__(self):
        return str(self.nombre_jornada)


class Modalidades(models.Model):
    id_modalidad_pk = models.AutoField(primary_key=True, verbose_name="ID de modalidad")
    nombre_modalidad = models.CharField(
        max_length=100, verbose_name="Nombre de modalidad"
    )

    class Meta:
        db_table = "modalidades"
        verbose_name = "Modalidad"
        verbose_name_plural = "Modalidades"

    def __str__(self):
        return str(self.nombre_modalidad)


class NivelesFormacionPrograma(models.Model):
    id_niveles_formacion_programa_pk = models.AutoField(
        primary_key=True, verbose_name="ID de nivel de formación"
    )
    nombre_nivel_formacion_programa = models.CharField(
        max_length=100, verbose_name="Nombre de nivel de formación"
    )

    class Meta:
        db_table = "niveles_formacion_programa"
        verbose_name = "Nivel de formación"
        verbose_name_plural = "Niveles de formación"

    def __str__(self):
        return str(self.nombre_nivel_formacion_programa)


class RequisitosPrograma(models.Model):
    id_requisito_programa_pk = models.AutoField(
        primary_key=True, verbose_name="ID de requisito de programa"
    )
    nombre_requisito_programa = models.CharField(
        max_length=100, verbose_name="Nombre de requisito"
    )

    class Meta:
        db_table = "requisitos_programa"
        verbose_name = "Requisito de programa"
        verbose_name_plural = "Requisitos de programa"

    def __str__(self):
        return str(self.nombre_requisito_programa)


class ProgramasFormacion(models.Model):
    id_programa_pk = models.AutoField(primary_key=True, verbose_name="ID de programa")
    cod_programa = models.CharField(
        max_length=6, unique=True, verbose_name="Código de programa"
    )
    nombre_programa = models.CharField(
        max_length=200, verbose_name="Nombre de programa"
    )
    id_requisito_programa_fk = models.ForeignKey(
        "RequisitosPrograma",
        on_delete=models.CASCADE,
        db_column="id_requisito_programa_fk",
        verbose_name="Requisito",
    )
    duracion_programa = models.IntegerField(verbose_name="Duración (meses/horas)")
    id_centro_formacion_programa_fk = models.ForeignKey(
        "centros.CentrosFormacion",
        on_delete=models.CASCADE,
        db_column="id_centro_formacion_programa_fk",
        verbose_name="Centro de formación",
    )
    id_nivel_formacion_programa_fk = models.ForeignKey(
        NivelesFormacionPrograma,
        on_delete=models.CASCADE,
        db_column="id_nivel_formacion_programa_fk",
        verbose_name="Nivel de formación",
    )
    estado_programa = models.BooleanField(verbose_name="Estado")

    class Meta:
        db_table = "programas_formacion"
        verbose_name = "Programa de formación"
        verbose_name_plural = "Programas de formación"

    def __str__(self):
        return str(self.nombre_programa)


class FichasFormacion(models.Model):
    id_ficha_formacion_pk = models.AutoField(
        primary_key=True, verbose_name="ID de ficha"
    )
    numero_ficha = models.CharField(max_length=7, verbose_name="Número de ficha")
    id_programa_ficha_fk = models.ForeignKey(
        "ProgramasFormacion",
        on_delete=models.CASCADE,
        db_column="id_programa_ficha_fk",
        verbose_name="Programa de formación",
    )
    id_jornada_ficha_fk = models.ForeignKey(
        "Jornadas",
        on_delete=models.CASCADE,
        db_column="id_jornada_ficha_fk",
        verbose_name="Jornada",
    )
    id_sede_ficha_fk = models.ForeignKey(
        "centros.Sedes",
        on_delete=models.CASCADE,
        db_column="id_sede_ficha_fk",
        verbose_name="Sede",
    )
    fecha_inicio_ficha = models.DateField(verbose_name="Fecha de inicio")
    fecha_fin_ficha = models.DateField(verbose_name="Fecha de fin")
    estado_ficha = models.BooleanField(
        verbose_name="Estado"
    )  # This field type is a guess.
    id_modalidad_ficha_fk = models.ForeignKey(
        "Modalidades",
        on_delete=models.CASCADE,
        db_column="id_modalidad_ficha_fk",
        verbose_name="Modalidad",
    )
    id_instructor_lider_ficha_fk = models.ForeignKey(
        "usuarios.Funcionarios",
        on_delete=models.CASCADE,
        db_column="id_instructor_lider_ficha_fk",
        verbose_name="Instructor líder",
    )

    class Meta:
        db_table = "fichas_formacion"
        verbose_name = "Ficha de formación"
        verbose_name_plural = "Fichas de formación"

    def __str__(self):
        return str(self.numero_ficha)
