from core.components.clear import clear
from datetime import datetime


def validate_database(message, query_function, error_message, success_callback=None):
    while True:
        value = validate_text(message)

        result = query_function(value)

        if result:
            if callable(success_callback):
                success_callback(value, result)

            return result

        clear()
        print(error_message.format(value=value))


def validate_text(menssage):
    while True:
        text = input(menssage).strip()
        # Quitamos espacios para validar solo las letras
        letters_only = text.replace(" ", "")

        if not text:
            clear()
            print("\n✕ Este campo no puede estar vacío.")
        elif not letters_only.isalpha():
            clear()
            print("\n✕ Solo se permiten letras y espacios (sin números ni símbolos).")
        else:
            return text

def validate_password(message, min_len, confirm_password=True):

    """
    Solicita y valida una contraseña segura.

    La contraseña debe contener:
    - Mínimo la cantidad de caracteres indicada en min_len.
    - Al menos una letra.
    - Al menos un número.
    - Al menos un carácter especial.
    """

    while True:

        password = input(message)

        # 1. Validar que no esté vacía

        if not password:

            clear()

            print("\n✕ La contraseña no puede estar vacía.")

            continue

        # 2. Validar longitud mínima

        if len(password) < min_len:

            clear()

            print(f"\n✕ La contraseña debe tener al menos {min_len} caracteres.")

            continue

        # 3. Validar que contenga al menos una letra

        if not any(char.isalpha() for char in password):

            clear()

            print("\n✕ La contraseña debe contener al menos una letra.")

            continue

        # 4. Validar que contenga al menos un número

        if not any(char.isdigit() for char in password):

            clear()

            print("\n✕ La contraseña debe contener al menos un número.")

            continue

        # 5. Validar que contenga al menos un carácter especial

        if not any(not char.isalnum() for char in password):

            clear()

            print("\n✕ La contraseña debe contener al menos un carácter especial.")

            continue

        # 6. Confirmación de contraseña

        if confirm_password:

            password_confirmation = input("Confirma tu contraseña: ")

            if password != password_confirmation:

                clear()

                print("\n✕ Las contraseñas no coinciden. Inténtalo de nuevo.")

                continue

        print("\n✓ ¡Contraseña ingresada correctamente!")

        return password


def validate_email(message, required_domain=None):
    """
    Solicita y valida un correo electrónico sin usar expresiones regulares.

    Parámetros:
    - message (str): El texto a mostrar en consola.
    - required_domain (str, opcional): Dominio exigido, ej: "@soy.sena.edu.co".
    """

    while True:

        email = input(message).strip().lower()

        # 1. Validar que no esté vacío
        if not email:
            clear()
            print("\n✕ El correo electrónico no puede estar vacío.")
            continue

        # 2. Validar estructura básica
        if email.count("@") != 1:
            clear()
            print("\n✕ El correo debe contener exactamente un símbolo '@'.")
            continue

        username, domain = email.split("@")

        if not username or not domain:
            clear()
            print("\n✕ El correo debe tener un usuario y un dominio válidos.")
            continue

        if "." not in domain or domain.startswith(".") or domain.endswith("."):
            clear()
            print(
                "\n✕ El dominio del correo debe incluir una extensión válida (ejemplo: .com, .edu.co)."
            )
            continue

        # 3. Validar dominio específico si es requerido
        if required_domain and not email.endswith(required_domain.lower()):
            clear()
            print(f"\n✕ El correo debe terminar estrictamente en {required_domain}")
            continue

        print("\n✓ ¡Correo electrónico ingresado correctamente!")

        return email


def validate_date(message, allow_future=True):
    """
    Solicita y valida una fecha en formato AAAA-MM-DD.

    Parámetros:
    - message (str): Texto mostrado al usuario.
    - allow_future (bool): Si es False, rechaza fechas posteriores a hoy.
    """

    while True:

        date_input = input(message).strip()

        if not date_input:
            clear()
            print("\n✕ La fecha no puede estar vacía.")
            continue

        try:
            # Convierte la cadena a objeto date
            valid_date = datetime.strptime(date_input, "%Y-%m-%d").date()

            # Validar si no se permiten fechas futuras
            if not allow_future and valid_date > datetime.now().date():
                clear()
                print("\n✕ La fecha no puede ser posterior al día de hoy.")
                continue

            # Validar año mínimo razonable
            if valid_date.year < 1900:
                clear()
                print("\n✕ Ingresa un año válido (posterior a 1900).")
                continue

            print("\n✓ ¡La fecha es correcta!")

            return valid_date

        except ValueError:
            clear()
            print(
                "\n✕ Formato o fecha inválida, usa el formato AAAA-MM-DD (ejemplo: 2006-09-27)."
            )


def validate_len(message, min_len, max_len):
    """
    Solicita y valida cualquier entrada que deba ser estrictamente numérica
    y que deba cumplir con un rango de longitud.
    """
    while True:
        value = input(message).strip()

        if not value:
            clear()
            print("\n✕ Este campo no puede estar vacío.")
        elif not value.isdigit():
            clear()
            print(
                "\n✕ Has ingresado caracteres no numéricos. Solo se permiten números."
            )
        elif not (min_len <= len(value) <= max_len):
            clear()
            if min_len == max_len:
                print(f"\n✕ El valor debe tener exactamente {min_len} dígitos.")
            else:
                print(f"\n✕ El valor debe tener entre {min_len} y {max_len} dígitos.")
        else:
            return value


def select_option(title, options):
    while True:
        print(f"\n「 {title} 」")

        for key, value in options.items():
            print(f"  {key}. {value}")

        selection = input("\nSelecciona una opción: ").strip()

        # Coincidencia directa
        if selection in options:
            selected_text = options[selection]
            print(f"\n✓ Has seleccionado: {selected_text}")
            return selection, selected_text

        # Coincidencia ignorando mayúsculas/minúsculas
        for key in options:
            if str(key).lower() == selection.lower():
                selected_text = options[key]
                print(f"\n✓ Has seleccionado: {selected_text}")
                return key, selected_text

        clear()
        print("\n✕ Opción no válida.")


def validate_confirmation(
    question,
    callback=None,
    fallback="✓ No se registró la información.",
    default_value=None,
):
    while True:
        option = input(f"\n{question} (S/N): ").strip().lower()

        if option == "s":
            if callable(callback):
                return callback()

            if isinstance(callback, str):
                while True:
                    value = input(f"\n{callback}").strip()

                    if value:
                        return value

                    clear()
                    print("\n✕ Este campo no puede estar vacío.")

            return True

        if option == "n":
            print(f"\n{fallback}")
            return default_value

        clear()
        print("\n✕ Por favor, responda 'S' o 'N'.")


def validate_phone(message, min_len, max_len, previous_phone=None):
    """
    Valida que un teléfono tenga formato válido.
    Admite '+' al inicio, espacios y guiones.
    """

    while True:
        value = input(f"\n{message.strip()} ").strip()

        if not value:
            clear()
            print("\n✕ Este campo no puede estar vacío.")
            continue

        # Quitar '+' únicamente si está al inicio
        phone_value = value[1:] if value.startswith("+") else value

        # Validar caracteres permitidos
        if not all(char.isdigit() or char in (" ", "-") for char in phone_value):
            clear()
            print(
                "\n✕ Formato inválido. Solo se permiten números, espacios, guiones y '+' al inicio."
            )
            continue

        # Obtener únicamente los dígitos
        digits = "".join(char for char in value if char.isdigit())

        if not digits:
            clear()
            print(
                "\n✕ Formato inválido. Solo se permiten números, espacios, guiones y '+' al inicio."
            )
            continue

        # Validar cantidad de dígitos
        if not min_len <= len(digits) <= max_len:
            clear()

            if min_len == max_len:
                print(f"\n✕ El teléfono debe contener exactamente {min_len} dígitos.")
            else:
                print(
                    f"\n✕ El teléfono debe contener entre {min_len} y {max_len} dígitos numéricos."
                )

            continue

        # Comparar con el teléfono anterior
        if previous_phone is not None:
            previous_digits = "".join(
                char for char in str(previous_phone) if char.isdigit()
            )

            if digits == previous_digits:
                clear()
                print(
                    "\n✕ El teléfono secundario no puede ser igual al teléfono principal."
                )
                continue

        return value

def validate_multiple(
    quantity_message: str,
    item_callback,
    min_value: int = 1,
    unique_key: str = None,
) -> list:
    """Solicita una cantidad al usuario e itera sobre 'item_callback'

    para capturar y retornar una lista con los elementos registrados.
    Si se especifica 'unique_key', evita que se registren elementos duplicados.
    """
    while True:
        try:
            raw_input = input(quantity_message)
            quantity = int(raw_input)
            if quantity >= min_value:
                break
            print(f"✕ Debes ingresar un número mayor o igual a {min_value}.")
        except ValueError:
            print("✕ Entrada inválida. Por favor, ingresa un número entero.")

    items = []
    i = 1
    while i <= quantity:
        print(f"\n--- Registro #{i} ---")
        data = item_callback(i)

        # Validar si el campo clave ya se encuentra registrado previamente
        if unique_key and isinstance(data, dict) and unique_key in data:
            value_to_check = data[unique_key]
            already_exists = any(
                item.get(unique_key) == value_to_check for item in items
            )

            if already_exists:
                print("\n✕ Este elemento ya ha sido registrado. Por favor, selecciona uno diferente.")
                continue  # Repite la captura del registro actual (#i)

        items.append(data)
        i += 1

    return items