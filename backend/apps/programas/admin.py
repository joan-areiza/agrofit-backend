from django.contrib import admin
from .models import (
    Jornadas,
    Modalidades,
    NivelesFormacionPrograma,
    RequisitosPrograma,
    ProgramasFormacion,
    FichasFormacion,
)

class JornadasAdmin(admin.ModelAdmin):
    list_display = ("id_jornada_pk", "nombre_jornada", "estado_jornada")
    list_filter = ("estado_jornada",)
    search_fields = ("nombre_jornada",)

class ModalidadesAdmin(admin.ModelAdmin):
    list_display = ("id_modalidad_pk", "nombre_modalidad")
    search_fields = ("nombre_modalidad",)
class NivelesFormacionProgramaAdmin(admin.ModelAdmin):
    list_display = ("id_niveles_formacion_programa_pk", "nombre_nivel_formacion_programa")
    search_fields = ("nombre_nivel_formacion_programa",)
class RequisitosProgramaAdmin(admin.ModelAdmin):
    list_display = ("id_requisito_programa_pk", "nombre_requisito_programa")
    search_fields = ("nombre_requisito_programa",)
class ProgramasFormacionAdmin(admin.ModelAdmin):
    list_display = (
        "id_programa_pk",
        "cod_programa",
        "nombre_programa",
        "duracion_programa",
        "id_requisito_programa_fk",
        "id_centro_formacion_programa_fk",
        "id_nivel_formacion_programa_fk",
        "estado_programa",
    )
    list_filter = (
        "estado_programa",
        "id_nivel_formacion_programa_fk",
        "id_requisito_programa_fk",
        "id_centro_formacion_programa_fk",
    )
    search_fields = ("cod_programa", "nombre_programa")
class FichasFormacionAdmin(admin.ModelAdmin):
    list_display = (
        "id_ficha_formacion_pk",
        "numero_ficha",
        "id_programa_ficha_fk",
        "id_jornada_ficha_fk",
        "id_sede_ficha_fk",
        "fecha_inicio_ficha",
        "fecha_fin_ficha",
        "estado_ficha",
        "id_modalidad_ficha_fk",
        "id_instructor_lider_ficha_fk",
    )
    list_filter = (
        "estado_ficha",
        "id_jornada_ficha_fk",
        "id_modalidad_ficha_fk",
        "id_sede_ficha_fk",
        "fecha_inicio_ficha",
    )
    search_fields = (
        "numero_ficha",
        "id_programa_ficha_fk__nombre_programa",
        "id_programa_ficha_fk__cod_programa",
    )
    date_hierarchy = "fecha_inicio_ficha"

admin.site.register(Jornadas,JornadasAdmin)
admin.site.register(Modalidades,ModalidadesAdmin)
admin.site.register(NivelesFormacionPrograma,NivelesFormacionProgramaAdmin)
admin.site.register(RequisitosPrograma,RequisitosProgramaAdmin)
admin.site.register(ProgramasFormacion,ProgramasFormacionAdmin)
admin.site.register(FichasFormacion,FichasFormacionAdmin)
