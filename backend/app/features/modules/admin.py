"""
Lógica funcional del rol Administrador - AgroFit
"""

from app.shared.components.clear import clear
from app.shared.database.connection import Connect_SQLite


def _db():
    database, cursor = Connect_SQLite()
    return database, cursor


def show_my_profile(user):
    clear()
    print("\n「 MI PERFIL - ADMINISTRADOR 」\n")
    database, cursor = _db()
    try:
        sql = """
            SELECT u.id_usuario_pk, u.numero_documento_usuario, td.nombre_tipo_documento,
                   u.correo_usuario, u.telefono_usuario, u.nombres_usuario,
                   u.apellidos_usuario, s.nombre_sexo, ts.nombre_tipo_sangre,
                   u.fecha_nacimiento_usuario, ec.nombre_estado_civil,
                   d.nombre_departamento, m.nombre_municipio, u.direccion_usuario,
                   r.nombre_rol, h.nombre_hospital, e.nombre_eps,
                   na.nombre_nivel_administrador, a.estado_administrador
            FROM usuarios u
            INNER JOIN tipos_documento td ON u.cod_tipo_documento_usuario_fk = td.cod_tipo_documento_pk
            INNER JOIN sexos s ON u.cod_sexo_usuario_fk = s.cod_sexo_pk
            INNER JOIN tipos_sangre ts ON u.cod_tipo_sangre_usuario_fk = ts.cod_tipo_sangre_pk
            INNER JOIN estados_civil ec ON u.id_estado_civil_usuario_fk = ec.id_estado_civil_pk
            INNER JOIN departamentos d ON u.cod_departamento_usuario_fk = d.cod_departamento_pk
            INNER JOIN municipios m ON u.cod_municipio_usuario_fk = m.cod_municipio_pk
            INNER JOIN roles r ON u.id_rol_usuario_fk = r.id_rol_pk
            INNER JOIN hospitales h ON u.id_hospital_usuario_fk = h.cod_hospital_pk
            INNER JOIN eps e ON u.id_eps_usuario_fk = e.cod_eps_pk
            LEFT JOIN administradores a ON a.id_usuario_administrador_fk = u.id_usuario_pk
            LEFT JOIN niveles_administrador na ON a.id_nivel_acceso_administrador_fk = na.id_nivel_administrador_pk
            WHERE u.id_usuario_pk = ?
        """
        cursor.execute(sql, (user[0],))
        row = cursor.fetchone()
        if not row:
            print("✕ No se encontró información del perfil.")
            return

        labels = [
            "ID Usuario", "Documento", "Tipo Documento", "Correo", "Teléfono",
            "Nombres", "Apellidos", "Sexo", "Tipo Sangre", "Fecha Nacimiento",
            "Estado Civil", "Departamento", "Municipio", "Dirección", "Rol",
            "Hospital", "EPS", "Nivel Administrador", "Estado"
        ]
        for label, value in zip(labels, row):
            if label == "Estado":
                value = "Activo" if value == 1 else ("Inactivo" if value == 0 else value)
            print(f"  {label:<22}: {value}")
    except Exception as error:
        print(f"✕ Error al consultar perfil: {error}")
    finally:
        cursor.close()
        database.close()
        input("\nPresione Enter para continuar...")


def manage_users(user):
    clear()
    while True:
        print("""
「 GESTIÓN DE USUARIOS 」

  1. Listar usuarios
  2. Buscar usuario por documento
  3. Activar / Desactivar usuario
  4. Volver
        """)
        opt = input("Opción: ").strip()
        if opt == "1":
            _list_users()
        elif opt == "2":
            _search_user_by_document()
        elif opt == "3":
            _toggle_user_status()
        elif opt == "4":
            break
        else:
            print("✕ Opción no válida.")
            input("\nPresione Enter para continuar...")


def _list_users():
    database, cursor = _db()
    try:
        sql = """
            SELECT u.id_usuario_pk, u.numero_documento_usuario,
                   u.nombres_usuario, u.apellidos_usuario,
                   u.correo_usuario, r.nombre_rol, u.estado_usuario
            FROM usuarios u
            INNER JOIN roles r ON u.id_rol_usuario_fk = r.id_rol_pk
            ORDER BY u.id_usuario_pk
            LIMIT 50
        """
        cursor.execute(sql)
        rows = cursor.fetchall()
        print("\n{:<6} {:<12} {:<25} {:<30} {:<15} {}".format("ID", "Documento", "Nombre", "Correo", "Rol", "Estado"))
        print("-" * 100)
        for r in rows:
            estado = "Activo" if r[6] == 1 else "Inactivo"
            nombre = f"{r[2]} {r[3]}"
            print(f"{r[0]:<6} {r[1]:<12} {nombre:<25} {r[4]:<30} {r[5]:<15} {estado}")
    except Exception as error:
        print(f"✕ Error: {error}")
    finally:
        cursor.close()
        database.close()
        input("\nPresione Enter para continuar...")


def _search_user_by_document():
    doc = input("\nNúmero de documento: ").strip()
    if not doc:
        print("✕ Documento vacío.")
        input("\nPresione Enter para continuar...")
        return

    database, cursor = _db()
    try:
        sql = """
            SELECT u.id_usuario_pk, u.numero_documento_usuario,
                   u.nombres_usuario, u.apellidos_usuario,
                   u.correo_usuario, r.nombre_rol, u.estado_usuario
            FROM usuarios u
            INNER JOIN roles r ON u.id_rol_usuario_fk = r.id_rol_pk
            WHERE u.numero_documento_usuario = ?
        """
        cursor.execute(sql, (doc,))
        row = cursor.fetchone()
        if row:
            estado = "Activo" if row[6] == 1 else "Inactivo"
            print(f"\n✓ ID: {row[0]} | {row[2]} {row[3]} | {row[4]} | {row[5]} | {estado}")
        else:
            print("✕ Usuario no encontrado.")
    except Exception as error:
        print(f"✕ Error: {error}")
    finally:
        cursor.close()
        database.close()
        input("\nPresione Enter para continuar...")


def _toggle_user_status():
    doc = input("\nDocumento del usuario a cambiar estado: ").strip()
    if not doc:
        print("✕ Documento vacío.")
        input("\nPresione Enter para continuar...")
        return

    database, cursor = _db()
    try:
        cursor.execute("SELECT id_usuario_pk, estado_usuario FROM usuarios WHERE numero_documento_usuario = ?", (doc,))
        row = cursor.fetchone()
        if not row:
            print("✕ Usuario no encontrado.")
        else:
            new_status = 0 if row[1] == 1 else 1
            cursor.execute("UPDATE usuarios SET estado_usuario = ? WHERE id_usuario_pk = ?", (new_status, row[0]))
            database.commit()
            print(f"✓ Estado actualizado a: {'Activo' if new_status == 1 else 'Inactivo'}")
    except Exception as error:
        print(f"✕ Error: {error}")
        database.rollback()
    finally:
        cursor.close()
        database.close()
        input("\nPresione Enter para continuar...")


def generate_reports(user):
    clear()
    while True:
        print("""
「 REPORTES 」

  1. Resumen de usuarios por rol
  2. Programas de formación
  3. Volver
        """)
        opt = input("Opción: ").strip()
        if opt == "1":
            _report_users_by_role()
        elif opt == "2":
            _report_programs()
        elif opt == "3":
            break
        else:
            print("✕ Opción no válida.")
            input("\nPresione Enter para continuar...")


def _report_users_by_role():
    database, cursor = _db()
    try:
        sql = "SELECT r.nombre_rol, COUNT(*) as total FROM usuarios u INNER JOIN roles r ON u.id_rol_usuario_fk = r.id_rol_pk GROUP BY r.nombre_rol ORDER BY total DESC"
        cursor.execute(sql)
        rows = cursor.fetchall()
        print("\n「 Usuarios por rol 」")
        for r in rows:
            print(f"  {r[0]:<20}: {r[1]}")
    except Exception as error:
        print(f"✕ Error: {error}")
    finally:
        cursor.close()
        database.close()
        input("\nPresione Enter para continuar...")


def _report_programs():
    database, cursor = _db()
    try:
        sql = """
            SELECT pf.cod_programa_pk, pf.nombre_programa, nf.nombre_nivel_formacion_programa, pf.duracion_programa
            FROM programas_formacion pf
            INNER JOIN niveles_formacion_programa nf ON pf.id_nivel_formacion_programa_fk = nf.id_niveles_formacion_programa_pk
            WHERE pf.estado_programa = 1
            ORDER BY pf.nombre_programa
            LIMIT 30
        """
        cursor.execute(sql)
        rows = cursor.fetchall()
        print("\n{:<10} {:<50} {:<12} {}".format("Código", "Programa", "Nivel", "Duración"))
        print("-" * 90)
        for r in rows:
            print(f"{r[0]:<10} {r[1][:48]:<50} {r[2]:<12} {r[3]} meses")
    except Exception as error:
        print(f"✕ Error: {error}")
    finally:
        cursor.close()
        database.close()
        input("\nPresione Enter para continuar...")