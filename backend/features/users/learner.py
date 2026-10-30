"""
Lógica funcional del rol Aprendiz - AgroFit
"""

from core.components.clear import clear
from core.database.connection import Connect_SQLite


def _db():
    database, cursor = Connect_SQLite()
    return database, cursor


def _get_aprendiz_id(user_id):
    database, cursor = _db()
    try:
        cursor.execute("SELECT id_aprendiz_pk FROM aprendices WHERE id_usuario_aprendiz_fk = ?", (user_id,))
        row = cursor.fetchone()
        return row[0] if row else None
    except Exception:
        return None
    finally:
        cursor.close()
        database.close()


def show_my_profile(user):
    clear()
    print("\n「 MI PERFIL - APRENDIZ 」\n")
    database, cursor = _db()
    try:
        sql = """
            SELECT u.id_usuario_pk, u.numero_documento_usuario, td.nombre_tipo_documento,
                   u.correo_usuario, u.telefono_usuario, u.nombres_usuario,
                   u.apellidos_usuario, s.nombre_sexo, ts.nombre_tipo_sangre,
                   u.fecha_nacimiento_usuario, ec.nombre_estado_civil,
                   d.nombre_departamento, m.nombre_municipio, u.direccion_usuario,
                   h.nombre_hospital, e.nombre_eps
            FROM usuarios u
            INNER JOIN tipos_documento td ON u.cod_tipo_documento_usuario_fk = td.cod_tipo_documento_pk
            INNER JOIN sexos s ON u.cod_sexo_usuario_fk = s.cod_sexo_pk
            INNER JOIN tipos_sangre ts ON u.cod_tipo_sangre_usuario_fk = ts.cod_tipo_sangre_pk
            INNER JOIN estados_civil ec ON u.id_estado_civil_usuario_fk = ec.id_estado_civil_pk
            INNER JOIN departamentos d ON u.cod_departamento_usuario_fk = d.cod_departamento_pk
            INNER JOIN municipios m ON u.cod_municipio_usuario_fk = m.cod_municipio_pk
            INNER JOIN hospitales h ON u.id_hospital_usuario_fk = h.cod_hospital_pk
            INNER JOIN eps e ON u.id_eps_usuario_fk = e.cod_eps_pk
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
            "Estado Civil", "Departamento", "Municipio", "Dirección", "Hospital", "EPS"
        ]
        for label, value in zip(labels, row):
            print(f"  {label:<20}: {value}")

        cursor.execute("""
            SELECT ff.numero_ficha, pf.nombre_programa, fu.fecha_inscripcion
            FROM fichas_usuarios fu
            INNER JOIN fichas_formacion ff ON fu.id_ficha_fk = ff.id_ficha_formacion_pk
            INNER JOIN programas_formacion pf ON ff.id_programa_ficha_fk = pf.id_programa_pk
            WHERE fu.id_usuario_ficha_fk = ?
        """, (user[0],))
        fichas = cursor.fetchall()
        if fichas:
            print("\n  「 Fichas de formación 」")
            for f in fichas:
                print(f"    Ficha {f[0]} | {f[1][:40]} | Inscrito: {f[2]}")
    except Exception as error:
        print(f"✕ Error al consultar perfil: {error}")
    finally:
        cursor.close()
        database.close()


def my_physical_evaluations(user):
    clear()
    print("\n「 MIS EVALUACIONES FÍSICAS 」\n")
    database, cursor = _db()
    try:
        sql = """
            SELECT ef.id_evaluacion_fisica_pk, ef.fecha_evaluacion, ef.peso_evaluacion,
                   ef.altura_evaluacion, ef.grasa_corporal_evaluacion, ef.grasa_muscular_evaluacion,
                   ef.presion_arterial, na.nombre_nivel_actividad_fisica, am.nombre_antecedente_medico,
                   cf.nombre_complexion_fisica, ef.observacion_evaluacion,
                   (ue.nombres_usuario || ' ' || ue.apellidos_usuario) AS entrenador
            FROM evaluaciones_fisicas ef
            INNER JOIN niveles_actividad_fisica na ON ef.id_nivel_actividad_fisica_evaluacion_fk = na.id_nivel_actividad_fisica_pk
            INNER JOIN antecedentes_medicos am ON ef.id_antecedente_medico_evaluacion_fk = am.id_antecedente_medico_pk
            INNER JOIN complexiones_fisicas cf ON ef.id_complexion_fisica_evaluacion_fk = cf.id_complexion_fisica_pk
            INNER JOIN entrenadores en ON ef.id_entrenador_encargado_evaluacion_fk = en.id_entrenador_pk
            INNER JOIN usuarios ue ON en.id_usuario_entrenador_fk = ue.id_usuario_pk
            WHERE ef.id_usuario_evaluacion_fk = ?
            ORDER BY ef.fecha_evaluacion DESC
        """
        cursor.execute(sql, (user[0],))
        rows = cursor.fetchall()
        if not rows:
            print("  No tienes evaluaciones físicas registradas.")
        else:
            for r in rows:
                print("-" * 60)
                print(f"  ID: {r[0]} | Fecha: {r[1]}\n  Peso: {r[2]} kg | Altura: {r[3]} m\n  Grasa corporal: {r[4]} | Grasa muscular: {r[5]}\n  Presión arterial: {r[6]}\n  Nivel actividad: {r[7]}\n  Antecedente: {r[8]} | Complexión: {r[9]}\n  Entrenador: {r[11]}\n  Observaciones: {r[10] or '(ninguna)'}")
            print("-" * 60)
    except Exception as error:
        print(f"✕ Error: {error}")
    finally:
        cursor.close()
        database.close()


def my_routines(user):
    clear()
    print("\n「 MIS RUTINAS DE ENTRENAMIENTO 」\n")
    aprendiz_id = _get_aprendiz_id(user[0])
    if not aprendiz_id:
        print("✕ No se encontró registro de aprendiz para este usuario.")
        return

    database, cursor = _db()
    try:
        sql = """
            SELECT ar.id_asignacion_rutina_usuario_pk, r.nombre_rutina, o.nombre_objetivo_rutina,
                   n.nombre_nivel_rutina, ar.fecha_hora_inicio_asignacion_rutina,
                   ar.fecha_hora_fin_asignacion_rutina, ar.estado_asignacion_rutina,
                   (ue.nombres_usuario || ' ' || ue.apellidos_usuario) AS entrenador
            FROM asignaciones_rutina_usuario ar
            INNER JOIN rutinas r ON ar.id_rutina_fk = r.id_rutina_pk
            INNER JOIN objetivos_rutina o ON r.id_objetivo_rutina_fk = o.id_objetivo_rutina_pk
            INNER JOIN niveles_rutina n ON r.id_nivel_rutina_fk = n.id_nivel_rutina_pk
            INNER JOIN entrenadores en ON ar.id_entrenador_asigna_rutina_fk = en.id_entrenador_pk
            INNER JOIN usuarios ue ON en.id_usuario_entrenador_fk = ue.id_usuario_pk
            WHERE ar.id_usuario_fk = ?
            ORDER BY ar.fecha_hora_inicio_asignacion_rutina DESC
        """
        cursor.execute(sql, (aprendiz_id,))
        rows = cursor.fetchall()
        if not rows:
            print("  No tienes rutinas asignadas.")
        else:
            for r in rows:
                estado = "Activa" if r[6] == 1 else "Finalizada/Inactiva"
                print("-" * 60)
                print(f"  Asignación ID: {r[0]}\n  Rutina: {r[1]}\n  Objetivo: {r[2]} | Nivel: {r[3]}\n  Inicio: {r[4]} | Fin: {r[5]}\n  Estado: {estado}\n  Asignada por: {r[7]}")
                cursor.execute("""
                    SELECT ej.nombre_ejercicio, dr.series_rutina, dr.repeticiones_rutina
                    FROM detalles_rutina dr
                    INNER JOIN ejercicios ej ON dr.id_ejercicio_rutina_fk = ej.id_ejercicio_pk
                    WHERE dr.id_rutina_fk = (SELECT id_rutina_fk FROM asignaciones_rutina_usuario WHERE id_asignacion_rutina_usuario_pk = ?)
                """, (r[0],))
                ejercicios = cursor.fetchall()
                if ejercicios:
                    print("  Ejercicios:")
                    for ej in ejercicios:
                        print(f"    - {ej[0]}: {ej[1]} series x {ej[2]} reps")
            print("-" * 60)
    except Exception as error:
        print(f"✕ Error: {error}")
    finally:
        cursor.close()
        database.close()


def my_progress(user):
    clear()
    print("\n「 MI PROGRESO 」\n")
    database, cursor = _db()
    try:
        sql = """
            SELECT sp.id_seguimiento_progreso_usuario_pk, sp.horas_ludicas,
                   sp.rutinas_completadas, sp.fecha_registro_progreso, sp.observacion_progreso_usuario
            FROM seguimientos_progreso_usuario sp
            WHERE sp.id_usuario_progreso_fk = ?
            ORDER BY sp.fecha_registro_progreso DESC
        """
        cursor.execute(sql, (user[0],))
        rows = cursor.fetchall()
        if not rows:
            print("  Aún no hay registros de progreso.")
        else:
            print("{:<6} {:<12} {:<18} {:<14} {}".format("ID", "Horas lúdicas", "Rutinas compl.", "Fecha", "Observación"))
            print("-" * 80)
            for r in rows:
                obs = (r[4] or "")[:30]
                print(f"{r[0]:<6} {r[1]:<12} {r[2]:<18} {str(r[3]):<14} {obs}")

            cursor.execute("SELECT SUM(horas_ludicas), SUM(rutinas_completadas) FROM seguimientos_progreso_usuario WHERE id_usuario_progreso_fk = ?", (user[0],))
            total = cursor.fetchone()
            print(f"\n  Total horas lúdicas: {total[0] or 0}\n  Total rutinas completadas: {total[1] or 0}")
    except Exception as error:
        print(f"✕ Error: {error}")
    finally:
        cursor.close()
        database.close()