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
    id_estado_asignacion_pk = models.AutoField(
        primary_key=True, verbose_name="ID de estado de asignación"
    )
    nombre_estado_asignacion = models.CharField(
        max_length=100, verbose_name="Nombre de estado de asignación"
    )

    class Meta:
        db_table = "estados_asignacion"
        verbose_name = "Estado de asignación"
        verbose_name_plural = "Estados de asignación"
        ordering = ['nombre_estado_asignacion']

    def __str__(self):
        return str(self.nombre_estado_asignacion)


class AsignacionesRutinaUsuario(models.Model):
    id_asignacion_rutina_usuario_pk = models.AutoField(
        primary_key=True, verbose_name="ID de asignación de rutina"
    )
    id_rutina_fk = models.ForeignKey(
        "rutinas.Rutinas",
        on_delete=models.CASCADE,
        db_column="id_rutina_fk",
        verbose_name="Rutina",
    )
    id_usuario_fk = models.ForeignKey(
        "usuarios.Aprendices",
        on_delete=models.CASCADE,
        db_column="id_usuario_fk",
        verbose_name="Usuario",
    )
    fecha_hora_inicio_asignacion_rutina = models.DateTimeField(
        auto_now_add=True, verbose_name="Fecha y hora de inicio"
    )
    fecha_hora_fin_asignacion_rutina = models.DateTimeField(
        verbose_name="Fecha y hora de fin"
    )
    id_estado_asignacion_rutina_fk = models.ForeignKey(
        "EstadosAsignacion",
        on_delete=models.CASCADE,
        db_column="id_estado_asignacion_rutina_fk",
        verbose_name="Estado de asignación",
    )
    id_entrenador_asigna_rutina_fk = models.ForeignKey(
        "usuarios.Entrenadores",
        on_delete=models.CASCADE,
        db_column="id_entrenador_asigna_rutina_fk",
        verbose_name="Entrenador que asigna",
    )

    class Meta:
        db_table = "asignaciones_rutina_usuario"
        verbose_name = "Asignación de rutina a usuario"
        verbose_name_plural = "Asignaciones de rutina a usuarios"
        ordering = ['-fecha_hora_inicio_asignacion_rutina']

    def __str__(self):
        return f"Rutina {self.id_rutina_fk} - Aprendiz {self.id_usuario_fk}"


class Asistencias(models.Model):
    id_asistencia_pk = models.AutoField(
        primary_key=True, verbose_name="ID de asistencia"
    )
    id_aprendiz_asistencia_fk = models.ForeignKey(
        "usuarios.Aprendices",
        on_delete=models.CASCADE,
        db_column="id_aprendiz_asistencia_fk",
        verbose_name="Aprendiz",
    )
    id_entrenador_asistencia_fk = models.ForeignKey(
        "usuarios.Entrenadores",
        on_delete=models.CASCADE,
        db_column="id_entrenador_asistencia_fk",
        verbose_name="Entrenador a cargo",
    )
    id_rutina_asistencia_fk = models.ForeignKey(
        "rutinas.Rutinas",
        on_delete=models.CASCADE,
        db_column="id_rutina_asistencia_fk",
        verbose_name="Rutina",
    )
    fecha_asistencia = models.DateTimeField(
        auto_now_add=True, verbose_name="Fecha y hora de asistencia"
    )
    estado_asistencia = models.BooleanField(
        verbose_name="Estado"
    )  # This field type is a guess.

    class Meta:
        db_table = "asistencias"
        verbose_name = "Asistencia"
        verbose_name_plural = "Asistencias"
        ordering = ['-fecha_asistencia']

    def __str__(self):
        return (
            f"Asistencia de {self.id_aprendiz_asistencia_fk} ({self.fecha_asistencia})"
        )


class EvaluacionesFisicas(models.Model):
    id_evaluacion_fisica_pk = models.AutoField(
        primary_key=True, verbose_name="ID de evaluación física"
    )
    peso_evaluacion = models.DecimalField(
        max_digits=5, decimal_places=2, verbose_name="Peso (kg)"
    )
    id_nivel_actividad_fisica_evaluacion_fk = models.ForeignKey(
        "rutinas.NivelesActividadFisica",
        on_delete=models.CASCADE,
        db_column="id_nivel_actividad_fisica_evaluacion_fk",
        verbose_name="Nivel de actividad física",
    )
    id_antecedente_medico_evaluacion_fk = models.ForeignKey(
        "usuarios.AntecedentesMedicos",
        on_delete=models.CASCADE,
        db_column="id_antecedente_medico_evaluacion_fk",
        verbose_name="Antecedente médico",
    )
    fecha_evaluacion = models.DateTimeField(
        auto_now=True, verbose_name="Fecha de evaluación"
    )
    grasa_corporal_evaluacion = models.DecimalField(
        max_digits=4, decimal_places=2, verbose_name="Grasa corporal (%)"
    )
    grasa_muscular_evaluacion = models.DecimalField(
        max_digits=5, decimal_places=2, verbose_name="Masa muscular (kg)"
    )
    altura_evaluacion = models.DecimalField(
        max_digits=3, decimal_places=2, verbose_name="Altura (m)"
    )
    observacion_evaluacion = models.TextField(
        default=None, blank=True, null=True, verbose_name="Observaciones"
    )
    id_usuario_evaluacion_fk = models.ForeignKey(
        "usuarios.Usuarios",
        on_delete=models.CASCADE,
        db_column="id_usuario_evaluacion_fk",
        verbose_name="Usuario",
    )
    id_entrenador_encargado_evaluacion_fk = models.ForeignKey(
        "usuarios.Entrenadores",
        on_delete=models.CASCADE,
        db_column="id_entrenador_encargado_evaluacion_fk",
        verbose_name="Entrenador encargado",
    )
    id_complexion_fisica_evaluacion_fk = models.ForeignKey(
        "rutinas.ComplexionesFisicas",
        on_delete=models.CASCADE,
        db_column="id_complexion_fisica_evaluacion_fk",
        verbose_name="Complexión física",
    )
    presion_sistolica = models.SmallIntegerField(verbose_name="Presión sistólica")
    presion_diastolica = models.SmallIntegerField(verbose_name="Presión diastólica")
    imc_evaluacion = models.DecimalField(
        max_digits=4, decimal_places=2, verbose_name="IMC"
    )
    medida_cintura = models.DecimalField(
        max_digits=5, decimal_places=2, verbose_name="Medida de cintura (cm)"
    )
    medida_cadera = models.DecimalField(
        max_digits=5, decimal_places=2, verbose_name="Medida de cadera (cm)"
    )

    class Meta:
        db_table = "evaluaciones_fisicas"
        verbose_name = "Evaluación física"
        verbose_name_plural = "Evaluaciones físicas"
        ordering = ['-fecha_evaluacion']

    def __str__(self):
        return f"Evaluación {self.id_evaluacion_fisica_pk}"


class EstadosSeguimiento(models.Model):
    id_estado_seguimiento_pk = models.AutoField(
        primary_key=True, verbose_name="ID de estado de seguimiento"
    )
    nombre_estado_seguimiento = models.CharField(
        max_length=100, verbose_name="Nombre de estado de seguimiento"
    )

    class Meta:
        db_table = "estados_seguimiento"
        verbose_name = "Estado de seguimiento"
        verbose_name_plural = "Estados de seguimiento"
        ordering = ['nombre_estado_seguimiento']

    def __str__(self):
        return str(self.nombre_estado_seguimiento)


class SeguimientosProgresoUsuario(models.Model):
    id_seguimiento_progreso_usuario_pk = models.AutoField(
        primary_key=True, verbose_name="ID de seguimiento de progreso"
    )
    horas_ludicas = models.IntegerField(verbose_name="Horas lúdicas")
    rutinas_completadas = models.IntegerField(verbose_name="Rutinas completadas")
    fecha_registro_progreso = models.DateTimeField(
        auto_now=True, verbose_name="Fecha de registro de progreso"
    )
    id_estado_seguimiento_fk = models.ForeignKey(
        "EstadosSeguimiento",
        on_delete=models.CASCADE,
        db_column="id_estado_seguimiento_fk",
        verbose_name="Estado de seguimiento",
    )
    id_evaluacion_fisica_fk = models.ForeignKey(
        "EvaluacionesFisicas",
        on_delete=models.CASCADE,
        db_column="id_evaluacion_fisica_fk",
        verbose_name="Evaluación física",
    )
    observacion_progreso_usuario = models.TextField(
        default=None, blank=True, null=True, verbose_name="Observaciones"
    )
    id_objetivo_actual_fk = models.ForeignKey(
        "rutinas.ObjetivosRutina",
        on_delete=models.CASCADE,
        db_column="id_objetivo_actual_fk",
        verbose_name="Objetivo actual",
    )
    logros_avances = models.TextField(
        default=None, blank=True, null=True, verbose_name="Logros y avances"
    )
    aspectos_a_mejorar = models.TextField(
        default=None, blank=True, null=True, verbose_name="Aspectos a mejorar"
    )

    class Meta:
        db_table = "seguimientos_progreso_usuario"
        verbose_name = "Seguimiento de progreso de usuario"
        verbose_name_plural = "Seguimientos de progreso de usuario"
        ordering = ['-fecha_registro_progreso']

    def __str__(self):
        return f"Seguimiento {self.id_seguimiento_progreso_usuario_pk}"
