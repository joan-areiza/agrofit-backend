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
    id_tipo_maquina_pk = models.AutoField(
        primary_key=True, verbose_name="ID de tipo de máquina"
    )
    nombre_tipo_maquina = models.CharField(
        max_length=100, verbose_name="Nombre de tipo de máquina"
    )

    class Meta:

        db_table = "tipos_maquina"
        verbose_name = "Tipo de máquina"
        verbose_name_plural = "Tipos de máquina"

    def __str__(self):
        return str(self.nombre_tipo_maquina)


class EstadosMaquina(models.Model):
    id_estado_maquina_pk = models.AutoField(
        primary_key=True, verbose_name="ID de estado de máquina"
    )
    nombre_estado_maquina = models.CharField(
        max_length=100, verbose_name="Nombre de estado de máquina"
    )

    class Meta:
        db_table = "estados_maquina"
        verbose_name = "Estado de máquina"
        verbose_name_plural = "Estados de máquina"

    def __str__(self):
        return str(self.nombre_estado_maquina)


class Maquinas(models.Model):
    id_maquina_pk = models.AutoField(primary_key=True, verbose_name="ID de máquina")
    cod_inventario = models.CharField(
        max_length=6, unique=True, verbose_name="Código de inventario"
    )
    nombre_maquina = models.CharField(max_length=100, verbose_name="Nombre de máquina")
    id_estado_maquina_fk = models.ForeignKey(
        "EstadosMaquina",
        on_delete=models.CASCADE,
        db_column="id_estado_maquina_fk",
        verbose_name="Estado de máquina",
    )
    id_tipo_maquina_fk = models.ForeignKey(
        "TiposMaquina",
        on_delete=models.CASCADE,
        db_column="id_tipo_maquina_fk",
        verbose_name="Tipo de máquina",
    )
    descripcion_maquina = models.TextField(
        default=None, blank=True, null=True, verbose_name="Descripción"
    )

    class Meta:
        db_table = "maquinas"
        verbose_name = "Máquina"
        verbose_name_plural = "Máquinas"

    def __str__(self):
        return str(self.nombre_maquina)


class Horarios(models.Model):
    id_horario_pk = models.AutoField(primary_key=True, verbose_name="ID de horario")
    id_jornada_horario_fk = models.ForeignKey(
        "programas.Jornadas",
        on_delete=models.CASCADE,
        db_column="id_jornada_horario_fk",
        verbose_name="Jornada",
    )
    hora_inicio_horario = models.TimeField(verbose_name="Hora de inicio")
    hora_fin_horario = models.TimeField(verbose_name="Hora de fin")
    cupo_maximo_horario = models.IntegerField(verbose_name="Cupo máximo")
    id_entrenador_horario_fk = models.ForeignKey(
        "usuarios.Entrenadores",
        on_delete=models.CASCADE,
        db_column="id_entrenador_horario_fk",
        verbose_name="Entrenador",
    )
    estado_horario = models.BooleanField(verbose_name="Estado")

    class Meta:
        db_table = "horarios"
        verbose_name = "Horario"
        verbose_name_plural = "Horarios"

    def __str__(self):
        return f"{self.hora_inicio_horario} - {self.hora_fin_horario}"
