# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.

from django.db import models

# Create your models here.
class AsignacionesRutinaUsuario(models.Model):
    id_asignacion_rutina_usuario_pk = models.AutoField(
        primary_key=True, blank=True, null=True
    )
    id_rutina_fk = models.ForeignKey(
        "Rutinas", models.DO_NOTHING, db_column="id_rutina_fk"
    )
    id_usuario_fk = models.ForeignKey(
        Aprendices, models.DO_NOTHING, db_column="id_usuario_fk"
    )
    fecha_hora_inicio_asignacion_rutina = models.DateTimeField()
    fecha_hora_fin_asignacion_rutina = models.DateTimeField()
    estado_asignacion_rutina = models.TextField()  # This field type is a guess.
    id_entrenador_asigna_rutina_fk = models.ForeignKey(
        "Entrenadores", models.DO_NOTHING, db_column="id_entrenador_asigna_rutina_fk"
    )

    class Meta:
        
        db_table = "asignaciones_rutina_usuario"

class Asistencias(models.Model):
    id_asistencia_pk = models.AutoField(primary_key=True, blank=True, null=True)
    id_aprendiz_asistencia_fk = models.ForeignKey(
        Aprendices, models.DO_NOTHING, db_column="id_aprendiz_asistencia_fk"
    )
    id_entrenador_asistencia_fk = models.ForeignKey(
        "Entrenadores", models.DO_NOTHING, db_column="id_entrenador_asistencia_fk"
    )
    id_rutina_asistencia_fk = models.ForeignKey(
        "Rutinas", models.DO_NOTHING, db_column="id_rutina_asistencia_fk"
    )
    fecha_asistencia = models.DateField()
    estado_asistencia = models.TextField()  # This field type is a guess.

    class Meta:
        
        db_table = "asistencias"

class EvaluacionesFisicas(models.Model):
    id_evaluacion_fisica_pk = models.AutoField(primary_key=True, blank=True, null=True)
    peso_evaluacion = models.DecimalField(
        max_digits=10, decimal_places=5
    )  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    id_nivel_actividad_fisica_evaluacion_fk = models.ForeignKey(
        "NivelesActividadFisica",
        models.DO_NOTHING,
        db_column="id_nivel_actividad_fisica_evaluacion_fk",
    )
    id_antecedente_medico_evaluacion_fk = models.ForeignKey(
        AntecedentesMedicos,
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
    id_entrenador_encargado_evaluacion_fk = models.ForeignKey(
        Entrenadores,
        models.DO_NOTHING,
        db_column="id_entrenador_encargado_evaluacion_fk",
    )
    id_complexion_fisica_evaluacion_fk = models.ForeignKey(
        ComplexionesFisicas,
        models.DO_NOTHING,
        db_column="id_complexion_fisica_evaluacion_fk",
    )
    presion_arterial = models.CharField(max_length=50)
    id_usuario_evaluacion_fk = models.ForeignKey(
        "Usuarios", models.DO_NOTHING, db_column="id_usuario_evaluacion_fk"
    )

    class Meta:
        
        db_table = "evaluaciones_fisicas"

class SeguimientosProgresoUsuario(models.Model):
    id_seguimiento_progreso_usuario_pk = models.AutoField(
        primary_key=True, blank=True, null=True
    )
    horas_ludicas = models.IntegerField()
    id_usuario_progreso_fk = models.ForeignKey(
        "Usuarios", models.DO_NOTHING, db_column="id_usuario_progreso_fk"
    )
    rutinas_completadas = models.IntegerField()
    fecha_registro_progreso = models.DateField()
    observacion_progreso_usuario = models.TextField(blank=True, null=True)

    class Meta:
        
        db_table = "seguimientos_progreso_usuario"

