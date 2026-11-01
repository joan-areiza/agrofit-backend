from django.contrib import admin
from .models import (
    EstadosRutina,
    NivelesActividadFisica,
    NivelesRutina,
    ObjetivosRutina,
    PartesCuerpo,
    TiposParticipacionMusculo,
    ComplexionesFisicas,
    Musculos,
    Ejercicios,
    EjerciciosMusculo,
    Rutinas,
    DetallesRutina,
)

class EstadosRutinaAdmin(admin.ModelAdmin):
    list_display = ("id_estado_rutina_pk", "nombre_estado_rutina")
    search_fields = ("nombre_estado_rutina",)
class NivelesActividadFisicaAdmin(admin.ModelAdmin):
    list_display = ("id_nivel_actividad_fisica_pk", "nombre_nivel_actividad_fisica")
    search_fields = ("nombre_nivel_actividad_fisica",)
class NivelesRutinaAdmin(admin.ModelAdmin):
    list_display = ("id_nivel_rutina_pk", "nombre_nivel_rutina")
    search_fields = ("nombre_nivel_rutina",)
class ObjetivosRutinaAdmin(admin.ModelAdmin):
    list_display = ("id_objetivo_rutina_pk", "nombre_objetivo_rutina")
    search_fields = ("nombre_objetivo_rutina", "descripcion_objetivo")
class PartesCuerpoAdmin(admin.ModelAdmin):
    list_display = ("id_parte_cuerpo_pk", "nombre_parte_cuerpo")
    search_fields = ("nombre_parte_cuerpo", "descripcion_parte_cuerpo")
class TiposParticipacionMusculoAdmin(admin.ModelAdmin):
    list_display = ("id_tipo_participacion_musculo_pk", "nombre_tipo_participacion_musculo")
    search_fields = ("nombre_tipo_participacion_musculo",)
class ComplexionesFisicasAdmin(admin.ModelAdmin):
    list_display = ("id_complexion_fisica_pk", "nombre_complexion_fisica")
    search_fields = ("nombre_complexion_fisica",)
class MusculosAdmin(admin.ModelAdmin):
    list_display = ("id_musculo_pk", "nombre_musculo", "id_parte_cuerpo_musculo_fk")
    list_filter = ("id_parte_cuerpo_musculo_fk",)
    search_fields = ("nombre_musculo", "descripcion_musculo")
class EjerciciosAdmin(admin.ModelAdmin):
    list_display = (
        "id_ejercicio_pk",
        "nombre_ejercicio",
        "id_musculo_ejercicio_fk",
        "id_maquina_ejercicio_fk",
        "url_video_demo_ejercicio",
    )
    list_filter = ("id_musculo_ejercicio_fk", "id_maquina_ejercicio_fk")
    search_fields = ("nombre_ejercicio", "descripcion_ejercicio")
class EjerciciosMusculoAdmin(admin.ModelAdmin):
    list_display = (
        "id_ejercicio_musculo_pk",
        "id_ejercicio_fk",
        "id_musculo_fk",
        "id_tipo_participacion_musculo_fk",
    )
    list_filter = ("id_tipo_participacion_musculo_fk", "id_musculo_fk")
    search_fields = (
        "id_ejercicio_fk__nombre_ejercicio",
        "id_musculo_fk__nombre_musculo",
    )
class RutinasAdmin(admin.ModelAdmin):
    list_display = (
        "id_rutina_pk",
        "nombre_rutina",
        "id_objetivo_rutina_fk",
        "id_nivel_rutina_fk",
        "id_estado_rutina_fk",
    )
    list_filter = ("id_objetivo_rutina_fk", "id_nivel_rutina_fk", "id_estado_rutina_fk")
    search_fields = ("nombre_rutina",)
class DetallesRutinaAdmin(admin.ModelAdmin):
    list_display = (
        "id_detalle_rutina_pk",
        "id_rutina_fk",
        "id_ejercicio_rutina_fk",
        "series_rutina",
        "repeticiones_rutina",
        "carga_rutina",
        "descanso_segundos",
    )
    list_filter = ("id_rutina_fk",)
    search_fields = (
        "id_rutina_fk__nombre_rutina",
        "id_ejercicio_rutina_fk__nombre_ejercicio",
    )

admin.site.register(EstadosRutina,EstadosRutinaAdmin)
admin.site.register(NivelesActividadFisica,NivelesActividadFisicaAdmin)
admin.site.register(NivelesRutina,NivelesRutinaAdmin)
admin.site.register(ObjetivosRutina,ObjetivosRutinaAdmin)
admin.site.register(PartesCuerpo,PartesCuerpoAdmin)
admin.site.register(TiposParticipacionMusculo,TiposParticipacionMusculoAdmin)
admin.site.register(ComplexionesFisicas,ComplexionesFisicasAdmin)
admin.site.register(Musculos,MusculosAdmin)
admin.site.register(Ejercicios,EjerciciosAdmin)
admin.site.register(EjerciciosMusculo,EjerciciosMusculoAdmin)
admin.site.register(Rutinas,RutinasAdmin)
admin.site.register(DetallesRutina,DetallesRutinaAdmin)
