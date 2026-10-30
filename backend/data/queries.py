from core.utils.format_text import format_text
from core.database.connection import Connect_SQLite  # Importa la función de conexión

database, cursor = Connect_SQLite()

# Seleccionar la base de datos
#cursor.execute("USE agrofit;")

def find_by_document_number(document_number):
    sql = """
        SELECT *
        FROM usuarios
        WHERE numero_documento_usuario = ?
    """
    cursor.execute(sql, (document_number,))
    return cursor.fetchone()

def find_by_email(email):
    sql = """
        SELECT *
        FROM usuarios
        WHERE correo_usuario = ?
    """

    cursor.execute(sql, (email,))
    return cursor.fetchone()


def fetch_name(query, value):
    """
    Busca un registro por nombre en la base de datos.

    Retorna:
    - El resultado encontrado.
    - None si no existe.
    """

    formatted_value = format_text(value)

    if not formatted_value:
        return None

    try:
        cursor.execute(query, (formatted_value,))
        result = cursor.fetchone()

        if result:
            return result

        return None

    except Exception as error:
        print(f"Error al realizar la consulta: {error}")
        return None


def divipole(city_name: str):
    query = """
        SELECT
            m.cod_municipio_pk,
            m.nombre_municipio,
            d.cod_departamento_pk,
            d.nombre_departamento
        FROM municipios m
        INNER JOIN departamentos d
            ON m.cod_departamento_municipio_fk = d.cod_departamento_pk
        WHERE LOWER(
            REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(
                m.nombre_municipio,
                'á', 'a'),
                'é', 'e'),
                'í', 'i'),
                'ó', 'o'),
                'ú', 'u')
        ) = ?
        LIMIT 1
    """

    return fetch_name(query, city_name)


def disability(name):
    query = """
        SELECT nombre_antecedente_medico
        FROM antecedentes_medicos
        WHERE LOWER(
            REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(
                nombre_antecedente_medico,
                'á', 'a'),
                'é', 'e'),
                'í', 'i'),
                'ó', 'o'),
                'ú', 'u')
        ) = ?
        LIMIT 1
    """

    result = fetch_name(query, name)

    return result[0] if result else None


def fetch_catalog(query):
    try:
        cursor.execute(query)
        results = cursor.fetchall()

        return {item_id: item_name.upper().title() for item_id, item_name in results}

    except Exception as error:
        print(f"Error al consultar las opciones: {error}")
        return {}

def cohort():
    sql = """
        SELECT id_ficha_formacion_pk, numero_ficha 
        FROM fichas_formacion 
        WHERE estado_ficha = 1
    """
    cursor.execute(sql)
    return {row[0]: row[1] for row in cursor.fetchall()}

def roles():
    query = """
        SELECT id_rol_pk, nombre_rol
        FROM roles
        ORDER BY id_rol_pk
    """
    return fetch_catalog(query)


def specialty():
    query = """
        SELECT id_especialidad_entrenador_pk, nombre_especialidad_entrenador
        FROM especialidades_entrenador
        ORDER BY id_especialidad_entrenador_pk
    """
    return fetch_catalog(query)


def dependency():
    query = """
        SELECT id_dependencia_funcionario_pk, nombre_dependencia_funcionario
        FROM dependencias_funcionario
        ORDER BY id_dependencia_funcionario_pk
    """
    return fetch_catalog(query)


def admin_level():
    query = """
        SELECT id_nivel_administrador_pk, nombre_nivel_administrador
        FROM niveles_administrador
        ORDER BY id_nivel_administrador_pk
    """
    return fetch_catalog(query)


def document_type():
    query = """
        SELECT cod_tipo_documento_pk, nombre_tipo_documento
        FROM tipos_documento
        ORDER BY cod_tipo_documento_pk
    """
    return fetch_catalog(query)


def gender():
    query = """
        SELECT cod_sexo_pk, nombre_sexo
        FROM sexos
        ORDER BY nombre_sexo
    """
    return fetch_catalog(query)


def marital_status():
    query = """
        SELECT id_estado_civil_pk, nombre_estado_civil
        FROM estados_civil
        ORDER BY id_estado_civil_pk
    """
    return fetch_catalog(query)


def blood_type():
    query = """
        SELECT cod_tipo_sangre_pk, nombre_tipo_sangre
        FROM tipos_sangre
        ORDER BY cod_tipo_sangre_pk
    """
    return fetch_catalog(query)


def eps():
    query = """
        SELECT cod_eps_pk, nombre_eps
        FROM eps
        ORDER BY cod_eps_pk
    """
    return fetch_catalog(query)


def hospital():
    query = """
        SELECT cod_hospital_pk, nombre_hospital
        FROM hospitales
        ORDER BY cod_hospital_pk
    """
    return fetch_catalog(query)


def training_center():
    query = """
        SELECT cod_centro_pk, nombre_centro
        FROM centros_formacion
        ORDER BY cod_centro_pk
    """
    return fetch_catalog(query)
