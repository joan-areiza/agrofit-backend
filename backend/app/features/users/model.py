import datetime
import hashlib
from app.shared.database import connection

connect = connection.Connect_SQLite()
database = connect[0]
cursor = connect[1]

#cursor.execute("USE agrofit;")


class User:

    def __init__(
        self,
        role=None,
        document_type=None,
        document_number=None,
        birth_date=None,
        names=None,
        surnames=None,
        gender=None,
        marital_status=None,
        blood_type=None,
        sena_email=None,
        password=None,
        phone=None,
        secondary_phone=None,
        municipality=None,
        department=None,
        address=None,
        eps=None,
        hospital=None,
        dependency=None,
        specialty=None,
        admin_level=None,
        cohort=None,
        leader_cohort=None,
    ):
        self.role = role
        self.document_type = document_type
        self.document_number = document_number
        self.birth_date = birth_date
        self.names = names
        self.surnames = surnames
        self.gender = gender
        self.marital_status = marital_status
        self.blood_type = blood_type
        self.sena_email = sena_email
        self.password = password
        self.phone = phone
        self.secondary_phone = secondary_phone
        self.municipality = municipality
        self.department = department
        self.address = address
        self.eps = eps
        self.hospital = hospital
        self.dependency = dependency
        self.specialty = specialty
        self.admin_level = admin_level
        self.cohort = cohort if cohort is not None else []
        self.leader_cohort = leader_cohort if leader_cohort is not None else []
        
    def register(self):

        created_date = datetime.datetime.now()

        # Cifrar contraseña
        hashed_password = hashlib.sha256()
        hashed_password.update(self.password.encode("utf8"))

        user_status = 1

        sql = """
        INSERT INTO usuarios (
            numero_documento_usuario,
            cod_tipo_documento_usuario_fk,
            correo_usuario,
            telefono_usuario,
            telefono_emergencia_usuario,
            clave_usuario,
            nombres_usuario,
            apellidos_usuario,
            cod_sexo_usuario_fk,
            cod_tipo_sangre_usuario_fk,
            fecha_nacimiento_usuario,
            id_estado_civil_usuario_fk,
            cod_departamento_usuario_fk,
            cod_municipio_usuario_fk,
            direccion_usuario,
            foto_usuario,
            fecha_registro_usuario,
            estado_usuario,
            id_rol_usuario_fk,
            id_hospital_usuario_fk,
            id_eps_usuario_fk
        )
        VALUES (
            ?, ?, ?, ?, ?, ?, ?, ?, ?, ?,
            ?, ?, ?, ?, ?, NULL, ?, ?, ?, ?, ?
        )
    """

        user = (
            self.document_number,
            self.document_type,
            self.sena_email,
            self.phone,
            self.secondary_phone,
            hashed_password.hexdigest(),
            self.names,
            self.surnames,
            self.gender,
            self.blood_type,
            self.birth_date,
            self.marital_status,
            self.department,
            self.municipality,
            self.address,
            created_date,
            user_status,
            self.role,
            self.hospital,
            self.eps,
        )

        try:
            # 1. Registrar usuario
            cursor.execute(sql, user)

            # 2. Obtener el ID generado en usuarios
            user_id = cursor.lastrowid

            # 3. Registrar información específica del rol
            if self.role == 1:
                cursor.execute(
                    """
                    INSERT INTO aprendices (
                        id_usuario_aprendiz_fk
                    )
                    VALUES (?)
                """,
                    (user_id,),
                )

                # Registrar fichas asociadas en fichas_usuarios
                if self.cohort:
                    for item in self.cohort:
                        cursor.execute(
                            """
                            INSERT INTO fichas_usuarios (
                                id_ficha_fk,
                                id_usuario_ficha_fk,
                                fecha_inscripcion
                            )
                            VALUES (?, ?, ?)
                        """,
                            (item["id_cohort"], user_id, item["enrollment_date"]),
                        )

            elif self.role == 2:
                cursor.execute(
                    """
                    INSERT INTO entrenadores (
                        id_usuario_entrenador_fk,
                        id_especialidad_entrenador_fk,
                        estado_entrenador
                    )
                    VALUES (?, ?, ?)
                """,
                    (user_id, self.specialty, 1),
                )

                # Registrar fichas asociadas en fichas_usuarios
                if self.cohort:
                    for item in self.cohort:
                        cursor.execute(
                            """
                            INSERT INTO fichas_usuarios (
                                id_ficha_fk,
                                id_usuario_ficha_fk,
                                fecha_inscripcion
                            )
                            VALUES (?, ?, ?)
                        """,
                            (item["id_cohort"], user_id, item["enrollment_date"]),
                        )

            elif self.role == 3:
                cursor.execute(
                    """
                    INSERT INTO funcionarios (
                        id_usuario_funcionario_fk,
                        id_dependencia_funcionario_fk,
                        id_estado_funcionario_fk
                    )
                    VALUES (?, ?, ?)
                """,
                    (user_id, self.dependency, 1),
                )

                # 1. Si es líder, actualizar las fichas que lidera en fichas_formacion
                if self.leader_cohort:
                    for item in self.leader_cohort:
                        cursor.execute(
                            """
                            UPDATE fichas_formacion
                            SET id_instructor_lider_ficha_fk = ?
                            WHERE id_ficha_formacion_pk = ?
                        """,
                            (user_id, item["id_cohort"]),
                        )

                # 2. Registrar las fichas a las que pertenece en fichas_usuarios
                if self.cohort:
                    for item in self.cohort:
                        cursor.execute(
                            """
                            INSERT INTO fichas_usuarios (
                                id_ficha_fk,
                                id_usuario_ficha_fk,
                                fecha_inscripcion
                            )
                            VALUES (?, ?, ?)
                        """,
                            (item["id_cohort"], user_id, item["enrollment_date"]),
                        )

            elif self.role == 4:
                cursor.execute(
                    """
                    INSERT INTO administradores (
                        id_usuario_administrador_fk,
                        id_nivel_acceso_administrador_fk,
                        estado_administrador
                    )
                    VALUES (?, ?, ?)
                """,
                    (user_id, self.admin_level, 1),
                )

            database.commit()
            result = [cursor.rowcount, self, user_id]

            """
            except:

                result = [0, self]

            return result
            """

        except Exception as error:
            database.rollback()
            print(f"\n✕ Error al registrar el usuario: {error}")
            result = [0, self, None]

        return result

    def authenticate(self):
        # Consulta para comprobar si existe el usuario
        sql = """
            SELECT
                id_usuario_pk,
                numero_documento_usuario,
                nombres_usuario,
                apellidos_usuario,
                correo_usuario,
                id_rol_usuario_fk
            FROM usuarios
            WHERE correo_usuario = ?
            AND clave_usuario = ?
            AND estado_usuario = 1
        """

        # Cifrar contraseña
        hashed_password = hashlib.sha256()
        hashed_password.update(self.password.encode("utf8"))

        # Datos para la consulta
        user = (self.sena_email, hashed_password.hexdigest())

        cursor.execute(sql, user)
        result = cursor.fetchone()

        return result

    def recover_password(self, new_password):

        hashed_password = hashlib.sha256()
        hashed_password.update(new_password.encode("utf8"))

        sql = """
            UPDATE usuarios
            SET clave_usuario = ?
            WHERE correo_usuario = ?
        """

        try:
            cursor.execute(sql, (hashed_password.hexdigest(), self.sena_email))

            database.commit()

            return [cursor.rowcount, self]

        except Exception as error:
            database.rollback()
            print(f"\n✕ Error al actualizar la contraseña: {error}")
            return [0, self]
