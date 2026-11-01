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
    cod_sexo_pk = models.CharField(
        max_length=6, primary_key=True, verbose_name="Código de sexo"
    )
    nombre_sexo = models.CharField(max_length=100, verbose_name="Nombre de sexo")

    class Meta:
        db_table = "sexos"
        verbose_name = "Sexo"
        verbose_name_plural = "Sexos"
        ordering = ['nombre_sexo']

    def __str__(self):
        return str(self.nombre_sexo)


class TiposDocumento(models.Model):
    cod_tipo_documento_pk = models.CharField(
        max_length=6, primary_key=True, verbose_name="Código de tipo de documento"
    )
    nombre_tipo_documento = models.CharField(
        max_length=100, verbose_name="Nombre de tipo de documento"
    )

    class Meta:
        db_table = "tipos_documento"
        verbose_name = "Tipo de documento"
        verbose_name_plural = "Tipos de documento"
        ordering = ['nombre_tipo_documento']

    def __str__(self):
        return str(self.nombre_tipo_documento)


class TiposSangre(models.Model):
    cod_tipo_sangre_pk = models.CharField(
        max_length=6, primary_key=True, verbose_name="Código de tipo de sangre"
    )
    nombre_tipo_sangre = models.CharField(
        max_length=100, verbose_name="Nombre de tipo de sangre"
    )

    class Meta:
        db_table = "tipos_sangre"
        verbose_name = "Tipo de sangre"
        verbose_name_plural = "Tipos de sangre"
        ordering = ['nombre_tipo_sangre']

    def __str__(self):
        return str(self.nombre_tipo_sangre)


class EstadosCivil(models.Model):
    id_estado_civil_pk = models.AutoField(
        primary_key=True, verbose_name="ID de estado civil"
    )
    nombre_estado_civil = models.CharField(
        max_length=100, verbose_name="Nombre de estado civil"
    )

    class Meta:
        db_table = "estados_civil"
        verbose_name = "Estado civil"
        verbose_name_plural = "Estados civiles"
        ordering = ['nombre_estado_civil']

    def __str__(self):
        return str(self.nombre_estado_civil)


class Roles(models.Model):
    id_rol_pk = models.AutoField(primary_key=True, verbose_name="ID de rol")
    nombre_rol = models.CharField(max_length=100, verbose_name="Nombre de rol")

    class Meta:
        db_table = "roles"
        verbose_name = "Rol"
        verbose_name_plural = "Roles"
        ordering = ['nombre_rol']

    def __str__(self):
        return str(self.nombre_rol)


class Hospitales(models.Model):
    cod_hospital_pk = models.CharField(
        max_length=6, primary_key=True, verbose_name="Código de hospital"
    )
    nombre_hospital = models.CharField(
        max_length=100, verbose_name="Nombre de hospital"
    )
    direccion_hospital = models.CharField(max_length=150, verbose_name="Dirección")

    class Meta:
        db_table = "hospitales"
        verbose_name = "Hospital"
        verbose_name_plural = "Hospitales"
        ordering = ['nombre_hospital']

    def __str__(self):
        return str(self.nombre_hospital)


class Eps(models.Model):
    cod_eps_pk = models.CharField(
        max_length=6, primary_key=True, verbose_name="Código de EPS"
    )
    nombre_eps = models.CharField(max_length=100, verbose_name="Nombre de EPS")
    telefono_eps = models.CharField(max_length=11, verbose_name="Teléfono")
    direccion_eps = models.CharField(max_length=150, verbose_name="Dirección")

    class Meta:
        db_table = "eps"
        verbose_name = "EPS"
        verbose_name_plural = "EPS"
        ordering = ['nombre_eps']

    def __str__(self):
        return str(self.nombre_eps)


class NivelesAdministrador(models.Model):
    id_nivel_administrador_pk = models.AutoField(
        primary_key=True, verbose_name="ID de nivel de administrador"
    )
    nombre_nivel_administrador = models.CharField(
        max_length=100, verbose_name="Nombre de nivel de administrador"
    )

    class Meta:
        db_table = "niveles_administrador"
        verbose_name = "Nivel de administrador"
        verbose_name_plural = "Niveles de administrador"
        ordering = ['nombre_nivel_administrador']

    def __str__(self):
        return str(self.nombre_nivel_administrador)


class EspecialidadesEntrenador(models.Model):
    id_especialidad_entrenador_pk = models.AutoField(
        primary_key=True, verbose_name="ID de especialidad de entrenador"
    )
    nombre_especialidad_entrenador = models.CharField(
        max_length=100, verbose_name="Nombre de especialidad de entrenador"
    )

    class Meta:
        db_table = "especialidades_entrenador"
        verbose_name = "Especialidad de entrenador"
        verbose_name_plural = "Especialidades de entrenador"
        ordering = ['nombre_especialidad_entrenador']

    def __str__(self):
        return str(self.nombre_especialidad_entrenador)


class EstadosAprendiz(models.Model):
    id_estado_aprendiz_pk = models.AutoField(
        primary_key=True, verbose_name="ID de estado de aprendiz"
    )
    nombre_estado_aprendiz = models.CharField(
        max_length=100, verbose_name="Nombre de estado de aprendiz"
    )

    class Meta:
        db_table = "estados_aprendiz"
        verbose_name = "Estado de aprendiz"
        verbose_name_plural = "Estados de aprendiz"
        ordering = ['nombre_estado_aprendiz']

    def __str__(self):
        return str(self.nombre_estado_aprendiz)


class EstadosFuncionario(models.Model):
    id_estado_funcionario_pk = models.AutoField(
        primary_key=True, verbose_name="ID de estado de funcionario"
    )
    nombre_estado_funcionario = models.CharField(
        max_length=100, verbose_name="Nombre de estado de funcionario"
    )

    class Meta:
        db_table = "estados_funcionario"
        verbose_name = "Estado de funcionario"
        verbose_name_plural = "Estados de funcionario"
        ordering = ['nombre_estado_funcionario']

    def __str__(self):
        return str(self.nombre_estado_funcionario)


class AntecedentesMedicos(models.Model):
    id_antecedente_medico_pk = models.AutoField(
        primary_key=True, verbose_name="ID de antecedente médico"
    )
    nombre_antecedente_medico = models.CharField(
        max_length=100, verbose_name="Nombre de antecedente médico"
    )

    class Meta:
        db_table = "antecedentes_medicos"
        verbose_name = "Antecedente médico"
        verbose_name_plural = "Antecedentes médicos"
        ordering = ['nombre_antecedente_medico']

    def __str__(self):
        return str(self.nombre_antecedente_medico)


class Usuarios(models.Model):
    id_usuario_pk = models.AutoField(primary_key=True, verbose_name="ID de usuario")
    numero_documento_usuario = models.CharField(
        max_length=11, unique=True, verbose_name="Número de documento"
    )
    cod_tipo_documento_usuario_fk = models.ForeignKey(
        "TiposDocumento",
        on_delete=models.CASCADE,
        db_column="cod_tipo_documento_usuario_fk",
        to_field="cod_tipo_documento_pk",
        verbose_name="Tipo de documento",
    )
    correo_usuario = models.CharField(
        max_length=120, unique=True, verbose_name="Correo electrónico"
    )
    telefono_usuario = models.CharField(
        default=None,
        max_length=11,
        blank=True,
        null=True,
        verbose_name="Teléfono",
    )
    telefono_emergencia_usuario = models.CharField(
        default=None,
        max_length=11,
        blank=True,
        null=True,
        verbose_name="Teléfono de emergencia",
    )
    clave_usuario = models.CharField(max_length=64, verbose_name="Contraseña")
    nombres_usuario = models.CharField(max_length=100, verbose_name="Nombres")
    apellidos_usuario = models.CharField(max_length=100, verbose_name="Apellidos")
    cod_sexo_usuario_fk = models.ForeignKey(
        "Sexos",
        on_delete=models.CASCADE,
        db_column="cod_sexo_usuario_fk",
        to_field="cod_sexo_pk",
        verbose_name="Sexo",
    )
    cod_tipo_sangre_usuario_fk = models.ForeignKey(
        "TiposSangre",
        on_delete=models.CASCADE,
        db_column="cod_tipo_sangre_usuario_fk",
        to_field="cod_tipo_sangre_pk",
        verbose_name="Tipo de sangre",
    )
    fecha_nacimiento_usuario = models.DateField(verbose_name="Fecha de nacimiento")
    id_estado_civil_usuario_fk = models.ForeignKey(
        "EstadosCivil",
        on_delete=models.CASCADE,
        db_column="id_estado_civil_usuario_fk",
        verbose_name="Estado civil",
    )
    cod_departamento_usuario_fk = models.ForeignKey(
        "centros.Departamentos",
        on_delete=models.CASCADE,
        db_column="cod_departamento_usuario_fk",
        to_field="cod_departamento_pk",
        verbose_name="Departamento",
    )
    cod_municipio_usuario_fk = models.ForeignKey(
        "centros.Municipios",
        on_delete=models.CASCADE,
        db_column="cod_municipio_usuario_fk",
        to_field="cod_municipio_pk",
        verbose_name="Municipio",
    )
    direccion_usuario = models.CharField(max_length=150, verbose_name="Dirección")
    foto_usuario = models.ImageField(
        default=None,
        blank=True,
        null=True,
        upload_to="users",
        verbose_name="Foto",
    )
    fecha_registro_usuario = models.DateTimeField(
        auto_now_add=True, verbose_name="Fecha de registro"
    )
    estado_usuario = models.BooleanField(verbose_name="Estado de usuario")
    id_rol_usuario_fk = models.ForeignKey(
        "Roles",
        on_delete=models.CASCADE,
        db_column="id_rol_usuario_fk",
        verbose_name="Rol",
    )
    cod_hospital_usuario_fk = models.ForeignKey(
        "Hospitales",
        on_delete=models.CASCADE,
        db_column="cod_hospital_usuario_fk",
        to_field="cod_hospital_pk",
        verbose_name="Hospital",
    )
    cod_eps_usuario_fk = models.ForeignKey(
        "Eps",
        on_delete=models.CASCADE,
        db_column="cod_eps_usuario_fk",
        to_field="cod_eps_pk",
        verbose_name="EPS",
    )

    class Meta:
        db_table = "usuarios"
        verbose_name = "Usuario"
        verbose_name_plural = "Usuarios"
        ordering = ['apellidos_usuario', 'nombres_usuario']

    def __str__(self):
        return f"{self.nombres_usuario} {self.apellidos_usuario}"


class Entrenadores(models.Model):
    id_entrenador_pk = models.AutoField(
        primary_key=True, verbose_name="ID de entrenador"
    )
    id_usuario_entrenador_fk = models.ForeignKey(
        "Usuarios",
        on_delete=models.CASCADE,
        db_column="id_usuario_entrenador_fk",
        verbose_name="Usuario",
    )
    id_especialidad_entrenador_fk = models.ForeignKey(
        "EspecialidadesEntrenador",
        on_delete=models.CASCADE,
        db_column="id_especialidad_entrenador_fk",
        verbose_name="Especialidad de entrenador",
    )
    estado_entrenador = models.BooleanField(verbose_name="Estado de entrenador")

    class Meta:
        db_table = "entrenadores"
        verbose_name = "Entrenador"
        verbose_name_plural = "Entrenadores"
        ordering = [
            "id_usuario_entrenador_fk"
        ]

    def __str__(self):
        return f"Entrenador: {self.id_usuario_entrenador_fk}"


class Administradores(models.Model):
    id_administrador_pk = models.AutoField(
        primary_key=True, verbose_name="ID de administrador"
    )
    id_usuario_administrador_fk = models.ForeignKey(
        "Usuarios",
        on_delete=models.CASCADE,
        db_column="id_usuario_administrador_fk",
        to_field="id_usuario_pk",
        verbose_name="Usuario administrador",
    )
    id_nivel_acceso_administrador_fk = models.ForeignKey(
        "NivelesAdministrador",
        on_delete=models.CASCADE,
        db_column="id_nivel_acceso_administrador_fk",
        verbose_name="Nivel de acceso",
    )
    estado_administrador = models.BooleanField(verbose_name="Estado de administrador")

    class Meta:
        db_table = "administradores"
        verbose_name = "Administrador"
        verbose_name_plural = "Administradores"
        ordering = [
            "id_usuario_administrador_fk"
        ]

    def __str__(self):
        return f"Administrador: {self.id_usuario_administrador_fk}"


class Funcionarios(models.Model):
    id_funcionario_pk = models.AutoField(
        primary_key=True, verbose_name="ID de funcionario"
    )
    id_usuario_funcionario_fk = models.ForeignKey(
        "Usuarios",
        on_delete=models.CASCADE,
        db_column="id_usuario_funcionario_fk",
        verbose_name="Usuario",
    )
    id_dependencia_funcionario_fk = models.ForeignKey(
        "centros.DependenciasFuncionario",
        on_delete=models.CASCADE,
        db_column="id_dependencia_funcionario_fk",
        verbose_name="Dependencia",
    )
    id_estado_funcionario_fk = models.ForeignKey(
        "EstadosFuncionario",
        on_delete=models.CASCADE,
        db_column="id_estado_funcionario_fk",
        verbose_name="Estado de funcionario",
    )

    class Meta:
        db_table = "funcionarios"
        verbose_name = "Funcionario"
        verbose_name_plural = "Funcionarios"
        ordering = [
            "id_usuario_funcionario_fk"
        ]

    def __str__(self):
        return f"Funcionario: {self.id_usuario_funcionario_fk}"


class Aprendices(models.Model):
    id_aprendiz_pk = models.AutoField(primary_key=True, verbose_name="ID de aprendiz")
    id_usuario_aprendiz_fk = models.ForeignKey(
        "Usuarios",
        on_delete=models.CASCADE,
        db_column="id_usuario_aprendiz_fk",
        to_field="id_usuario_pk",
        verbose_name="Usuario aprendiz",
    )
    id_estado_aprendiz_fk = models.ForeignKey(
        "EstadosAprendiz",
        on_delete=models.CASCADE,
        db_column="id_estado_aprendiz_fk",
        verbose_name="Estado de aprendiz",
    )

    class Meta:
        db_table = "aprendices"
        verbose_name = "Aprendiz"
        verbose_name_plural = "Aprendices"
        ordering = [
            "id_usuario_aprendiz_fk"
        ]

    def __str__(self):
        return f"Aprendiz: {self.id_usuario_aprendiz_fk}"


class FichasUsuarios(models.Model):
    id_ficha_usuario_pk = models.AutoField(
        primary_key=True, verbose_name="ID de ficha de usuario"
    )
    id_ficha_fk = models.ForeignKey(
        "programas.FichasFormacion",
        on_delete=models.CASCADE,
        db_column="id_ficha_fk",
        verbose_name="Ficha de formación",
    )
    id_usuario_ficha_fk = models.ForeignKey(
        "Usuarios",
        on_delete=models.CASCADE,
        db_column="id_usuario_ficha_fk",
        verbose_name="Usuario",
    )
    fecha_inscripcion = models.DateField(verbose_name="Fecha de inscripción")

    class Meta:
        db_table = "fichas_usuarios"
        verbose_name = "Ficha de usuario"
        verbose_name_plural = "Fichas de usuarios"
        ordering = ['-fecha_inscripcion']

    def __str__(self):
        return f"Ficha {self.id_ficha_fk} - {self.id_usuario_ficha_fk}"
