"""
Menú del Administrador - AgroFit
Conectado a la base de datos agrofit.
"""

from features.users.admins import (
    show_my_profile,
    manage_users,
    generate_reports,
)


def admin_menu(user):
    """
    Menú principal del rol Administrador.
    user: resultado de authenticate() — tupla con datos del usuario.
    """
    while True:
        print("""
===================================================
               MENÚ ADMINISTRADOR
===================================================

        1. Mi perfil
        2. Usuarios
        3. Reportes
        4. Cerrar sesión

===================================================
        """)

        option = input("\n¿Qué deseas hacer?: ").strip()

        if option == "1":
            show_my_profile(user)

        elif option == "2":
            manage_users(user)

        elif option == "3":
            generate_reports(user)
            
        elif option == "4":
            print("\n✓ Sesión cerrada.")
            break

        else:
            print("\n✕ Opción no válida.")

        input("\nPresione Enter para continuar...")
