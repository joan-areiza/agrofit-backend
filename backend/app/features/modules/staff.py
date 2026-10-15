"""
Lógica funcional del rol Funcionario - AgroFit
"""

from app.shared.components.clear import clear
from app.shared.database.connection import Connect_SQLite


def _db():
    database, cursor = Connect_SQLite()
    return database, cursor


def show_my_profile(user):
    clear()
    print("\n「 MI PERFIL - FUNCIONARIO 」\n")
    database, cursor = _db()
    try:
        sql = """
            SELECT
                u.id_usuario_pk, u.numero_documento_usuario, td.nombre_tipo_documento,
                u.correo_usuario, u.telefono_usuario, u.nombres_usuario,
                u.apellidos_usuario, s.nombre_sexo, u.fecha_nacimiento_usuario,
                df.nombre_dependencia_funcionario, ef.nombre_estado_funcionario
            FROM usuarios u
            INNER JOIN tipos_documento td ON u.cod_tipo_documento_usuario_fk = td.cod_tipo_documento_pk
            INNER JOIN sexos s ON u.cod_sexo_usuario_fk = s.cod_sexo_pk
            INNER JOIN funcionarios f ON f.id_usuario_funcionario_fk = u.id_usuario_pk
            INNER JOIN dependencias_funcionario df ON f.id_dependencia_funcionario_fk = df.id_dependencia_funcionario_pk
            INNER JOIN estados_funcionario ef ON f.id_estado_funcionario_fk = ef.id_estado_funcionario_pk
            WHERE u.id_usuario_pk = ?
        """
        cursor.execute(sql, (user[0],))
        row = cursor.fetchone()
        if not row:
            print("✕ No se encontró información del perfil.")
            return

        labels = [
            "ID Usuario", "Documento", "Tipo Documento", "Correo", "Teléfono",
            "Nombres", "Apellidos", "Sexo", "Fecha Nacimiento", "Dependencia", "Estado"
        ]
        for label, value in zip(labels, row):
            print(f"  {label:<20}: {value}")
    except Exception as error:
        print(f"✕ Error al consultar perfil: {error}")
    finally:
        cursor.close()
        database.close()


def consult_learners(user):
    clear()
    while True:
        print("""
「 CONSULTAR APRENDICES 」

  1. Listar aprendices
  2. Buscar por documento
  3. Ver fichas de un aprendiz
  4. Volver
        """)
        opt = input("Opción: ").strip()
        if opt == "1":
            _list_learners()
        elif opt == "2":
            _search_learner()
        elif opt == "3":
            _learner_fichas()
        elif opt == "4":
            break
        else:
            print("✕ Opción no válida.")


def _list_learners():
    database, cursor = _db()
    try:
        sql = """
            SELECT a.id_aprendiz_pk, u.numero_documento_usuario,
                   u.nombres_usuario, u.apellidos_usuario,
                   u.correo_usuario, u.telefono_usuario
            FROM aprendices a
            INNER JOIN usuarios u ON a.id_usuario_aprendiz_fk = u.id_usuario_pk
            WHERE u.estado_usuario = 1
            ORDER BY u.apellidos_usuario, u.nombres_usuario
            LIMIT 50
        """
        cursor.execute(sql)
        rows = cursor.fetchall()
        print("\n{:<8} {:<12} {:<28} {:<30} {}".format("ID Apr", "Documento", "Nombre", "Correo", "Teléfono"))
        print("-" * 95)
        for r in rows:
            nombre = f"{r[2]} {r[3]}"
            print(f"{r[0]:<8} {r[1]:<12} {nombre[:26]:<28} {r[4][:28]:<30} {r[5] or '-'}")
    except Exception as error:
        print(f"✕ Error: {error}")
    finally:
        cursor.close()
        database.close()


def _search_learner():
    doc = input("\nDocumento del aprendiz: ").strip()
    if not doc:
        print("✕ Documento vacío.")
        return

    database, cursor = _db()
    try:
        sql = """
            SELECT a.id_aprendiz_pk, u.numero_documento_usuario,
                   u.nombres_usuario, u.apellidos_usuario,
                   u.correo_usuario, u.telefono_usuario,
                   m.nombre_municipio, d.nombre_departamento
            FROM aprendices a
            INNER JOIN usuarios u ON a.id_usuario_aprendiz_fk = u.id_usuario_pk
            INNER JOIN municipios m ON u.cod_municipio_usuario_fk = m.cod_municipio_pk
            INNER JOIN departamentos d ON u.cod_departamento_usuario_fk = d.cod_departamento_pk
            WHERE u.numero_documento_usuario = ?
        """
        cursor.execute(sql, (doc,))
        row = cursor.fetchone()
        if row:
            print(f"\n✓ ID Aprendiz: {row[0]}\n  Documento: {row[1]}\n  Nombre: {row[2]} {row[3]}\n  Correo: {row[4]}\n  Teléfono: {row[5] or '-'}\n  Ubicación: {row[6]}, {row[7]}")
        else:
            print("✕ Aprendiz no encontrado.")
    except Exception as error:
        print(f"✕ Error: {error}")
    finally:
        cursor.close()
        database.close()


def _learner_fichas():
    doc = input("\nDocumento del aprendiz: ").strip()
    database, cursor = _db()
    try:
        sql = """
            SELECT fu.id_ficha_usuario_pk, ff.numero_ficha, pf.nombre_programa,
                   fu.fecha_inscripcion, j.nombre_jornada, mod.nombre_modalidad
            FROM fichas_usuarios fu
            INNER JOIN usuarios u ON fu.id_usuario_ficha_fk = u.id_usuario_pk
            INNER JOIN fichas_formacion ff ON fu.id_ficha_fk = ff.id_ficha_formacion_pk
            INNER JOIN programas_formacion pf ON ff.id_programa_ficha_fk = pf.id_programa_pk
            INNER JOIN jornadas j ON ff.id_jornada_ficha_fk = j.id_jornada_pk
            INNER JOIN modalidades mod ON ff.id_modalidad_ficha_fk = mod.id_modalidad_pk
            WHERE u.numero_documento_usuario = ? AND u.id_rol_usuario_fk = 1
        """
        cursor.execute(sql, (doc,))
        rows = cursor.fetchall()
        if not rows:
            print("✕ No se encontraron fichas para este aprendiz.")
        else:
            print("\n{:<6} {:<10} {:<40} {:<12} {:<10} {}".format("ID", "Ficha", "Programa", "Inscripción", "Jornada", "Modalidad"))
            print("-" * 95)
            for r in rows:
                print(f"{r[0]:<6} {r[1]:<10} {r[2][:38]:<40} {str(r[3]):<12} {r[4]:<10} {r[5]}")
    except Exception as error:
        print(f"✕ Error: {error}")
    finally:
        cursor.close()
        database.close()


def view_physical_evaluations(user):
    clear()
    while True:
        print("""
「 EVALUACIONES FÍSICAS 」

  1. Listar evaluaciones recientes
  2. Buscar por documento de usuario
  3. Ver detalle de una evaluación
  4. Volver
        """)
        opt = input("Opción: ").strip()
        if opt == "1":
            _list_evaluations()
        elif opt == "2":
            _search_evaluations_by_doc()
        elif opt == "3":
            _evaluation_detail()
        elif opt == "4":
            break
        else:
            print("✕ Opción no válida.")


def _list_evaluations():
    database, cursor = _db()
    try:
        sql = """
            SELECT ef.id_evaluacion_fisica_pk, u.nombres_usuario, u.apellidos_usuario,
                   ef.fecha_evaluacion, ef.peso_evaluacion, ef.altura_evaluacion
            FROM evaluaciones_fisicas ef
            INNER JOIN usuarios u ON ef.id_usuario_evaluacion_fk = u.id_usuario_pk
            ORDER BY ef.fecha_evaluacion DESC
            LIMIT 30
        """
        cursor.execute(sql)
        rows = cursor.fetchall()
        if not rows:
            print("\n  No hay evaluaciones registradas.")
        else:
            print("\n{:<6} {:<28} {:<12} {:<8} {}".format("ID", "Usuario", "Fecha", "Peso", "Altura"))
            print("-" * 70)
            for r in rows:
                nombre = f"{r[1]} {r[2]}"
                print(f"{r[0]:<6} {nombre[:26]:<28} {str(r[3]):<12} {r[4]:<8} {r[5]}")
    except Exception as error:
        print(f"✕ Error: {error}")
    finally:
        cursor.close()
        database.close()


def _search_evaluations_by_doc():
    doc = input("\nDocumento del usuario: ").strip()
    database, cursor = _db()
    try:
        sql = """
            SELECT ef.id_evaluacion_fisica_pk, ef.fecha_evaluacion,
                   ef.peso_evaluacion, ef.altura_evaluacion, na.nombre_nivel_actividad_fisica
            FROM evaluaciones_fisicas ef
            INNER JOIN usuarios u ON ef.id_usuario_evaluacion_fk = u.id_usuario_pk
            INNER JOIN niveles_actividad_fisica na ON ef.id_nivel_actividad_fisica_evaluacion_fk = na.id_nivel_actividad_fisica_pk
            WHERE u.numero_documento_usuario = ?
            ORDER BY ef.fecha_evaluacion DESC
        """
        cursor.execute(sql, (doc,))
        rows = cursor.fetchall()
        if not rows:
            print("✕ No se encontraron evaluaciones.")
        else:
            print("\n{:<6} {:<12} {:<8} {:<8} {}".format("ID", "Fecha", "Peso", "Altura", "Nivel Act."))
            print("-" * 55)
            for r in rows:
                print(f"{r[0]:<6} {str(r[1]):<12} {r[2]:<8} {r[3]:<8} {r[4]}")
    except Exception as error:
        print(f"✕ Error: {error}")
    finally:
        cursor.close()
        database.close()


def _evaluation_detail():
    try:
        eval_id = int(input("\nID de la evaluación: ").strip())
    except ValueError:
        print("✕ ID inválido.")
        return

    database, cursor = _db()
    try:
        sql = """
            SELECT u.nombres_usuario, u.apellidos_usuario, u.numero_documento_usuario,
                   ef.fecha_evaluacion, ef.peso_evaluacion, ef.altura_evaluacion,
                   ef.grasa_corporal_evaluacion, ef.grasa_muscular_evaluacion,
                   ef.presion_arterial, na.nombre_nivel_actividad_fisica,
                   am.nombre_antecedente_medico, cf.nombre_complexion_fisica,
                   ef.observacion_evaluacion
            FROM evaluaciones_fisicas ef
            INNER JOIN usuarios u ON ef.id_usuario_evaluacion_fk = u.id_usuario_pk
            INNER JOIN niveles_actividad_fisica na ON ef.id_nivel_actividad_fisica_evaluacion_fk = na.id_nivel_actividad_fisica_pk
            INNER JOIN antecedentes_medicos am ON ef.id_antecedente_medico_evaluacion_fk = am.id_antecedente_medico_pk
            INNER JOIN complexiones_fisicas cf ON ef.id_complexion_fisica_evaluacion_fk = cf.id_complexion_fisica_pk
            WHERE ef.id_evaluacion_fisica_pk = ?
        """
        cursor.execute(sql, (eval_id,))
        row = cursor.fetchone()
        if not row:
            print("✕ Evaluación no encontrada.")
        else:
            print(f"\nUsuario: {row[0]} {row[1]} (Doc: {row[2]})\nFecha: {row[3]}\nPeso: {row[4]} kg | Altura: {row[5]} m\nGrasa corporal: {row[6]} | Grasa muscular: {row[7]}\nPresión arterial: {row[8]}\nNivel actividad: {row[9]}\nAntecedente: {row[10]} | Complexión: {row[11]}\nObservaciones: {row[12] or '(ninguna)'}")
    except Exception as error:
        print(f"✕ Error: {error}")
    finally:
        cursor.close()
        database.close()


def generate_reports(user):
    clear()
    while True:
        print("""
「 REPORTES 」

  1. Aprendices activos por ficha
  2. Total de aprendices activos
  3. Programas de formación activos
  4. Evaluaciones físicas por mes
  5. Volver
        """)
        opt = input("Opción: ").strip()
        if opt == "1":
            _report_learners_by_status()
        elif opt == "2":
            _report_active_learners()
        elif opt == "3":
            _report_programs()
        elif opt == "4":
            _report_evaluations_by_month()
        elif opt == "5":
            break
        else:
            print("✕ Opción no válida.")


def _report_learners_by_status():
    database, cursor = _db()
    try:
        sql = """
            SELECT ff.numero_ficha, COUNT(*) as total
            FROM fichas_usuarios fu
            INNER JOIN fichas_formacion ff ON fu.id_ficha_fk = ff.id_ficha_formacion_pk
            INNER JOIN usuarios u ON fu.id_usuario_ficha_fk = u.id_usuario_pk
            WHERE u.id_rol_usuario_fk = 1 AND u.estado_usuario = 1
            GROUP BY ff.numero_ficha
            ORDER BY total DESC
        """
        cursor.execute(sql)
        rows = cursor.fetchall()
        print("\n「 Aprendices activos por ficha 」")
        if not rows:
            print("  (Sin datos de fichas)")
        for r in rows:
            print(f"  Ficha {r[0]:<20}: {r[1]} aprendices")
    except Exception as error:
        print(f"✕ Error: {error}")
    finally:
        cursor.close()
        database.close()


def _report_active_learners():
    database, cursor = _db()
    try:
        cursor.execute("SELECT COUNT(*) FROM aprendices a INNER JOIN usuarios u ON a.id_usuario_aprendiz_fk = u.id_usuario_pk WHERE u.estado_usuario = 1")
        total = cursor.fetchone()[0]
        print(f"\n「 Aprendices activos 」: {total}")
    except Exception as error:
        print(f"✕ Error: {error}")
    finally:
        cursor.close()
        database.close()


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


def _report_evaluations_by_month():
    database, cursor = _db()
    try:
        sql = "SELECT strftime('%Y-%m', fecha_evaluacion) as mes, COUNT(*) as total FROM evaluaciones_fisicas GROUP BY mes ORDER BY mes DESC LIMIT 12"
        cursor.execute(sql)
        rows = cursor.fetchall()
        print("\n「 Evaluaciones físicas por mes 」")
        if not rows:
            print("  (Sin datos)")
        for r in rows:
            print(f"  {r[0]}: {r[1]}")
    except Exception as error:
        print(f"✕ Error: {error}")
    finally:
        cursor.close()
        database.close()