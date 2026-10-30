# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.

from django.db import models

# Create your models here.
class EstadosAsignacion(models.Model):
    id_estado_asignacion_pk = models.AutoField(primary_key=True)
    nombre_estado_asignacion = models.CharField(max_length=100)

    class Meta:

        db_table = "estados_asignacion"


class AsignacionesRutinaUsuario(models.Model):
    id_asignacion_rutina_usuario_pk = models.AutoField(primary_key=True)
    id_rutina_fk = models.ForeignKey(
        "rutinas.Rutinas", models.DO_NOTHING, db_column="id_rutina_fk"
    )
    id_usuario_fk = models.ForeignKey(
        "usuarios.Aprendices", models.DO_NOTHING, db_column="id_usuario_fk"
    )
    fecha_hora_inicio_asignacion_rutina = models.DateTimeField()
    fecha_hora_fin_asignacion_rutina = models.DateTimeField()
    id_estado_asignacion_rutina_fk = models.ForeignKey(
        "EstadosAsignacion",
        models.DO_NOTHING,
        db_column="id_estado_asignacion_rutina_fk",
    )
    id_entrenador_asigna_rutina_fk = models.ForeignKey(
        "usuarios.Entrenadores", models.DO_NOTHING, db_column="id_entrenador_asigna_rutina_fk"
    )

    class Meta:

        db_table = "asignaciones_rutina_usuario"


class Asistencias(models.Model):
    id_asistencia_pk = models.AutoField(primary_key=True)
    id_aprendiz_asistencia_fk = models.ForeignKey(
        "usuarios.Aprendices", models.DO_NOTHING, db_column="id_aprendiz_asistencia_fk"
    )
    id_entrenador_asistencia_fk = models.ForeignKey(
        "usuarios.Entrenadores", models.DO_NOTHING, db_column="id_entrenador_asistencia_fk"
    )
    id_rutina_asistencia_fk = models.ForeignKey(
        "rutinas.Rutinas", models.DO_NOTHING, db_column="id_rutina_asistencia_fk"
    )
    fecha_asistencia = models.DateField()
    estado_asistencia = models.BooleanField()  # This field type is a guess.

    class Meta:

        db_table = "asistencias"


class EvaluacionesFisicas(models.Model):
    id_evaluacion_fisica_pk = models.AutoField(primary_key=True)
    peso_evaluacion = models.DecimalField(
        max_digits=10, decimal_places=5
    )  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    id_nivel_actividad_fisica_evaluacion_fk = models.ForeignKey(
        "rutinas.NivelesActividadFisica",
        models.DO_NOTHING,
        db_column="id_nivel_actividad_fisica_evaluacion_fk",
    )
    id_antecedente_medico_evaluacion_fk = models.ForeignKey(
        "usuarios.AntecedentesMedicos",
        models.DO_NOTHING,
        db_column="id_antecedente_medico_evaluacion_fk",
    )
    fecha_evaluacion = models.DateField()
    grasa_corporal_evaluacion = models.CharField(max_length=50)
    grasa_muscular_evaluacion = models.CharField(max_length=50)
    altura_evaluacion = models.DecimalField(
        max_digits=10, decimal_places=5
    )  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    observacion_evaluacion = models.TextField(blank=True, null=True)
    id_usuario_evaluacion_fk = models.ForeignKey(
        "usuarios.Usuarios", models.DO_NOTHING, db_column="id_usuario_evaluacion_fk"
    )
    id_entrenador_encargado_evaluacion_fk = models.ForeignKey(
        "usuarios.Entrenadores",
        models.DO_NOTHING,
        db_column="id_entrenador_encargado_evaluacion_fk",
    )
    id_complexion_fisica_evaluacion_fk = models.ForeignKey(
        "rutinas.ComplexionesFisicas",
        models.DO_NOTHING,
        db_column="id_complexion_fisica_evaluacion_fk",
    )
    presion_arterial = models.CharField(max_length=50)
    imc_evaluacion = models.DecimalField(
        max_digits=10, decimal_places=5
    )  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    medida_cintura = models.DecimalField(
        max_digits=10, decimal_places=5
    )  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    medida_cadera = models.DecimalField(
        max_digits=10, decimal_places=5
    )  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float

    class Meta:

        db_table = "evaluaciones_fisicas"


class EstadosSeguimiento(models.Model):
    id_estado_seguimiento_pk = models.AutoField(primary_key=True)
    nombre_estado_seguimiento = models.CharField(max_length=100)

    class Meta:

        db_table = "estados_seguimiento"


class SeguimientosProgresoUsuario(models.Model):
    id_seguimiento_progreso_usuario_pk = models.AutoField(primary_key=True)
    horas_ludicas = models.IntegerField()
    rutinas_completadas = models.IntegerField()
    fecha_registro_progreso = models.DateField()
    id_estado_seguimiento_fk = models.ForeignKey(
        "EstadosSeguimiento", models.DO_NOTHING, db_column="id_estado_seguimiento_fk"
    )
    id_evaluacion_fisica_fk = models.ForeignKey(
        "EvaluacionesFisicas", models.DO_NOTHING, db_column="id_evaluacion_fisica_fk"
    )
    observacion_progreso_usuario = models.TextField(blank=True, null=True)
    id_objetivo_actual_fk = models.ForeignKey(
        "rutinas.ObjetivosRutina", models.DO_NOTHING, db_column="id_objetivo_actual_fk"
    )
    logros_avances = models.TextField(blank=True, null=True)
    aspectos_a_mejorar = models.TextField(blank=True, null=True)

    class Meta:

        db_table = "seguimientos_progreso_usuario"
