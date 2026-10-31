from django.contrib import admin
from .models import (
    Sexos,
    TiposDocumento,
    TiposSangre,
    EstadosCivil,
    Roles,
    Hospitales,
    Eps,
    NivelesAdministrador,
    EspecialidadesEntrenador,
    EstadosAprendiz,
    EstadosFuncionario,
    AntecedentesMedicos,
    Usuarios,
    Entrenadores,
    Administradores,
    Funcionarios,
    Aprendices,
    FichasUsuarios,
)


class SexosAdmin(admin.ModelAdmin):
    list_display = ("cod_sexo_pk", "nombre_sexo")
    search_fields = ("nombre_sexo",)


class TiposDocumentoAdmin(admin.ModelAdmin):
    list_display = ("cod_tipo_documento_pk", "nombre_tipo_documento")
    search_fields = ("nombre_tipo_documento",)


class TiposSangreAdmin(admin.ModelAdmin):
    list_display = ("cod_tipo_sangre_pk", "nombre_tipo_sangre")
    search_fields = ("nombre_tipo_sangre",)


class EstadosCivilAdmin(admin.ModelAdmin):
    list_display = ("id_estado_civil_pk", "nombre_estado_civil")
    search_fields = ("nombre_estado_civil",)


class RolesAdmin(admin.ModelAdmin):
    list_display = ("id_rol_pk", "nombre_rol")
    search_fields = ("nombre_rol",)


class HospitalesAdmin(admin.ModelAdmin):
    list_display = ("cod_hospital_pk", "nombre_hospital", "direccion_hospital")
    search_fields = ("nombre_hospital", "direccion_hospital")


class EpsAdmin(admin.ModelAdmin):
    list_display = ("cod_eps_pk", "nombre_eps", "telefono_eps", "direccion_eps")
    search_fields = ("nombre_eps",)


class NivelesAdministradorAdmin(admin.ModelAdmin):
    list_display = ("id_nivel_administrador_pk", "nombre_nivel_administrador")
    search_fields = ("nombre_nivel_administrador",)


class EspecialidadesEntrenadorAdmin(admin.ModelAdmin):
    list_display = ("id_especialidad_entrenador_pk", "nombre_especialidad_entrenador")
    search_fields = ("nombre_especialidad_entrenador",)


class EstadosAprendizAdmin(admin.ModelAdmin):
    list_display = ("id_estado_aprendiz_pk", "nombre_estado_aprendiz")
    search_fields = ("nombre_estado_aprendiz",)


class EstadosFuncionarioAdmin(admin.ModelAdmin):
    list_display = ("id_estado_funcionario_pk", "nombre_estado_funcionario")
    search_fields = ("nombre_estado_funcionario",)


class AntecedentesMedicosAdmin(admin.ModelAdmin):
    list_display = ("id_antecedente_medico_pk", "nombre_antecedente_medico")
    search_fields = ("nombre_antecedente_medico",)


class UsuariosAdmin(admin.ModelAdmin):
    list_display = (
        "id_usuario_pk",
        "numero_documento_usuario",
        "nombres_usuario",
        "apellidos_usuario",
        "correo_usuario",
        "estado_usuario",
        "id_rol_usuario_fk",
    )
    list_filter = ("estado_usuario", "id_rol_usuario_fk", "cod_sexo_usuario_fk")
    search_fields = (
        "numero_documento_usuario",
        "nombres_usuario",
        "apellidos_usuario",
        "correo_usuario",
    )
    readonly_fields = ("fecha_registro_usuario",)


class EntrenadoresAdmin(admin.ModelAdmin):
    list_display = (
        "id_entrenador_pk",
        "id_usuario_entrenador_fk",
        "id_especialidad_entrenador_fk",
        "estado_entrenador",
    )
    list_filter = ("estado_entrenador", "id_especialidad_entrenador_fk")
    search_fields = (
        "id_usuario_entrenador_fk__nombres_usuario",
        "id_usuario_entrenador_fk__apellidos_usuario",
    )


class AdministradoresAdmin(admin.ModelAdmin):
    list_display = (
        "id_administrador_pk",
        "id_usuario_administrador_fk",
        "id_nivel_acceso_administrador_fk",
        "estado_administrador",
    )
    list_filter = ("estado_administrador", "id_nivel_acceso_administrador_fk")
    search_fields = (
        "id_usuario_administrador_fk__nombres_usuario",
        "id_usuario_administrador_fk__apellidos_usuario",
    )


class FuncionariosAdmin(admin.ModelAdmin):
    list_display = (
        "id_funcionario_pk",
        "id_usuario_funcionario_fk",
        "id_dependencia_funcionario_fk",
        "id_estado_funcionario_fk",
    )
    list_filter = ("id_estado_funcionario_fk", "id_dependencia_funcionario_fk")
    search_fields = (
        "id_usuario_funcionario_fk__nombres_usuario",
        "id_usuario_funcionario_fk__apellidos_usuario",
    )


class AprendicesAdmin(admin.ModelAdmin):
    list_display = ("id_aprendiz_pk", "id_usuario_aprendiz_fk", "id_estado_aprendiz_fk")
    list_filter = ("id_estado_aprendiz_fk",)
    search_fields = (
        "id_usuario_aprendiz_fk__nombres_usuario",
        "id_usuario_aprendiz_fk__apellidos_usuario",
        "id_usuario_aprendiz_fk__numero_documento_usuario",
    )


class FichasUsuariosAdmin(admin.ModelAdmin):
    list_display = (
        "id_ficha_usuario_pk",
        "id_ficha_fk",
        "id_usuario_ficha_fk",
        "fecha_inscripcion",
    )
    list_filter = ("fecha_inscripcion",)
    search_fields = (
        "id_usuario_ficha_fk__nombres_usuario",
        "id_usuario_ficha_fk__apellidos_usuario",
        "id_ficha_fk__numero_ficha",
    )

admin.site.register(Sexos,SexosAdmin)
admin.site.register(TiposDocumento,TiposDocumentoAdmin)
admin.site.register(TiposSangre,TiposSangreAdmin)
admin.site.register(EstadosCivil,EstadosCivilAdmin)
admin.site.register(Roles,RolesAdmin)
admin.site.register(Hospitales,HospitalesAdmin)
admin.site.register(Eps,EpsAdmin)
admin.site.register(NivelesAdministrador,NivelesAdministradorAdmin)
admin.site.register(EspecialidadesEntrenador,EspecialidadesEntrenadorAdmin)
admin.site.register(EstadosAprendiz,EstadosAprendizAdmin)
admin.site.register(EstadosFuncionario,EstadosFuncionarioAdmin)
admin.site.register(AntecedentesMedicos,AntecedentesMedicosAdmin)
admin.site.register(Usuarios,UsuariosAdmin)
admin.site.register(Entrenadores,EntrenadoresAdmin)
admin.site.register(Administradores,AdministradoresAdmin)
admin.site.register(Funcionarios,FuncionariosAdmin)
admin.site.register(Aprendices,AprendicesAdmin)
admin.site.register(FichasUsuarios,FichasUsuariosAdmin)
