"""
Proyecto Python y MySQL por consola
- Abrir un asistente
- Login o registro
- Si elegimos registro, creara un usuario en la BD
- Si elegimos login, identifica al usuario y nos pregunta
"""

# app/shared/components/menu.py

from app.features.users import auth
from app.features.about.about import about
from app.features.contact.contact import contact

from app.shared.components.loading import loading
from app.shared.components.clear import clear


def show_menu():

    while True:

        print("""
                        MENÚ
===================================================

        1. Iniciar Sesión
        2. Recuperar contraseña
        3. Registrarse
        4. Sobre Nosotros
        5. Ubicación y Contacto
        6. Salir

===================================================
        """)

        hazel = auth.Auth()

        option = input("\n¿Qué deseas hacer?: ").strip()

        if option == "1":

            clear()
            print("\n✓ Has seleccionado: Iniciar Sesión")

            hazel.login()

        elif option == "2":

            clear()
            print("\n✓ Has seleccionado: Recuperar contraseña")

            hazel.recover_password()

        elif option == "3":

            clear()
            print("\n✓ Has seleccionado: Registrarse")

            hazel.register()

        elif option == "4":

            clear()
            print("\n✓ Has seleccionado: Sobre Nosotros")

            about()

        elif option == "5":

            clear()
            print("\n✓ Has seleccionado: Ubicación y Contacto")

            Contact = contact()
            Contact.send_message()

        elif option == "6":

            clear()
            print("\n✓ Has seleccionado: Salir")

            print("\nOk, hasta pronto!!!...")

            loading("Saliendo del programa")

            print("✓ El programa se ha cerrado correctamente")

            exit()

        else:

            clear()

            print("\n✕ Opción no válida, por favor intenta de nuevo.")

            input("\nPresione Enter para regresar al menú...")

        clear()