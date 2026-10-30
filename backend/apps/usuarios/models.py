# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.

from django.db import models

# Create your models here.
class Sexos(models.Model):
    cod_sexo_pk = models.CharField(max_length=6, primary_key=True)
    nombre_sexo = models.CharField(max_length=100)

    class Meta:

        db_table = "sexos"


class TiposDocumento(models.Model):
    cod_tipo_documento_pk = models.CharField(max_length=6, primary_key=True)
    nombre_tipo_documento = models.CharField(max_length=100)

    class Meta:

        db_table = "tipos_documento"


class TiposSangre(models.Model):
    cod_tipo_sangre_pk = models.CharField(max_length=6, primary_key=True)
    nombre_tipo_sangre = models.CharField(max_length=100)

    class Meta:

        db_table = "tipos_sangre"


class EstadosCivil(models.Model):
    id_estado_civil_pk = models.IntegerField(primary_key=True)
    nombre_estado_civil = models.CharField(max_length=100)

    class Meta:
        db_table = "estados_civil"


class Roles(models.Model):
    id_rol_pk = models.AutoField(primary_key=True)
    nombre_rol = models.CharField(max_length=100)

    class Meta:

        db_table = "roles"


class Hospitales(models.Model):
    cod_hospital_pk = models.CharField(max_length=6, primary_key=True)
    nombre_hospital = models.CharField(max_length=100)
    direccion_hospital = models.CharField(max_length=150)

    class Meta:

        db_table = "hospitales"


class Eps(models.Model):
    cod_eps_pk = models.CharField(max_length=6, primary_key=True)
    nombre_eps = models.CharField(max_length=100)
    telefono_eps = models.CharField(max_length=11)
    direccion_eps = models.CharField(max_length=150)

    class Meta:

        db_table = "eps"


class NivelesAdministrador(models.Model):
    id_nivel_administrador_pk = models.AutoField(primary_key=True)
    nombre_nivel_administrador = models.CharField(max_length=100)

    class Meta:

        db_table = "niveles_administrador"


class EspecialidadesEntrenador(models.Model):
    id_especialidad_entrenador_pk = models.AutoField(primary_key=True)
    nombre_especialidad_entrenador = models.CharField(max_length=100)

    class Meta:

        db_table = "especialidades_entrenador"


class EstadosAprendiz(models.Model):
    id_estado_aprendiz_pk = models.AutoField(primary_key=True)
    nombre_estado_aprendiz = models.CharField(max_length=100)

    class Meta:

        db_table = "estados_aprendiz"


class EstadosFuncionario(models.Model):
    id_estado_funcionario_pk = models.AutoField(primary_key=True)
    nombre_estado_funcionario = models.CharField(max_length=100)

    class Meta:

        db_table = "estados_funcionario"


class AntecedentesMedicos(models.Model):
    id_antecedente_medico_pk = models.AutoField(primary_key=True)
    nombre_antecedente_medico = models.CharField(max_length=100)

    class Meta:

        db_table = "antecedentes_medicos"


class Usuarios(models.Model):
    id_usuario_pk = models.AutoField(primary_key=True)
    numero_documento_usuario = models.CharField(max_length=11, unique=True)

    cod_tipo_documento_usuario_fk = models.ForeignKey(
        "TiposDocumento",
        models.DO_NOTHING,
        db_column="cod_tipo_documento_usuario_fk",
        to_field="cod_tipo_documento_pk",
    )

    correo_usuario = models.CharField(max_length=120, unique=True)
    telefono_usuario = models.CharField(max_length=11, blank=True, null=True)
    telefono_emergencia_usuario = models.CharField(max_length=11, blank=True, null=True)
    clave_usuario = models.CharField(max_length=64)
    nombres_usuario = models.CharField(max_length=100)
    apellidos_usuario = models.CharField(max_length=100)

    cod_sexo_usuario_fk = models.ForeignKey(
        "Sexos",
        models.DO_NOTHING,
        db_column="cod_sexo_usuario_fk",
        to_field="cod_sexo_pk",
    )

    cod_tipo_sangre_usuario_fk = models.ForeignKey(
        "TiposSangre",
        models.DO_NOTHING,
        db_column="cod_tipo_sangre_usuario_fk",
        to_field="cod_tipo_sangre_pk",
    )

    fecha_nacimiento_usuario = models.DateField()

    id_estado_civil_usuario_fk = models.ForeignKey(
        "EstadosCivil",
        models.DO_NOTHING,
        db_column="id_estado_civil_usuario_fk",
    )

    cod_departamento_usuario_fk = models.ForeignKey(
        "centros.Departamentos",
        models.DO_NOTHING,
        db_column="cod_departamento_usuario_fk",
        to_field="cod_departamento_pk",
    )

    cod_municipio_usuario_fk = models.ForeignKey(
        "centros.Municipios",
        models.DO_NOTHING,
        db_column="cod_municipio_usuario_fk",
        to_field="cod_municipio_pk",
    )

    direccion_usuario = models.CharField(max_length=150)
    foto_usuario = models.BinaryField(blank=True, null=True)
    fecha_registro_usuario = models.DateField()
    estado_usuario = models.BooleanField()

    id_rol_usuario_fk = models.ForeignKey(
        "Roles",
        models.DO_NOTHING,
        db_column="id_rol_usuario_fk",
    )

    id_hospital_usuario_fk = models.ForeignKey(
        "Hospitales",
        models.DO_NOTHING,
        db_column="id_hospital_usuario_fk",
        to_field="cod_hospital_pk",
    )

    id_eps_usuario_fk = models.ForeignKey(
        "Eps",
        models.DO_NOTHING,
        db_column="id_eps_usuario_fk",
        to_field="cod_eps_pk",
    )

    class Meta:
        db_table = "usuarios"


class Entrenadores(models.Model):
    id_entrenador_pk = models.AutoField(primary_key=True)
    id_usuario_entrenador_fk = models.ForeignKey(
        "Usuarios", models.DO_NOTHING, db_column="id_usuario_entrenador_fk"
    )
    id_especialidad_entrenador_fk = models.ForeignKey(
        "EspecialidadesEntrenador",
        models.DO_NOTHING,
        db_column="id_especialidad_entrenador_fk",
    )
    estado_entrenador = models.BooleanField()

    class Meta:
        db_table = "entrenadores"


class Administradores(models.Model):
    id_administrador_pk = models.AutoField(primary_key=True)
    id_usuario_administrador_fk = models.ForeignKey(
        "Usuarios",
        models.DO_NOTHING,
        db_column="id_usuario_administrador_fk",
        to_field="id_usuario_pk",
    )
    id_nivel_acceso_administrador_fk = models.ForeignKey(
        "NivelesAdministrador",
        models.DO_NOTHING,
        db_column="id_nivel_acceso_administrador_fk",
    )
    estado_administrador = models.BooleanField()  # This field type is a guess.

    class Meta:

        db_table = "administradores"


class Funcionarios(models.Model):
    id_funcionario_pk = models.AutoField(primary_key=True)
    id_usuario_funcionario_fk = models.ForeignKey(
        "Usuarios", models.DO_NOTHING, db_column="id_usuario_funcionario_fk"
    )
    id_dependencia_funcionario_fk = models.ForeignKey(
        "centros.DependenciasFuncionario",
        models.DO_NOTHING,
        db_column="id_dependencia_funcionario_fk",
    )
    id_estado_funcionario_fk = models.ForeignKey(
        "EstadosFuncionario", models.DO_NOTHING, db_column="id_estado_funcionario_fk"
    )

    class Meta:

        db_table = "funcionarios"


class Aprendices(models.Model):
    id_aprendiz_pk = models.AutoField(primary_key=True)
    id_usuario_aprendiz_fk = models.ForeignKey(
        "Usuarios",
        models.DO_NOTHING,
        db_column="id_usuario_aprendiz_fk",
        to_field="id_usuario_pk",
    )
    id_estado_aprendiz_fk = models.ForeignKey(
        "EstadosAprendiz", models.DO_NOTHING, db_column="id_estado_aprendiz_fk"
    )

    class Meta:

        db_table = "aprendices"


class FichasUsuarios(models.Model):
    id_ficha_usuario_pk = models.AutoField(primary_key=True)
    id_ficha_fk = models.ForeignKey(
        "programas.FichasFormacion", models.DO_NOTHING, db_column="id_ficha_fk"
    )
    id_usuario_ficha_fk = models.ForeignKey(
        "Usuarios", models.DO_NOTHING, db_column="id_usuario_ficha_fk"
    )
    fecha_inscripcion = models.DateField()

    class Meta:

        db_table = "fichas_usuarios"
