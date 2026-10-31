from django.contrib import admin
from .models import (
    Regiones,
    Departamentos,
    Municipios,
    CentrosFormacion,
    Sedes,
    DependenciasFuncionario,
)
class RegionesAdmin(admin.ModelAdmin):
    list_display = ("id_region_pk", "nombre_region")
    search_fields = ("nombre_region",)
class DepartamentosAdmin(admin.ModelAdmin):
    list_display = (
        "cod_departamento_pk",
        "nombre_departamento",
        "id_region_departamento_fk",
    )
    list_filter = ("id_region_departamento_fk",)
    search_fields = ("cod_departamento_pk", "nombre_departamento")
class MunicipiosAdmin(admin.ModelAdmin):
    list_display = (
        "cod_municipio_pk",
        "nombre_municipio",
        "cod_departamento_municipio_fk",
    )
    list_filter = ("cod_departamento_municipio_fk",)
    search_fields = ("cod_municipio_pk", "nombre_municipio")
class CentrosFormacionAdmin(admin.ModelAdmin):
    list_display = (
        "id_centro_pk",
        "cod_centro",
        "nombre_centro",
        "direccion_centro",
        "dias_permitidos",
        "cod_municipio_centro_fk",
    )
    list_filter = ("cod_municipio_centro_fk",)
    search_fields = ("cod_centro", "nombre_centro", "direccion_centro")
class SedesAdmin(admin.ModelAdmin):
    list_display = ("id_sede_pk", "nombre_sede", "direccion_sede", "id_centro_sede_fk")
    list_filter = ("id_centro_sede_fk",)
    search_fields = ("nombre_sede", "direccion_sede")
class DependenciasFuncionarioAdmin(admin.ModelAdmin):
    list_display = (
        "id_dependencia_funcionario_pk",
        "nombre_dependencia_funcionario",
        "id_centro_dependencia_fk",
    )
    list_filter = ("id_centro_dependencia_fk",)
    search_fields = ("nombre_dependencia_funcionario",)

admin.site.register(Regiones, RegionesAdmin)
admin.site.register(Departamentos, DepartamentosAdmin)
admin.site.register(Municipios, MunicipiosAdmin)
admin.site.register(CentrosFormacion, CentrosFormacionAdmin)
admin.site.register(Sedes, SedesAdmin)
admin.site.register(DependenciasFuncionario, DependenciasFuncionarioAdmin)
