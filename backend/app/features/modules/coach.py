"""
Lógica funcional del rol Entrenador - AgroFit
Todas las operaciones conectadas a la base de datos agrofit (SQLite).
"""

from app.shared.components.clear import clear
from app.shared.database.connection import Connect_SQLite


def _db():
    database, cursor = Connect_SQLite()
    return database, cursor


def _get_entrenador_id(user_id):
    database, cursor = _db()
    try:
        cursor.execute(
            "SELECT id_entrenador_pk FROM entrenadores WHERE id_usuario_entrenador_fk = ?",
            (user_id,),
        )
        row = cursor.fetchone()
        return row[0] if row else None
    except Exception:
        return None
    finally:
        cursor.close()
        database.close()


def show_my_profile(user):
    """Perfil del entrenador autenticado."""
    clear()
    print("\n「 MI PERFIL - ENTRENADOR 」\n")

    database, cursor = _db()
    try:
        sql = """
            SELECT
                u.id_usuario_pk,
                u.numero_documento_usuario,
                td.nombre_tipo_documento,
                u.correo_usuario,
                u.telefono_usuario,
                u.nombres_usuario,
                u.apellidos_usuario,
                s.nombre_sexo,
                u.fecha_nacimiento_usuario,
                ee.nombre_especialidad_entrenador,
                e.estado_entrenador
            FROM usuarios u
            INNER JOIN tipos_documento td ON u.cod_tipo_documento_usuario_fk = td.cod_tipo_documento_pk
            INNER JOIN sexos s ON u.cod_sexo_usuario_fk = s.cod_sexo_pk
            INNER JOIN entrenadores e ON e.id_usuario_entrenador_fk = u.id_usuario_pk
            INNER JOIN especialidades_entrenador ee
                ON e.id_especialidad_entrenador_fk = ee.id_especialidad_entrenador_pk
            WHERE u.id_usuario_pk = ?
        """
        cursor.execute(sql, (user[0],))
        row = cursor.fetchone()

        if not row:
            print("✕ No se encontró información del perfil de entrenador.")
            return

        labels = [
            "ID Usuario",
            "Documento",
            "Tipo Documento",
            "Correo",
            "Teléfono",
            "Nombres",
            "Apellidos",
            "Sexo",
            "Fecha Nacimiento",
            "Especialidad",
            "Estado",
        ]
        for label, value in zip(labels, row):
            if label == "Estado":
                value = "Activo" if value == 1 else "Inactivo"
            print(f"  {label:<20}: {value}")

    except Exception as error:
        print(f"✕ Error al consultar perfil: {error}")
    finally:
        cursor.close()
        database.close()


def my_learners(user):
    """Lista todos los aprendices vinculados a las fichas asignadas al entrenador."""
    clear()
    print("\n「 MIS APRENDICES REGISTRADOS EN FICHAS 」\n")

    database, cursor = _db()
    try:
        # Obtener el ID del entrenador
        entrenador_id = _get_entrenador_id(user[0])
        
        sql = """
            SELECT DISTINCT
                a.id_aprendiz_pk,
                u.numero_documento_usuario,
                u.nombres_usuario,
                u.apellidos_usuario,
                u.correo_usuario,
                ff.numero_ficha,
                pf.nombre_programa
            FROM fichas_usuarios fu_entrenador
            INNER JOIN fichas_formacion ff ON fu_entrenador.id_ficha_fk = ff.id_ficha_formacion_pk
            INNER JOIN programas_formacion pf ON ff.id_programa_ficha_fk = pf.id_programa_pk
            INNER JOIN fichas_usuarios fu_aprendiz ON fu_aprendiz.id_ficha_fk = ff.id_ficha_formacion_pk
            INNER JOIN usuarios u ON fu_aprendiz.id_usuario_ficha_fk = u.id_usuario_pk
            INNER JOIN aprendices a ON a.id_usuario_aprendiz_fk = u.id_usuario_pk
            WHERE (fu_entrenador.id_usuario_ficha_fk = ? OR fu_entrenador.id_usuario_ficha_fk = ?)
              AND u.estado_usuario = 1
            ORDER BY ff.numero_ficha, u.apellidos_usuario, u.nombres_usuario
        """
        # Se envía tanto el id_usuario_pk como el id_entrenador_pk por si fu_entrenador guarda cualquiera de los dos
        cursor.execute(sql, (user[0], entrenador_id or 0))
        rows = cursor.fetchall()

        if not rows:
            print("  No hay aprendices asociados a tus fichas de formación.")
        else:
            print(
                "{:<8} {:<12} {:<28} {:<10} {}".format(
                    "ID Apr", "Documento", "Nombre Aprendiz", "Ficha", "Programa"
                )
            )
            print("-" * 85)
            for r in rows:
                nombre_completo = f"{r[2]} {r[3]}"
                programa = (r[6] or "")[:20]
                print(
                    f"{r[0]:<8} {r[1]:<12} {nombre_completo[:26]:<28} {r[5]:<10} {programa}"
                )

    except Exception as error:
        print(f"✕ Error al consultar aprendices: {error}")
    finally:
        cursor.close()
        database.close()


def manage_routines(user):
    """Gestión de rutinas de entrenamiento."""
    clear()
    while True:
        print("""
「 RUTINAS DE ENTRENAMIENTO 」

  1. Listar rutinas
  2. Ver detalle de una rutina
  3. Crear nueva rutina
  4. Asignar rutina a aprendiz
  5. Ver asignaciones realizadas
  6. Volver
        """)
        opt = input("Opción: ").strip()

        if opt == "1":
            _list_routines()
        elif opt == "2":
            _routine_detail()
        elif opt == "3":
            _create_routine(user)
        elif opt == "4":
            _assign_routine(user)
        elif opt == "5":
            _my_assignments(user)
        elif opt == "6":
            break
        else:
            print("✕ Opción no válida.")


def _list_routines():
    database, cursor = _db()
    try:
        sql = """
            SELECT r.id_rutina_pk, r.nombre_rutina,
                   o.nombre_objetivo_rutina, n.nombre_nivel_rutina,
                   e.nombre_estado_rutina
            FROM rutinas r
            INNER JOIN objetivos_rutina o ON r.id_objetivo_rutina_fk = o.id_objetivo_rutina_pk
            INNER JOIN niveles_rutina n ON r.id_nivel_rutina_fk = n.id_nivel_rutina_pk
            INNER JOIN estados_rutina e ON r.id_estado_rutina_fk = e.id_estado_rutina_pk
            ORDER BY r.id_rutina_pk
        """
        cursor.execute(sql)
        rows = cursor.fetchall()
        if not rows:
            print("\n  No hay rutinas registradas.")
        else:
            print(
                "\n{:<6} {:<30} {:<18} {:<12} {}".format(
                    "ID", "Nombre", "Objetivo", "Nivel", "Estado"
                )
            )
            print("-" * 85)
            for r in rows:
                print(f"{r[0]:<6} {r[1][:28]:<30} {r[2]:<18} {r[3]:<12} {r[4]}")
    except Exception as error:
        print(f"✕ Error: {error}")
    finally:
        cursor.close()
        database.close()


def _routine_detail():
    try:
        rutina_id = int(input("\nDigite el ID de la rutina a consultar: ").strip())
    except ValueError:
        print("✕ ID inválido. Debe ingresar un número entero.")
        return

    database, cursor = _db()
    try:
        sql = """
            SELECT r.nombre_rutina, o.nombre_objetivo_rutina,
                   n.nombre_nivel_rutina, e.nombre_estado_rutina
            FROM rutinas r
            INNER JOIN objetivos_rutina o ON r.id_objetivo_rutina_fk = o.id_objetivo_rutina_pk
            INNER JOIN niveles_rutina n ON r.id_nivel_rutina_fk = n.id_nivel_rutina_pk
            INNER JOIN estados_rutina e ON r.id_estado_rutina_fk = e.id_estado_rutina_pk
            WHERE r.id_rutina_pk = ?
        """
        cursor.execute(sql, (rutina_id,))
        header = cursor.fetchone()
        if not header:
            print("\n✕ No se encontró ninguna rutina con ese ID.")
            return

        print("\n" + "=" * 60)
        print(f"  RUTINA: {header[0]}")
        print(f"  Objetivo: {header[1]} | Nivel: {header[2]} | Estado: {header[3]}")
        print("=" * 60)

        cursor.execute(
            """
            SELECT ej.nombre_ejercicio, dr.series_rutina, dr.repeticiones_rutina
            FROM detalles_rutina dr
            INNER JOIN ejercicios ej ON dr.id_ejercicio_rutina_fk = ej.id_ejercicio_pk
            WHERE dr.id_rutina_fk = ?
        """,
            (rutina_id,),
        )
        detalles = cursor.fetchall()
        if detalles:
            print(
                "\n{:<35} {:<10} {}".format(
                    "Ejercicio", "Series", "Repeticiones"
                )
            )
            print("-" * 60)
            for d in detalles:
                print(f"{d[0][:33]:<35} {d[1]:<10} {d[2]}")
        else:
            print("\n  (Sin ejercicios asociados)")
        print("=" * 60)

    except Exception as error:
        print(f"✕ Error: {error}")
    finally:
        cursor.close()
        database.close()


def _create_routine(user):
    clear()
    print("\n「 CREAR NUEVA RUTINA 」\n")

    database, cursor = _db()
    try:
        nombre = input("Nombre de la rutina: ").strip()
        if not nombre:
            print("✕ El nombre no puede estar vacío.")
            return

        cursor.execute("SELECT id_objetivo_rutina_pk, nombre_objetivo_rutina FROM objetivos_rutina")
        objetivos = cursor.fetchall()
        print("\nObjetivos disponibles:")
        for obj in objetivos:
            print(f"  [{obj[0]}] {obj[1]}")
        id_objetivo = int(input("Selecciona el ID del objetivo: ").strip())

        cursor.execute("SELECT id_nivel_rutina_pk, nombre_nivel_rutina FROM niveles_rutina")
        niveles = cursor.fetchall()
        print("\nNiveles disponibles:")
        for niv in niveles:
            print(f"  [{niv[0]}] {niv[1]}")
        id_nivel = int(input("Selecciona el ID del nivel: ").strip())

        sql_rutina = """
            INSERT INTO rutinas (nombre_rutina, id_objetivo_rutina_fk, id_nivel_rutina_fk, id_estado_rutina_fk)
            VALUES (?, ?, ?, 1)
        """
        cursor.execute(sql_rutina, (nombre, id_objetivo, id_nivel))
        rutina_id = cursor.lastrowid

        cursor.execute("SELECT id_ejercicio_pk, nombre_ejercicio FROM ejercicios")
        ejercicios = cursor.fetchall()

        print("\n--- AGREGAR EJERCICIOS A LA RUTINA ---")
        cant_ejercicios = int(input("¿Cuántos ejercicios incluirá esta rutina?: ").strip())

        for i in range(1, cant_ejercicios + 1):
            print(f"\nEjercicio #{i}:")
            for ej in ejercicios:
                print(f"  [{ej[0]}] {ej[1]}")
            id_ejercicio = int(input("  ID del ejercicio: ").strip())
            series = int(input("  Número de series: ").strip())
            reps = int(input("  Número de repeticiones: ").strip())

            sql_detalle = """
                INSERT INTO detalles_rutina (series_rutina, repeticiones_rutina, id_rutina_fk, id_ejercicio_rutina_fk)
                VALUES (?, ?, ?, ?)
            """
            cursor.execute(sql_detalle, (series, reps, rutina_id, id_ejercicio))

        database.commit()
        print(f"\n✓ Rutina '{nombre}' (ID: {rutina_id}) creada exitosamente.")

    except ValueError:
        print("\n✕ Entrada inválida. Operación cancelada.")
        database.rollback()
    except Exception as error:
        print(f"\n✕ Error al crear rutina: {error}")
        database.rollback()
    finally:
        cursor.close()
        database.close()


def _assign_routine(user):
    entrenador_id = _get_entrenador_id(user[0])
    if not entrenador_id:
        print("✕ No se encontró registro de entrenador.")
        return

    database, cursor = _db()
    try:
        cursor.execute("""
            SELECT r.id_rutina_pk, r.nombre_rutina, o.nombre_objetivo_rutina
            FROM rutinas r
            INNER JOIN objetivos_rutina o ON r.id_objetivo_rutina_fk = o.id_objetivo_rutina_pk
            WHERE r.id_estado_rutina_fk = 1
        """)
        rutinas = cursor.fetchall()

        if not rutinas:
            print("\n✕ No existen rutinas registradas en el sistema.")
            return

        print("\n--- RUTINAS DISPONIBLES ---")
        for r in rutinas:
            print(f"  [{r[0]}] {r[1]} - ({r[2]})")

        rutina_id = int(input("\nDigite el ID de la rutina a asignar: ").strip())

        if not any(r[0] == rutina_id for r in rutinas):
            print("\n✕ Error: El ID de rutina seleccionado no es válido.")
            return

        cursor.execute("""
            SELECT a.id_aprendiz_pk, u.nombres_usuario, u.apellidos_usuario, u.numero_documento_usuario
            FROM aprendices a
            INNER JOIN usuarios u ON a.id_usuario_aprendiz_fk = u.id_usuario_pk
            WHERE u.estado_usuario = 1
        """)
        aprendices = cursor.fetchall()

        if not aprendices:
            print("\n✕ No hay aprendices activos registrados.")
            return

        print("\n--- APRENDICES REGISTRADOS ---")
        for ap in aprendices:
            print(f"  [{ap[0]}] {ap[1]} {ap[2]} (Doc: {ap[3]})")

        aprendiz_id = int(input("\nDigite el ID del aprendiz (id_aprendiz_pk): ").strip())

        if not any(ap[0] == aprendiz_id for ap in aprendices):
            print("\n✕ Error: El ID del aprendiz especificado no existe.")
            return

        fecha_inicio = input("Fecha/hora inicio (YYYY-MM-DD HH:MM:SS): ").strip()
        fecha_fin = input("Fecha/hora fin (YYYY-MM-DD HH:MM:SS): ").strip()

        if len(fecha_inicio) == 10:
            fecha_inicio += " 00:00:00"
        if len(fecha_fin) == 10:
            fecha_fin += " 23:59:59"

        sql = """
            INSERT INTO asignaciones_rutina_usuario
            (id_rutina_fk, id_usuario_fk, fecha_hora_inicio_asignacion_rutina,
             fecha_hora_fin_asignacion_rutina, estado_asignacion_rutina,
             id_entrenador_asigna_rutina_fk)
            VALUES (?, ?, ?, ?, 1, ?)
        """
        cursor.execute(
            sql,
            (rutina_id, aprendiz_id, fecha_inicio, fecha_fin, entrenador_id),
        )
        database.commit()
        print("\n✓ Rutina asignada correctamente.")

    except ValueError:
        print("\n✕ Datos ingresados no válidos.")
        database.rollback()
    except Exception as error:
        print(f"\n✕ Error al asignar: {error}")
        database.rollback()
    finally:
        cursor.close()
        database.close()


def _my_assignments(user):
    entrenador_id = _get_entrenador_id(user[0])
    if not entrenador_id:
        print("✕ No se encontró registro de entrenador.")
        return

    database, cursor = _db()
    try:
        sql = """
            SELECT ar.id_asignacion_rutina_usuario_pk,
                   r.nombre_rutina,
                   u.nombres_usuario, u.apellidos_usuario,
                   ar.fecha_hora_inicio_asignacion_rutina,
                   ar.fecha_hora_fin_asignacion_rutina,
                   ar.estado_asignacion_rutina
            FROM asignaciones_rutina_usuario ar
            INNER JOIN rutinas r ON ar.id_rutina_fk = r.id_rutina_pk
            INNER JOIN aprendices a ON ar.id_usuario_fk = a.id_aprendiz_pk
            INNER JOIN usuarios u ON a.id_usuario_aprendiz_fk = u.id_usuario_pk
            WHERE ar.id_entrenador_asigna_rutina_fk = ?
            ORDER BY ar.id_asignacion_rutina_usuario_pk DESC
            LIMIT 30
        """
        cursor.execute(sql, (entrenador_id,))
        rows = cursor.fetchall()
        if not rows:
            print("\n  No hay asignaciones registradas.")
        else:
            print(
                "\n{:<6} {:<25} {:<22} {:<20} {}".format(
                    "ID", "Rutina", "Aprendiz", "Inicio", "Estado"
                )
            )
            print("-" * 90)
            for r in rows:
                nombre = f"{r[2]} {r[3]}"
                estado = "Activa" if r[6] == 1 else "Finalizada/Inactiva"
                print(
                    f"{r[0]:<6} {r[1][:23]:<25} {nombre[:20]:<22} {str(r[4])[:19]:<20} {estado}"
                )
    except Exception as error:
        print(f"✕ Error: {error}")
    finally:
        cursor.close()
        database.close()


def manage_physical_evaluations(user):
    """Gestión de evaluaciones físicas."""
    clear()
    while True:
        print("""
「 EVALUACIONES FÍSICAS 」

  1. Listar mis evaluaciones realizadas
  2. Registrar nueva evaluación
  3. Ver detalle de evaluación
  4. Volver
        """)
        opt = input("Opción: ").strip()

        if opt == "1":
            _list_my_evaluations(user)
        elif opt == "2":
            _register_evaluation(user)
        elif opt == "3":
            _evaluation_detail()
        elif opt == "4":
            break
        else:
            print("✕ Opción no válida.")


def _list_my_evaluations(user):
    entrenador_id = _get_entrenador_id(user[0])
    if not entrenador_id:
        print("✕ No se encontró registro de entrenador.")
        return

    database, cursor = _db()
    try:
        sql = """
            SELECT ef.id_evaluacion_fisica_pk,
                   u.nombres_usuario, u.apellidos_usuario,
                   ef.fecha_evaluacion, ef.peso_evaluacion,
                   ef.altura_evaluacion, na.nombre_nivel_actividad_fisica
            FROM evaluaciones_fisicas ef
            INNER JOIN usuarios u ON ef.id_usuario_evaluacion_fk = u.id_usuario_pk
            INNER JOIN niveles_actividad_fisica na
                ON ef.id_nivel_actividad_fisica_evaluacion_fk = na.id_nivel_actividad_fisica_pk
            WHERE ef.id_entrenador_encargado_evaluacion_fk = ?
            ORDER BY ef.fecha_evaluacion DESC
            LIMIT 30
        """
        cursor.execute(sql, (entrenador_id,))
        rows = cursor.fetchall()
        if not rows:
            print("\n  No hay evaluaciones registradas.")
        else:
            print(
                "\n{:<6} {:<25} {:<12} {:<8} {:<8} {}".format(
                    "ID", "Usuario", "Fecha", "Peso", "Altura", "Nivel Act."
                )
            )
            print("-" * 80)
            for r in rows:
                nombre = f"{r[1]} {r[2]}"
                print(
                    f"{r[0]:<6} {nombre[:23]:<25} {str(r[3]):<12} {r[4]:<8} {r[5]:<8} {r[6]}"
                )
    except Exception as error:
        print(f"✕ Error: {error}")
    finally:
        cursor.close()
        database.close()


def _register_evaluation(user):
    """Registra una nueva evaluación física calculando automáticamente la grasa corporal y el índice muscular, seleccionando opciones desde la BD."""
    entrenador_id = _get_entrenador_id(user[0])
    if not entrenador_id:
        print("✕ No se encontró registro de entrenador.")
        return

    database, cursor = _db()
    try:
        id_usuario = int(input("\nID del usuario a evaluar: ").strip())
        peso = float(input("Peso (kg): ").strip())
        altura = float(input("Altura (m): ").strip())
        presion = input("Presión arterial: ").strip()
        fecha = input("Fecha evaluación (YYYY-MM-DD): ").strip()

        # --- SELECCIÓN DE NIVEL DE ACTIVIDAD FÍSICA DESDE LA BD ---
        cursor.execute("SELECT id_nivel_actividad_fisica_pk, nombre_nivel_actividad_fisica FROM niveles_actividad_fisica")
        niveles = cursor.fetchall()
        print("\n--- NIVELES DE ACTIVIDAD FÍSICA ---")
        for niv in niveles:
            print(f"  [{niv[0]}] {niv[1]}")
        id_nivel = int(input("Seleccione el ID del nivel de actividad física: ").strip())

        # --- SELECCIÓN DE ANTECEDENTE MÉDICO DESDE LA BD ---
        cursor.execute("SELECT id_antecedente_medico_pk, nombre_antecedente_medico FROM antecedentes_medicos")
        antecedentes = cursor.fetchall()
        print("\n--- ANTECEDENTES MÉDICOS ---")
        for ant in antecedentes:
            print(f"  [{ant[0]}] {ant[1]}")
        id_antec = int(input("Seleccione el ID del antecedente médico: ").strip())

        # --- SELECCIÓN DE COMPLEXIÓN FÍSICA DESDE LA BD ---
        cursor.execute("SELECT id_complexion_fisica_pk, nombre_complexion_fisica FROM complexiones_fisicas")
        complexiones = cursor.fetchall()
        print("\n--- COMPLEXIÓN FÍSICA ---")
        for comp in complexiones:
            print(f"  [{comp[0]}] {comp[1]}")
        id_complex = int(input("Seleccione el ID de la complexión física: ").strip())

        observacion = input("\nObservaciones (opcional): ").strip() or None

        # --- CÁLCULO AUTOMÁTICO DE ÍNDICES BIOMÉTRICOS ---
        imc = peso / (altura ** 2)
        
        # Estimación estándar del porcentaje de grasa corporal según el IMC y nivel de actividad
        grasa_corp_calc = round(max(5.0, (1.20 * imc) + (0.23 * 25) - 5.4 - (id_nivel * 0.5)), 1)
        
        # Cálculo del índice de masa muscular estimada (Masa magra)
        grasa_musc_calc = round(100.0 - grasa_corp_calc, 1)

        grasa_corp = f"{grasa_corp_calc}%"
        grasa_musc = f"{grasa_musc_calc}%"

        print(f"\n✓ CÁLCULO BIOMÉTRICO AUTOMÁTICO:")
        print(f"  └─ IMC              : {round(imc, 2)} kg/m²")
        print(f"  └─ % Grasa Corporal : {grasa_corp}")
        print(f"  └─ % Índice Muscular: {grasa_musc}")

        # --- INSERCIÓN EN LA BASE DE DATOS ---
        sql = """
            INSERT INTO evaluaciones_fisicas
            (peso_evaluacion, id_nivel_actividad_fisica_evaluacion_fk,
             id_antecedente_medico_evaluacion_fk, fecha_evaluacion,
             grasa_corporal_evaluacion, grasa_muscular_evaluacion,
             altura_evaluacion, observacion_evaluacion,
             id_entrenador_encargado_evaluacion_fk,
             id_complexion_fisica_evaluacion_fk, presion_arterial,
             id_usuario_evaluacion_fk)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """
        cursor.execute(
            sql,
            (
                peso,
                id_nivel,
                id_antec,
                fecha,
                grasa_corp,
                grasa_musc,
                altura,
                observacion,
                entrenador_id,
                id_complex,
                presion,
                id_usuario,
            ),
        )
        database.commit()
        print("\n✓ Evaluación física registrada correctamente con sus cálculos biométricos.")

    except ValueError:
        print("✕ Datos inválidos.")
        database.rollback()
    except Exception as error:
        print(f"✕ Error al registrar: {error}")
        database.rollback()
    finally:
        cursor.close()
        database.close()


def _evaluation_detail():
    try:
        eval_id = int(input("\nDigite el ID de la evaluación a consultar: ").strip())
    except ValueError:
        print("✕ ID inválido. Debe ingresar un número entero.")
        return

    database, cursor = _db()
    try:
        sql = """
            SELECT
                u.nombres_usuario, u.apellidos_usuario, u.numero_documento_usuario,
                ef.fecha_evaluacion, ef.peso_evaluacion, ef.altura_evaluacion,
                ef.grasa_corporal_evaluacion, ef.grasa_muscular_evaluacion,
                ef.presion_arterial, na.nombre_nivel_actividad_fisica,
                am.nombre_antecedente_medico, cf.nombre_complexion_fisica,
                ef.observacion_evaluacion
            FROM evaluaciones_fisicas ef
            INNER JOIN usuarios u ON ef.id_usuario_evaluacion_fk = u.id_usuario_pk
            INNER JOIN niveles_actividad_fisica na 
                ON ef.id_nivel_actividad_fisica_evaluacion_fk = na.id_nivel_actividad_fisica_pk
            INNER JOIN antecedentes_medicos am 
                ON ef.id_antecedente_medico_evaluacion_fk = am.id_antecedente_medico_pk
            INNER JOIN complexiones_fisicas cf 
                ON ef.id_complexion_fisica_evaluacion_fk = cf.id_complexion_fisica_pk
            WHERE ef.id_evaluacion_fisica_pk = ?
        """
        cursor.execute(sql, (eval_id,))
        row = cursor.fetchone()

        if not row:
            print("\n✕ No se encontró ninguna evaluación física con ese ID.")
            return

        print("\n" + "=" * 50)
        print("   DETALLE DE LA EVALUACIÓN FÍSICA")
        print("=" * 50)
        print(f"  Usuario          : {row[0]} {row[1]} (Doc: {row[2]})")
        print(f"  Fecha            : {row[3]}")
        print(f"  Peso             : {row[4]} kg")
        print(f"  Altura           : {row[5]} m")
        print(f"  Grasa Corporal   : {row[6]}")
        print(f"  Grasa Muscular   : {row[7]}")
        print(f"  Presión Arterial : {row[8]}")
        print(f"  Nivel Actividad  : {row[9]}")
        print(f"  Antecedente Med. : {row[10]}")
        print(f"  Complexión       : {row[11]}")
        print(f"  Observaciones    : {row[12] or '(ninguna)'}")
        print("=" * 50)

    except Exception as error:
        print(f"✕ Error en la consulta: {error}")
    finally:
        cursor.close()
        database.close()


def learner_progress(user):
    """Consulta de progreso de aprendices."""
    clear()
    print("\n「 PROGRESO DE APRENDICES 」\n")

    doc = input(
        "Documento del aprendiz (o Enter para ver todos recientes): "
    ).strip()

    database, cursor = _db()
    try:
        if doc:
            sql = """
                SELECT sp.id_seguimiento_progreso_usuario_pk,
                       u.nombres_usuario, u.apellidos_usuario,
                       sp.horas_ludicas, sp.rutinas_completadas,
                       sp.fecha_registro_progreso, sp.observacion_progreso_usuario
                FROM seguimientos_progreso_usuario sp
                INNER JOIN usuarios u ON sp.id_usuario_progreso_fk = u.id_usuario_pk
                WHERE u.numero_documento_usuario = ?
                ORDER BY sp.fecha_registro_progreso DESC
            """
            cursor.execute(sql, (doc,))
        else:
            sql = """
                SELECT sp.id_seguimiento_progreso_usuario_pk,
                       u.nombres_usuario, u.apellidos_usuario,
                       sp.horas_ludicas, sp.rutinas_completadas,
                       sp.fecha_registro_progreso, sp.observacion_progreso_usuario
                FROM seguimientos_progreso_usuario sp
                INNER JOIN usuarios u ON sp.id_usuario_progreso_fk = u.id_usuario_pk
                ORDER BY sp.fecha_registro_progreso DESC
                LIMIT 20
            """
            cursor.execute(sql)

        rows = cursor.fetchall()
        if not rows:
            print("  No hay registros de progreso.")
        else:
            print(
                "{:<6} {:<25} {:<10} {:<12} {:<12} {}".format(
                    "ID", "Usuario", "Horas", "Rutinas", "Fecha", "Observación"
                )
            )
            print("-" * 95)
            for r in rows:
                nombre = f"{r[1]} {r[2]}"
                obs = (r[6] or "")[:25]
                print(
                    f"{r[0]:<6} {nombre[:23]:<25} {r[3]:<10} {r[4]:<12} {str(r[5]):<12} {obs}"
                )
    except Exception as error:
        print(f"✕ Error: {error}")
    finally:
        cursor.close()
        database.close()