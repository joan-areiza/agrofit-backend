from django.contrib import admin
from .models import (
    EstadosAsignacion,
    AsignacionesRutinaUsuario,
    Asistencias,
    EvaluacionesFisicas,
    EstadosSeguimiento,
    SeguimientosProgresoUsuario,
)
class EstadosAsignacionAdmin(admin.ModelAdmin):
    list_display = ("id_estado_asignacion_pk", "nombre_estado_asignacion")
    search_fields = ("nombre_estado_asignacion",)


class AsignacionesRutinaUsuarioAdmin(admin.ModelAdmin):
    list_display = (
        "id_asignacion_rutina_usuario_pk",
        "id_rutina_fk",
        "id_usuario_fk",
        "fecha_hora_inicio_asignacion_rutina",
        "fecha_hora_fin_asignacion_rutina",
        "id_estado_asignacion_rutina_fk",
        "id_entrenador_asigna_rutina_fk",
    )
    list_filter = ("id_estado_asignacion_rutina_fk", "fecha_hora_inicio_asignacion_rutina")
    search_fields = (
        "id_usuario_fk__id_usuario_aprendiz_fk__nombres_usuario",
        "id_usuario_fk__id_usuario_aprendiz_fk__apellidos_usuario",
    )
    date_hierarchy = "fecha_hora_inicio_asignacion_rutina"


class AsistenciasAdmin(admin.ModelAdmin):
    list_display = (
        "id_asistencia_pk",
        "id_aprendiz_asistencia_fk",
        "id_entrenador_asistencia_fk",
        "id_rutina_asistencia_fk",
        "fecha_asistencia",
        "estado_asistencia",
    )
    list_filter = ("estado_asistencia", "fecha_asistencia")
    search_fields = (
        "id_aprendiz_asistencia_fk__id_usuario_aprendiz_fk__nombres_usuario",
        "id_aprendiz_asistencia_fk__id_usuario_aprendiz_fk__apellidos_usuario",
    )
    date_hierarchy = "fecha_asistencia"


class EvaluacionesFisicasAdmin(admin.ModelAdmin):
    list_display = (
        "id_evaluacion_fisica_pk",
        "id_usuario_evaluacion_fk",
        "id_entrenador_encargado_evaluacion_fk",
        "fecha_evaluacion",
        "peso_evaluacion",
        "altura_evaluacion",
        "imc_evaluacion",
        "presion_sistolica",
        "presion_diastolica",
    )
    list_filter = (
        "fecha_evaluacion",
        "id_nivel_actividad_fisica_evaluacion_fk",
        "id_complexion_fisica_evaluacion_fk",
    )
    search_fields = (
        "id_usuario_evaluacion_fk__nombres_usuario",
        "id_usuario_evaluacion_fk__apellidos_usuario",
        "id_usuario_evaluacion_fk__numero_documento_usuario",
    )
    date_hierarchy = "fecha_evaluacion"


class EstadosSeguimientoAdmin(admin.ModelAdmin):
    list_display = ("id_estado_seguimiento_pk", "nombre_estado_seguimiento")
    search_fields = ("nombre_estado_seguimiento",)


class SeguimientosProgresoUsuarioAdmin(admin.ModelAdmin):
    list_display = (
        "id_seguimiento_progreso_usuario_pk",
        "id_evaluacion_fisica_fk",
        "fecha_registro_progreso",
        "horas_ludicas",
        "rutinas_completadas",
        "id_estado_seguimiento_fk",
        "id_objetivo_actual_fk",
    )
    list_filter = ("id_estado_seguimiento_fk", "fecha_registro_progreso", "id_objetivo_actual_fk")
    search_fields = (
        "observacion_progreso_usuario",
        "logros_avances",
        "aspectos_a_mejorar",
    )
    date_hierarchy = "fecha_registro_progreso"

admin.site.register(EstadosAsignacion,EstadosAsignacionAdmin)
admin.site.register(AsignacionesRutinaUsuario,AsignacionesRutinaUsuarioAdmin)
admin.site.register(Asistencias,AsistenciasAdmin)
admin.site.register(EvaluacionesFisicas,EvaluacionesFisicasAdmin)
admin.site.register(EstadosSeguimiento,EstadosSeguimientoAdmin)
admin.site.register(SeguimientosProgresoUsuario,SeguimientosProgresoUsuarioAdmin)

