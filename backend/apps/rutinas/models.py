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
    id_estado_rutina_pk = models.AutoField(
        primary_key=True, verbose_name="ID de estado de rutina"
    )
    nombre_estado_rutina = models.CharField(
        max_length=100, verbose_name="Nombre de estado de rutina"
    )

    class Meta:
        db_table = "estados_rutina"
        verbose_name = "Estado de rutina"
        verbose_name_plural = "Estados de rutina"
        ordering = ['nombre_estado_rutina']

    def __str__(self):
        return str(self.nombre_estado_rutina)


class NivelesActividadFisica(models.Model):
    id_nivel_actividad_fisica_pk = models.AutoField(
        primary_key=True, verbose_name="ID de nivel de actividad física"
    )
    nombre_nivel_actividad_fisica = models.CharField(
        max_length=100, verbose_name="Nombre de nivel de actividad física"
    )

    class Meta:
        db_table = "niveles_actividad_fisica"
        verbose_name = "Nivel de actividad física"
        verbose_name_plural = "Niveles de actividad física"
        ordering = ['nombre_nivel_actividad_fisica']

    def __str__(self):
        return str(self.nombre_nivel_actividad_fisica)


class NivelesRutina(models.Model):
    id_nivel_rutina_pk = models.AutoField(
        primary_key=True, verbose_name="ID de nivel de rutina"
    )
    nombre_nivel_rutina = models.CharField(
        max_length=100, verbose_name="Nombre de nivel de rutina"
    )

    class Meta:
        db_table = "niveles_rutina"
        verbose_name = "Nivel de rutina"
        verbose_name_plural = "Niveles de rutina"
        ordering = ['nombre_nivel_rutina']

    def __str__(self):
        return str(self.nombre_nivel_rutina)


class ObjetivosRutina(models.Model):
    id_objetivo_rutina_pk = models.AutoField(
        primary_key=True, verbose_name="ID de objetivo de rutina"
    )
    nombre_objetivo_rutina = models.CharField(
        max_length=150, verbose_name="Nombre de objetivo de rutina"
    )
    descripcion_objetivo = models.TextField(
        default=None, blank=True, null=True, verbose_name="Descripción"
    )

    class Meta:
        db_table = "objetivos_rutina"
        verbose_name = "Objetivo de rutina"
        verbose_name_plural = "Objetivos de rutina"
        ordering = ['nombre_objetivo_rutina']

    def __str__(self):
        return str(self.nombre_objetivo_rutina)


class PartesCuerpo(models.Model):
    id_parte_cuerpo_pk = models.AutoField(
        primary_key=True, verbose_name="ID de parte del cuerpo"
    )
    nombre_parte_cuerpo = models.CharField(
        max_length=60, verbose_name="Nombre de parte del cuerpo"
    )
    descripcion_parte_cuerpo = models.TextField(
        default=None, blank=True, null=True, verbose_name="Descripción"
    )

    class Meta:
        db_table = "partes_cuerpo"
        verbose_name = "Parte del cuerpo"
        verbose_name_plural = "Partes del cuerpo"
        ordering = ['nombre_parte_cuerpo']

    def __str__(self):
        return str(self.nombre_parte_cuerpo)


class TiposParticipacionMusculo(models.Model):
    id_tipo_participacion_musculo_pk = models.AutoField(
        primary_key=True, verbose_name="ID de tipo de participación muscular"
    )
    nombre_tipo_participacion_musculo = models.CharField(
        max_length=100, verbose_name="Nombre de tipo de participación muscular"
    )

    class Meta:
        db_table = "tipos_participacion_musculo"
        verbose_name = "Tipo de participación muscular"
        verbose_name_plural = "Tipos de participación muscular"
        ordering = ['nombre_tipo_participacion_musculo']

    def __str__(self):
        return str(self.nombre_tipo_participacion_musculo)


class ComplexionesFisicas(models.Model):
    id_complexion_fisica_pk = models.AutoField(
        primary_key=True, verbose_name="ID de complexión física"
    )
    nombre_complexion_fisica = models.CharField(
        max_length=100, verbose_name="Nombre de complexión física"
    )

    class Meta:
        db_table = "complexiones_fisicas"
        verbose_name = "Complexión física"
        verbose_name_plural = "Complexiones físicas"
        ordering = ['nombre_complexion_fisica']

    def __str__(self):
        return str(self.nombre_complexion_fisica)


class Musculos(models.Model):
    id_musculo_pk = models.AutoField(primary_key=True, verbose_name="ID de músculo")
    nombre_musculo = models.CharField(max_length=80, verbose_name="Nombre de músculo")
    descripcion_musculo = models.TextField(
        default=None, blank=True, null=True, verbose_name="Descripción"
    )
    id_parte_cuerpo_musculo_fk = models.ForeignKey(
        "PartesCuerpo",
        on_delete=models.CASCADE,
        db_column="id_parte_cuerpo_musculo_fk",
        verbose_name="Parte del cuerpo",
    )

    class Meta:
        db_table = "musculos"
        verbose_name = "Músculo"
        verbose_name_plural = "Músculos"
        ordering = ['nombre_musculo']

    def __str__(self):
        return str(self.nombre_musculo)


class Ejercicios(models.Model):
    id_ejercicio_pk = models.AutoField(primary_key=True, verbose_name="ID de ejercicio")
    nombre_ejercicio = models.CharField(
        max_length=100, verbose_name="Nombre de ejercicio"
    )
    descripcion_ejercicio = models.TextField(
        default=None, blank=True, null=True, verbose_name="Descripción"
    )
    url_video_demo_ejercicio = models.CharField(
        max_length=150, verbose_name="URL de video demostrativo"
    )
    id_maquina_ejercicio_fk = models.ForeignKey(
        "gimnasio.Maquinas",
        on_delete=models.CASCADE,
        db_column="id_maquina_ejercicio_fk",
        verbose_name="Máquina",
    )
    id_musculo_ejercicio_fk = models.ForeignKey(
        "Musculos",
        on_delete=models.CASCADE,
        db_column="id_musculo_ejercicio_fk",
        verbose_name="Músculo principal",
    )

    class Meta:
        db_table = "ejercicios"
        verbose_name = "Ejercicio"
        verbose_name_plural = "Ejercicios"
        ordering = ['nombre_ejercicio']

    def __str__(self):
        return str(self.nombre_ejercicio)


class EjerciciosMusculo(models.Model):
    id_ejercicio_musculo_pk = models.AutoField(
        primary_key=True, verbose_name="ID de relación ejercicio-músculo"
    )
    id_ejercicio_fk = models.ForeignKey(
        "Ejercicios",
        on_delete=models.CASCADE,
        db_column="id_ejercicio_fk",
        verbose_name="Ejercicio",
    )
    id_musculo_fk = models.ForeignKey(
        "Musculos",
        on_delete=models.CASCADE,
        db_column="id_musculo_fk",
        verbose_name="Músculo",
    )
    id_tipo_participacion_musculo_fk = models.ForeignKey(
        "TiposParticipacionMusculo",
        on_delete=models.CASCADE,
        db_column="id_tipo_participacion_musculo_fk",
        verbose_name="Tipo de participación",
    )

    class Meta:
        db_table = "ejercicios_musculo"
        verbose_name = "Participación muscular en ejercicio"
        verbose_name_plural = "Participaciones musculares en ejercicios"
        ordering = ['id_ejercicio_fk']

    def __str__(self):
        return f"{self.id_ejercicio_fk} - {self.id_musculo_fk} ({self.id_tipo_participacion_musculo_fk})"


class Rutinas(models.Model):
    id_rutina_pk = models.AutoField(primary_key=True, verbose_name="ID de rutina")
    nombre_rutina = models.CharField(max_length=100, verbose_name="Nombre de rutina")
    id_objetivo_rutina_fk = models.ForeignKey(
        "ObjetivosRutina",
        on_delete=models.CASCADE,
        db_column="id_objetivo_rutina_fk",
        verbose_name="Objetivo de rutina",
    )
    id_nivel_rutina_fk = models.ForeignKey(
        "NivelesRutina",
        on_delete=models.CASCADE,
        db_column="id_nivel_rutina_fk",
        verbose_name="Nivel de rutina",
    )
    id_estado_rutina_fk = models.ForeignKey(
        "EstadosRutina",
        on_delete=models.CASCADE,
        db_column="id_estado_rutina_fk",
        verbose_name="Estado de rutina",
    )

    class Meta:
        db_table = "rutinas"
        verbose_name = "Rutina"
        verbose_name_plural = "Rutinas"
        ordering = ['nombre_rutina']

    def __str__(self):
        return str(self.nombre_rutina)


class DetallesRutina(models.Model):
    id_detalle_rutina_pk = models.AutoField(
        primary_key=True, verbose_name="ID de detalle de rutina"
    )
    series_rutina = models.IntegerField(verbose_name="Series")
    repeticiones_rutina = models.IntegerField(verbose_name="Repeticiones")
    carga_rutina = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        default=None,
        null=True,
        blank=True,
        verbose_name="Carga (kg)",
    )
    descanso_segundos = models.IntegerField(verbose_name="Descanso (segundos)")
    id_rutina_fk = models.ForeignKey(
        "Rutinas",
        on_delete=models.CASCADE,
        db_column="id_rutina_fk",
        verbose_name="Rutina",
    )
    id_ejercicio_rutina_fk = models.ForeignKey(
        "Ejercicios",
        on_delete=models.CASCADE,
        db_column="id_ejercicio_rutina_fk",
        verbose_name="Ejercicio",
    )

    class Meta:
        db_table = "detalles_rutina"
        verbose_name = "Detalle de rutina"
        verbose_name_plural = "Detalles de rutina"
        ordering = ['id_detalle_rutina_pk']

    def __str__(self):
        return f"Rutina {self.id_rutina_fk} - {self.id_ejercicio_rutina_fk} ({self.series_rutina}x{self.repeticiones_rutina})"
