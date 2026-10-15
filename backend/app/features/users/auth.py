import app.features.users.model as model
from app.shared.components.loading import loading
from app.shared.components.clear import clear
from data import queries as get
from app.shared.utils import validators as val
from app.cli.menus.role_menu import show_role_menu

"""
8:00 am a 5:00 pm Lunes a Viernes

Dayana
Camilo
Luz Elena
"""


class Auth:
    def register(self):
        loading("Ok!! Vamos a registrarte en el sistema")
        # 1. Rol y Documento
        id_role, text_role = val.select_option(
            "¿Cuál es tu tipo de cuenta?: ", get.roles()
        )

        id_dependency = None
        id_specialty = None
        id_admin_level = None
        leader_cohort = []  # Lista para almacenar las fichas: [{'id_cohort': ..., 'enrollment_date': ...}]
        cohort = []
        sena_email = None

        if id_role == 1:
            """
            disability = val.validate_confirmation(
                question="¿Presenta algún antecedente médico?",
                callback=lambda: val.validate_database(
                    message="\nDigite tu discapacidad médico: ",
                    query_function=get.disability,
                    error_message=(
                        "\n✕ El antecedente '{value}' no se encuentra registrado."
                    )
                ),
                fallback="✓ No se registró ningún antecedente médico.",
                default_value="Ninguno"
            )

            if disability != "Ninguno":
                print(f"\n✓ Antecedente médico registrado: {disability}")
            """
            sena_email = val.validate_email(
                message="\nDigita tu email institucional (@soy.sena.edu.co): ",
                required_domain="@soy.sena.edu.co",
            )

            if get.find_by_email(sena_email) is not None:
                print(f"\n✕ Alerta: El correo '{sena_email}' ya se encuentra registrado en el sistema.")
                input("\nPresione Enter para regresar...")
                return

            cohort = val.validate_multiple(
                quantity_message="\n¿Cuántas fichas tienes asociadas?: ",
                unique_key="id_cohort",
                item_callback=lambda i: {
                    "id_cohort": val.select_option(f"Selecciona la ficha #{i}: ", get.cohort())[0],
                    "enrollment_date": val.validate_date(
                        message=f"Digita la fecha de inscripción para la ficha #{i} (YYYY-MM-DD): "
                    ),
                },
            )
        elif id_role == 2:
            id_specialty, specialty_text = val.select_option(
                "¿Cuál es tu especialidad?: ", get.specialty()
            )
            sena_email = val.validate_email(
                message="\nDigita tu email institucional (@sena.edu.co): ",
                required_domain="@sena.edu.co",
            )
            if get.find_by_email(sena_email) is not None:
                print(f"\n✕ Alerta: El correo '{sena_email}' ya se encuentra registrado en el sistema.")
                input("\nPresione Enter para regresar...")
                return
            cohort = val.validate_multiple(
                quantity_message="\n¿Cuántas fichas tienes asociadas?: ",
                unique_key="id_cohort",
                item_callback=lambda i: {
                    "id_cohort": val.select_option(f"Selecciona la ficha #{i}: ", get.cohort())[0],
                    "enrollment_date": val.validate_date(
                        message=f"Digita la fecha de inscripción para la ficha #{i} (YYYY-MM-DD): "
                    ),
                },
            )

        elif id_role == 3:
            id_dependency, dependency_text = val.select_option(
                "¿Cuál es tu dependencia?: ", get.dependency()
            )
            sena_email = val.validate_email(
                message="\nDigita tu email institucional (@sena.edu.co): ",
                required_domain="@sena.edu.co",
            )
            if get.find_by_email(sena_email) is not None:
                print(f"\n✕ Alerta: El correo '{sena_email}' ya se encuentra registrado en el sistema.")
                input("\nPresione Enter para regresar...")
                return
            # Preguntar si es instructor líder de ficha
            is_leader = val.validate_confirmation(
                question="\n¿Eres instructor líder de alguna ficha?"
            )

            if is_leader:
                print("\n--- Fichas que LIDERAS ---")
                leader_cohort = val.validate_multiple(
                    quantity_message="¿Cuántas fichas lideras?: ",
                    item_callback=lambda i: {
                        "id_cohort": val.select_option(
                            f"Selecciona la ficha que lideras #{i}: ", get.cohort()
                        )[0]
                    },
                )

            print("\n--- Fichas a las que PERTENECES ---")
            cohort = val.validate_multiple(
                quantity_message="\n¿Cuántas fichas tienes asociadas?: ",
                unique_key="id_cohort",
                item_callback=lambda i: {
                    "id_cohort": val.select_option(f"Selecciona la ficha #{i}: ", get.cohort())[0],
                    "enrollment_date": val.validate_date(
                        message=f"Digita la fecha de inscripción para la ficha #{i} (YYYY-MM-DD): "
                    ),
                },
            )
        elif id_role == 4:
            id_admin_level, admin_level_text = val.select_option(
                "¿Cuál es tu nivel?: ", get.admin_level()
            )
            sena_email = val.validate_email(
                message="\nDigita tu email institucional (@sena.edu.co): ",
                required_domain="@sena.edu.co",
            )
            if get.find_by_email(sena_email) is not None:
                print(f"\n✕ Alerta: El correo '{sena_email}' ya se encuentra registrado en el sistema.")
                input("\nPresione Enter para regresar...")
                return
        id_document_type, document_type_text = val.select_option(
            "¿Cual es tu tipo de documento?: ", get.document_type()
        )

        document_number = val.validate_len(
            "\nDigita tu número de documento: ", min_len=6, max_len=11
        )

        if get.find_by_document_number(document_number) is not None:
            print(f"\n✕ Alerta: El documento número '{document_number}' ya se encuentra registrado en el sistema.")
            input("\nPresione Enter para regresar...")
            return

        # 2. Datos Personales
        # --- NOMBRES Y APELLIDOS ---
        names = val.validate_text("\n¿Cuáles son tus nombres?: ")
        surnames = val.validate_text("\n¿Cuáles son tus apellidos?: ")

        birth_date = val.validate_date(
            "\nDigita tu fecha de nacimiento (AAAA-MM-DD): ", allow_future=False
        )

        id_gender, gender_text = val.select_option(
            "¿Cual es tu género?: ", get.gender()
        )

        id_marital_status, marital_status_text = val.select_option(
            "¿Cual es tu estado civil?: ", get.marital_status()
        )

        id_blood_type, blood_type_text = val.select_option(
            "¿Cual es tu tipo de sangre?: ", get.blood_type()
        )

        # 3. Credenciales y Contacto
        password = val.validate_password(
            message="\nDigita tu contraseña: ", min_len=8, confirm_password=True
        )

        # --- TELÉFONO PRINCIPAL ---
        phone = val.validate_confirmation(
            question="¿Tiene número de teléfono principal?",
            callback=lambda: val.validate_phone(
                message="Digita tu número de teléfono: ", min_len=11, max_len=11
            ),
        )

        # --- TELÉFONO SECUNDARIO ---
        secondary_phone = val.validate_confirmation(
            question="¿Tiene número de teléfono secundario?",
            callback=lambda: val.validate_phone(
                message="Digita tu número de teléfono secundario: ",
                previous_phone=phone,
                min_len=11,
                max_len=11,
            ),
        )

        id_municipality, birth_city, id_department, city_department = (
            val.validate_database(
                message="\nDigita tu municipio de nacimiento: ",
                query_function=get.divipole,
                error_message=(
                    "\n✕ El municipio '{value}' no existe en Colombia o está mal escrito."
                ),
            )
        )

        print(f"\n✓ Municipio ingresado: {birth_city}")
        print(f"✓ Departamento asignado: {city_department}")

        address = input("Digita tu dirección de residencia: ").strip()

        while not address:
            clear()
            print("\n✕ La dirección no puede estar vacía.")
            address = input("Digita tu dirección de residencia: ").strip()

        id_eps, eps_text = val.select_option("¿Cual es tu EPS?: ", get.eps())

        id_hospital, hospital_text = val.select_option(
            "¿Cual es tu Hospital?: ", get.hospital()
        )

        """
        training_center = get.training_center()
        id_training_center, text_training_center = val.select_option("¿Cuál es tu centro de formación?: ", training_center)
        """

        user = model.User(
            role=id_role,
            document_type=id_document_type,
            document_number=document_number,
            birth_date=birth_date,
            names=names,
            surnames=surnames,
            gender=id_gender,
            marital_status=id_marital_status,
            blood_type=id_blood_type,
            sena_email=sena_email,
            password=password,
            phone=phone,
            secondary_phone=secondary_phone,
            municipality=id_municipality,
            department=id_department,
            address=address,
            eps=id_eps,
            hospital=id_hospital,
            dependency=id_dependency,
            specialty=id_specialty,
            admin_level=id_admin_level,
            cohort=leader_cohort,
            leader_cohort=cohort,
        )
        register = user.register()

        if register[0] >= 1:
            print(
                f"\n✓ Perfecto {register[1].names} te has registrado con el email {register[1].sena_email}"
            )
            input("\nPresione Enter para continuar...")
        else:
            print("\n✕ No te has registrado correctamente!! Intentalo más tarde...")
            input("\nPresione Enter para continuar...")

    def login(self):

        loading("Vale!! Identificate en el sistema")

        # Imprimir usuarios de prueba
        print("\n========================================================")
        print("                 USUARIOS DE PRUEBA                     ")
        print("========================================================")
        print("1. APRENDIZ:")
        print("   • Email: santiago.gomez@soy.sena.edu.co | Clave: Clave1234*")
        print("2. ENTRENADOR:")
        print("   • Email: carlos.mendoza@sena.edu.co     | Clave: Clave1234*")
        print("3. FUNCIONARIO:")
        print("   • Email: marta.perez@sena.edu.co        | Clave: Clave1234*")
        print("4. ADMINISTRADOR:")
        print("   • Email: andres.vargas@sena.edu.co      | Clave: Clave1234*")
        print("========================================================\n")

        try:

            sena_email = val.validate_email(message="\nDigita tu email institucional: ")

            password = val.validate_password(
                message="\nDigita tu contraseña: ", min_len=8, confirm_password=False
            )

            user = model.User(sena_email=sena_email, password=password)

            login = user.authenticate()

            if login:

                print(f"\n✓ Bienvenid@ a AgroFit, " f"{login[2]} {login[3]}.")

                role = login[5]
                show_role_menu(role, login)

            else:

                print("\n✕ Correo o contraseña incorrectos.")

        except Exception as error:

            print(f"\n✕ Error al iniciar sesión: {error}")

        input("\nPresione Enter para continuar...")

    def recover_password(self):

        print("\n========================================================")
        print("              RECUPERACIÓN DE CONTRASEÑA                ")
        print("========================================================")

        sena_email = val.validate_email(message="\nDigita tu email institucional: ")

        user = model.User(sena_email=sena_email)

        exists = get.find_by_email(sena_email)

        if exists is None:
            print("\n✕ No existe una cuenta registrada con ese email.")
            input("\nPresione Enter para continuar...")
            return

        print(f"\n✓ Cuenta encontrada: {exists[7]} {exists[8]}")

        new_password = val.validate_password(
            message="\nDigita tu nueva contraseña: ", min_len=8, confirm_password=True
        )

        user.password = new_password

        result = user.recover_password(new_password)

        if result[0] >= 1:
            print("\n========================================================")
            print("         CONTRASEÑA ACTUALIZADA CORRECTAMENTE           ")
            print("========================================================")
            print("✓ Ya puedes iniciar sesión con tu nueva contraseña.")
        else:
            print("\n✕ No se pudo actualizar la contraseña. Inténtalo más tarde.")

        input("\nPresione Enter para continuar...")
