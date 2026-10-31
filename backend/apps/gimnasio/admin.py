from django.contrib import admin
from .models import TiposMaquina, EstadosMaquina, Maquinas, Horarios
class TiposMaquinaAdmin(admin.ModelAdmin):
    list_display = ("id_tipo_maquina_pk", "nombre_tipo_maquina")
    search_fields = ("nombre_tipo_maquina",)
class EstadosMaquinaAdmin(admin.ModelAdmin):
    list_display = ("id_estado_maquina_pk", "nombre_estado_maquina")
    search_fields = ("nombre_estado_maquina",)
class MaquinasAdmin(admin.ModelAdmin):
    list_display = (
        "id_maquina_pk",
        "cod_inventario",
        "nombre_maquina",
        "id_estado_maquina_fk",
        "id_tipo_maquina_fk",
    )
    list_filter = ("id_estado_maquina_fk", "id_tipo_maquina_fk")
    search_fields = ("cod_inventario", "nombre_maquina", "descripcion_maquina")
class HorariosAdmin(admin.ModelAdmin):
    list_display = (
        "id_horario_pk",
        "id_jornada_horario_fk",
        "hora_inicio_horario",
        "hora_fin_horario",
        "cupo_maximo_horario",
        "id_entrenador_horario_fk",
        "estado_horario",
    )
    list_filter = ("estado_horario", "id_jornada_horario_fk")
    search_fields = (
        "id_entrenador_horario_fk__id_usuario_entrenador_fk__nombres_usuario",
        "id_entrenador_horario_fk__id_usuario_entrenador_fk__apellidos_usuario",
    )

admin.site.register(TiposMaquina,TiposMaquinaAdmin)
admin.site.register(EstadosMaquina,EstadosMaquinaAdmin)
admin.site.register(Maquinas,MaquinasAdmin)
admin.site.register(Horarios,HorariosAdmin)
